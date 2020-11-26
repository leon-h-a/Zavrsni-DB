import paho.mqtt.client as mqtt

client = mqtt.Client()


# todo: ovo staviti preko global varijabli
class Config:
    # psql_ip = "172.105.76.166"
    psql_ip = "localhost"
    psql_port = "1883"
    psql_user = "admin"
    psql_db_name = "zavrsni"
