import paho.mqtt.client as mqtt


# This is the Subscriber
broker="localhost"
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("house/bulb")


def on_message(client, userdata, msg):

    print(msg.payload.decode('UTF-8'))



client = mqtt.Client()
client.connect("localhost", 1883)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()