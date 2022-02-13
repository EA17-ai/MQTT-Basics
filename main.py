import random
import time

import paho.mqtt.client as mqtt

broker = "localhost"
port = 1883


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to Broker")
    else:
        print("Not connected")


def on_publish(client, userdata, result):
    print("data published")
    pass


client1 = mqtt.Client()
client1.on_connect = on_connect
client1.connect(broker,port)
client1.on_publish = on_publish
while True:
    r=str(random.random())
    time.sleep(5)
    client1.publish("house/bulb",r)
