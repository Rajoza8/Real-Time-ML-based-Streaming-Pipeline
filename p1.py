import csv
import json
import requests
from kafka import KafkaProducer

url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "aapl",
    "outputsize": "full",
    "datatype": "csv",
}

headers = {
    "content-type": "application/octet-stream",
    "X-RapidAPI-Key": "c292620961msh5c9150db0763cf2p184118jsn618fcd82d4a4",
    "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com",
}

response = requests.get(url, headers=headers, params=querystring)

# Creating a Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: x.encode('utf-8') 
)

# Sending the data to the Kafka topic
producer.send("project3", response.text)  


# Flush and close the producer
producer.flush()
producer.close()
