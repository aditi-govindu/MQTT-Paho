# Import modules

import time
import paho.mqtt.client as paho
import random

broker = 'broker.hivemq.com'

# Function to connect to Mosquitto server, where rc = 0 indicates success 
def on_connect(client1, userdata, flags, rc):
    print('Publisher connected with result '+ str(rc))
    time.sleep(2)

# Create client
client1 = paho.Client('client-001')
print('Connecting to broker:',broker)

# Connect to broker and start publishing data
client1.connect(broker)
client1.on_connect = on_connect
client1.loop_start()

try:
    while True:
        for i in range(10,50):
        # Print temperature as a random number in range 30-100
            temp = random.randint(30, 100)
            # Publish temp to server
            print(f'Publishing  {temp}\n')
            client1.publish('Test/Temperature', str(temp))
            time.sleep(2)
except KeyboardInterrupt:
    # End infinite loop using Ctrl+C in command prompt
    client1.loop_stop()
    client1.disconnect()