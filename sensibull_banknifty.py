import requests
import pytz
from pymongo import MongoClient, ASCENDING
from datetime import datetime

def save_data_to_collection(data):
    client = MongoClient('localhost', 27017)
    db = client.sensibull
    collection = db['banknifty']
    collection.create_index([
        ('timestamp', ASCENDING),],
        unique=True)
    ist = pytz.timezone('Asia/Kolkata')
    time = datetime.now(ist)
    document = {
        "timestamp": time,
        "data": data
    }
    result = collection.insert(document)

url = "https://strategy.sensibull.com/api/v1/optionchain/BANKNIFTY"
r = requests.get(url)
data = r.json().get('data')
save_data_to_collection(data)



