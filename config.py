import paho.mqtt.client as mqtt
import json

# For production (Unix)
with open('/etc/webserveri/zavrsni/config.json') as config_file:
    config = json.load(config_file)

client = mqtt.Client()


class Config:
    PSQL_HOST = config.get("PSQL_HOST")
    PSQL_PORT = config.get("PSQL_PORT")
    PSQL_USER = config.get("PSQL_USER")
    PSQL_PASSWORD = config.get("PSQL_PASS")
    PSQL_DATABASE = config.get("PSQL_DATABASE")
