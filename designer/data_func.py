from firebase import firebase
import requests
import json
import urllib.request

url = 'https://us-central1-kcc-library.cloudfunctions.net/showAll'
u = urllib.request.urlopen(url)
data = u.read()
print(data)


#firebase = firebase.FirebaseApplication('https://us-central1-kcc-library.cloudfunctions.net', None)
#result = firebase.get('/showAll', None)
#print(result)

