import paho.mqtt.client as mqtt_client

broker= "192.168.86.216"
port = 1883
topic = "esp32/temperatura"

def on_message(client, userdata, msg):
    print(str(msg.payload))

def connect_mqtt():
    client = mqtt_client.Client("PythonSub_FranOrlovic")
    client.connect(broker, port)
    client.on_message= on_message
    return client

def run():
    client = connect_mqtt()
    client.subscribe(topic)
    client.loop_forever()

run()