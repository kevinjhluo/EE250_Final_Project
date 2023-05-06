import paho.mqtt.client as mqtt
import socket

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))


if __name__ == '__main__':
    ip_address=socket.gethostbyname(socket.gethostname())
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(host="test.mosquitto.org", port=1883, keepalive=60)
    client.loop_start()


    while True:
        #replace user with your USC username in all subscriptions
        client.publish("button/morse_code")


