import paho.mqtt.client as mqtt

client = mqtt.Client()


# todo: ovo staviti preko global varijabli
class Config:
    # psql_ip = "172.105.76.166"
    psql_ip = "localhost"
    psql_port = "5432"
    # psql_user = "postgres"
    psql_pass = ""
    psql_user = "zavrsni_admin"
    # psql_user = "zavrsni_client"
    psql_db_name = "zavrsni"
