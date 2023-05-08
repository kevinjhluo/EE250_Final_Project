import paho.mqtt.client as mqtt
from flask import Flask, render_template


app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html', message=received_message)
    

broker_address = "test.mosquitto.org"
topic = "button/morse_code"

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    global received_message
    received_message = msg.payload.decode("utf-8")
    print("Received message: " + received_message)



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(host="test.mosquitto.org", port=1883, keepalive=60)

if __name__ == '__main__':
    client.loop_start()
    app.run()

