from config import client
from session_generator import Session
# from topics.uC_init import uc_initialisation

# todo: add timestamps in embedded


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # client.subscribe("$SYS/#")


def on_message(client, userdata, msg):
    print(msg.payload)


def uc_initialisation(mosq, obj, msg):
    print("MESSAGES: " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


client.on_connect = on_connect
client.message_callback_add("init", uc_initialisation)
client.on_message = on_message

client.connect("172.105.76.166", 1883, 60)

MQTT_TOPIC = [("init", 0), ("a", 0)]

client.subscribe(MQTT_TOPIC)
client.loop_forever()

# if __name__ == '__main__':
    # client.loop_forever()
