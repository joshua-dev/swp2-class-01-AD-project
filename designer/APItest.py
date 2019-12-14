import firebase_admin
from firebase_admin import credentials
import requests
import time

cred = credentials.Certificate(
    './kcc-library-firebase-adminsdk-tadou-6febe202b4.json')
firebase_admin.initialize_app(cred)

elasped_time = time.time()

res = requests.get(
    'https://us-central1-kcc-library.cloudfunctions.net/showAll')

print(res.status_code)

elasped_time = time.time() - elasped_time

print(f'API test took {elasped_time}seconds')
