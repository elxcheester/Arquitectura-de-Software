import wikipedia
import pageviewapi
import pymongo
import os
from pymongo import MongoClient


#print (wikipedia.search("Barack"))
#ny = wikipedia.page("New York")
#print(ny.title)

#Datos
notice =  pageviewapi.per_article('en.wikipedia', 'Barack', '20151106', '20151120',
                        access='all-access', agent='all-agents', granularity='daily')
#print(notice)

#conexion a bd y creacion de la base de datos
myclient = MongoClient(host=os.environ['MONGO_HOST'], port=int(os.environ['MONGO_PORT']))
db = myclient.wiki

#coleccion
datos = db.datos

result = datos.insert_one(notice)

print ('Objeto instertado ' + str(result.inserted_id))
