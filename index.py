import firebase_admin as admin
from firebase_admin import credentials,firestore
import json
cred = credentials.Certificate('./python-shivaya.json')
default_app = admin.initialize_app(cred)

db=firestore.client()

container=[]
for doc in db.collection('pickers').get():
    print(doc.to_dict())
    container.append(doc.to_dict())


for each in container:
    print(each['truckDriverName'])
    #null means none in python