from config import client
from clients.microcontrollers import initialisation
from clients.microcontrollers import MQTT_ACTIVE_CLIENTS
from models import Base
from database.session_generator import engine


""" General functions """
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# todo: add timestamps in embedded
def broker_info(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # client.subscribe("$SYS/#")


client.on_connect = broker_info
client.message_callback_add("init", initialisation)

client.connect("172.105.76.166", 1883, 60)

client.subscribe(MQTT_ACTIVE_CLIENTS)
client.loop_forever()

# if __name__ == '__main__':
# client.loop_forever()
