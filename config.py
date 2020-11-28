import paho.mqtt.client as mqtt

client = mqtt.Client()


# todo: ovo staviti preko global varijabli
class Config:
    psql_ip = "localhost"
    psql_port = "5432"
    psql_pass = "admin"
    psql_user = "postgres"
    # psql_user = "zavrsni_client"
    psql_db_name = "zavrsni-localhost"
