import paho.mqtt.client as mqtt

broker_address = "test.mosquitto.org"
topic = "button/morse_code"

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))

def on_message(client, userdata, msg):
    print("Received message: " + str(msg.payload.decode()))

client = mqtt.Client("pc_subscriber")
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address)

client.subscribe(topic)
client.loop_forever()