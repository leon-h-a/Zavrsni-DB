from database.session_generator import Session


MQTT_ACTIVE_CLIENTS = [("init", 0)]


def initialisation(client, userdata, message):
    # Session.
    print(message.payload.decode('UTF-8'))


def get_active_clients():
    # todo: ovo se izvalci iz baze ovisno o tome jeli kontroler aktivan
    raise NotImplemented


def uc_state(client, userdata, message):
    raise NotImplemented
