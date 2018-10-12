# Run the script with python importer.py

# Install dependencies with pip
# https://pip.pypa.io/en/stable/installing/
# Deps: firebase_admin, requests

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import requests
import json
from pprint import pprint

# sports.txt contains all sport names (first column of the spreadsheet seperated by /r)
# Must be in the same directory of the script
sports_file = open('sports.txt', 'r')
sportNames = sports_file.read().split('\r')
sports_file.close()

# SportsData.json is the downloaded json file
# Open SportsData.json and parse the json data
# Must be in the same directory as the script
with open('SportData.json') as data_file:
  json_data = json.load(data_file)

# Download the service account key from the firebase control panel
# Rename the downloaded file to serviceAccountKey.json and make sure it's in the same directory as the script
cred = credentials.Certificate('serviceAccountKey.json')

# Register and initialize the app
firebase_admin.initialize_app(cred)

# Get an instance of the firestore client
db = firestore.client()

# Loop through the json data where i is an integer in the range of the number of sport names
for i in range(len(sportNames)):
  # Create a new document named with the sport name in the collection sports
  doc_ref = db.collection(u'sports').document(u'%s' %(sportNames[i]))
  # Set fields using the json data corresponding to the sport name
  doc_ref.set({
  u'name': u'%s' %(sportNames[i]),
  u'nameAbr': u'%s' %(json_data[sportNames[i]]['nameAbr']),
  u'tags': u'%s' %(json_data[sportNames[i]]['newTags']),
  u'sportDescription': u'%s' %(json_data[sportNames[i]]['sportDescription'])
})

# To add another field, use this template and add it into the block above
# u'fieldName': u'%s' %(json_data[sportNames[i]]['jsonFieldReference'])
# where %s is used for string interpolation. 
# Other formatting options can be used for other data types



