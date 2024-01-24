from paho.mqtt import client as mqtt_client

broker = "192.168.86.216"
port = 1883
topic = "esp32/temperatura"

def connect_mqtt():
    client = mqtt_client.Client("PythonPub_FranOrlovic")
    client.connect(broker, port)

    return client

def run():
    client = connect_mqtt()
    client.loop_start()
    client.publish(topic, 100)
    client.loop_stop()


run()