# -*- coding: utf-8 -*-
import pymongo
import json
import pandas as pd
import numpy as np
import time
from bson.son import SON

from database import returnHostString



def setConnectionPymongo(dbname, not_enc=False):
    
    client = pymongo.MongoClient(returnHostString(dbname))
    db = client[dbname]
    return db, dbname


def queryTodf(querySet):
    t = time.time()
    print(f"**MONGO: query with filters: {querySet._query}, time {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))}")
    listjson=querySet.to_json()
    obj = json.loads(listjson)
    D_out = pd.DataFrame.from_records(obj)
    elapsed = time.time() - t
    print(f"**MONGO: end query, time: {np.round(elapsed,1)} sec")
    return D_out

#inserisce una tabella di dati
def insert_data_many(db,collectionName,D_data):
    collection = db[collectionName]
    size = 100000 #maximum number of records per insert
    list_of_dfs = (D_data.loc[i:i+size-1,:] for i in range(0, len(D_data),size))
    inserted=0
    for data in list_of_dfs:
        records = json.loads(data.T.to_json()).values()
        res= collection.insert_many(records)
        inserted = inserted+ len(res.inserted_ids)
    print(f"Inseriti {str(inserted)} record in collezione {collectionName}")

#seleziona una tabella intera
def selectAllData(dbname,collectionName, not_enc=False):
    db, _ =setConnectionPymongo(dbname, not_enc)
    collection = db[collectionName]
    cursor = collection.find()
    fetch_data = list(cursor)
    df = pd.DataFrame(fetch_data)
    return df

def selectOneData(dbname,collectionName, not_enc=False):
    db, _ =setConnectionPymongo(dbname, not_enc)
    collection = db[collectionName]
    cursor = collection.find_one()
    fetch_data = list(cursor)
    df = pd.DataFrame(fetch_data)
    return df

def selectQueryData(dbname,collectionName,filter_query,project_query, not_enc=False):
    db, _=setConnectionPymongo(dbname, not_enc)
    collection = db[collectionName]
    cursor = collection.find(filter_query,project_query)
    fetch_data = list(cursor)
    df = pd.DataFrame(fetch_data)
    return df

def selectDistinct(dbname,collectionName,filter_query,project_query, not_enc=False):
    db, _ =setConnectionPymongo(dbname, not_enc)
    collection = db[collectionName]
    cursor = collection.distinct(filter_query,project_query)
    fetch_data = list(cursor)
    df = pd.DataFrame(fetch_data)
    return df


def listDatabase():
    client = pymongo.MongoClient('localhost',27017)
    dbs = client.list_database_names()
    for coll in ['admin','config','local']:
        dbs.remove(coll)
    return dbs


# %%
def groupBy(dbname, collectionName, group_variables, op_variables, resample_var=[], sort_var='',direction='', not_enc=False, filter_query={}):
    #dbname name of the db 
    # collectionName name of the collection/class
    
    #group_variables is a list of the fields of the collection to aggregate on.
    # [field1, field2, field3] is the equivalent to GROUP BY field1, field2, field3
    #insert variable names separated by a dot for nested var field1.fiel1nested

    #op_variables is a list of lists with two items where the 1st is the var and
    #the 2nd the operator to apply
    #[['field1','sum'],['field2','count']] is equal to
    #SELECT -----, SUM(field1), COUNT(field1)

    #sort_var is a sorting variable in the same format of an op_variable
    #['field_1','sum'] sort the table by the sum of field1
    #direction can be asc or desc
    
    #resample variable is a time variable to resample ['TIMESTAMP_IN','WEEK']


    
    #setto la connessione al database
    db, _ = setConnectionPymongo(dbname, not_enc)
    collection = db[collectionName]
    
    if len(filter_query)>0:
        pipeline=[filter_query]
    else:
        pipeline=[]
    
    
    

    ########## verifico se ci sono variabili da disaggregare (WIND) ###########
    #verifico fra le variabili di raggruppamento
    for var in group_variables:
        position = var.find('.') #cerco il punto nel nome delle variabili
        if position >-1: #se ho trovato il punto nella parola
            var_name = var[:position]
            pipeline.append({"$unwind": f"${var_name}"})

    #verifico fra le variabili di aggregazione
    for var,other in op_variables:
        position = var.find('.') #cerco il punto nel nome delle variabili
        if position >-1: #se ho trovato il punto nella parola
            var_name = var[:position]
            pipeline.append({"$unwind": f"${var_name}"})
            
    #################### ricampiono eventuali variabili temporali ############
    if len(resample_var)>0:
        var = resample_var[0]
        timespan=resample_var[1]
        
        #select format
        if timespan=='year':
            time_format = '%Y'
        elif timespan=='month':
            time_format = '%Y-%m'
        elif timespan =='week':
            time_format = '%Y-%u'
        else:
            time_format = '%Y-%m-%d'
            
        
        dict_project = {}
        
        dict_project["PERIOD"] =  { "$dateToString": 
                                               { "format": time_format, "date": f"${var}" } 
                                               }
        # add all the other variables                                
        for var in group_variables:
            dict_project[var] = 1
        for var in op_variables:
            dict_project[var[0]] = 1
            
        pipeline.append({"$project":dict_project})
        
        # add the period as grouping variable
        group_variables.append("PERIOD")
            

    ##################### costruisco il raggruppamento (GROUP) ################
    #creo il dizionario _id con le variabili di aggregazione
    _id = {}
    for gvar in group_variables:
        position = gvar.find('.') #cerco il punto nel nome delle variabili
        if position >-1: #se ho trovato il punto nella parola
            var_name = gvar[position+1:]
            _id[var_name] = "$"+str(gvar) #tolgo il punto dal nome della variabile
        else:
            _id[gvar] = "$"+str(gvar)

    #creo il dizionario group con tutta l'operazione di group by
    group = {}
    group['_id']=_id #aggiungo le variabili di aggregazione



    #aggiungo tutte le altre variabili con operatori
    for var,op in op_variables:
         #disaggrego eventuali aggregati
         position = var.find('.') #cerco il punto nel nome delle variabili
         if position >-1: #se ho trovato il punto nella parola
             var_name = var[position+1:]
         else:
             var_name = var
         if op.lower()=='count':
            group[op+"_"+var_name] = {"$sum":1}

         elif op.lower()=='sum':
            group[op+"_"+var_name] =  { "$sum": { '$convert': { 'input': "$"+var, 'to': "double" } } }
            
         elif op.lower()=='max':
             group[op+"_"+var_name] =  { "$max": "$"+var }
             
         elif op.lower()=='min':
             group[op+"_"+var_name] =  { "$min": "$"+var }

         else:
            group[op+"_"+var_name] = {"$"+op:"$"+var}

    pipeline.append({"$group": group})
    ################################# costruisco il sorting (SORT)
    #creo la tupla di sort
    if len(sort_var)>0:
        if direction.lower()=='desc': #descending sort
            sort = (sort_var[1]+"_"+sort_var[0],-1)
        else: #descending sort
            sort = (sort_var[1]+"_"+sort_var[0],1)
        pipeline.append({"$sort": SON([sort])})




    #fetch data
    print(pipeline)
    agg=collection.aggregate(pipeline,allowDiskUse=True)
    res=pd.DataFrame(list(agg))
    if len(res)>0:
        aggr = res['_id'].apply(pd.Series)
        aggr=aggr.join(res)
        res=aggr.drop('_id',axis=1) # drop index
    
    return res

# %% convert dates to pandas
def convertMongoToPandasDate(D_table, datefield):
    #converte le date estratte da mongobd
    #trovando dei dizionari converte usando le ms unit
    #altrimenti tenta una conversione con pandas_to_datetime
    D_table[datefield] = [pd.to_datetime(i['$date'], unit='ms',origin='unix') if isinstance(i,dict) else pd.to_datetime(i,errors='coerce') for i in D_table[datefield].values]
    #D_table[datefield] = [i['$date'] if isinstance(i,dict) else pd.to_datetime(i) for i in D_table[datefield].values]
    #D_table[datefield] =pd.to_datetime(D_table[datefield], unit='ms',origin='unix')
    return D_table


    
    
