from kafka import KafkaConsumer
import csv

# Create a Kafka consumer
consumer = KafkaConsumer(
    "project3",  
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: x.decode('utf-8'),  # 
    auto_offset_reset='earliest',  # This makes the consumer start at the beginning of the topic
)

# Opening the CSV file in write mode
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Consume messages from the topic
    for message in consumer:
        # The message value is a CSV string, so we need to convert it to a list of rows
        rows = csv.reader(message.value.splitlines())

        # Write each row to the CSV file
        for row in rows:
            writer.writerow(row)
