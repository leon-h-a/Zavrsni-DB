from database.session_generator import session_scope
from models.microcontrollers import Microcontroller, Pin


MQTT_ACTIVE_CLIENTS = [("init", 0)]


def initialisation(client, userdata, msg):
    default_pins = [
        Pin(embeded_pin_name="PSWM1", io_type="INPUT", used_for=None, current_value=None, active=False),
        Pin(embeded_pin_name="PSWM2", io_type="INPUT", used_for=None, current_value=None, active=False),
        Pin(embeded_pin_name="PA1", io_type="INPUT", used_for=None, current_value=None, active=False),
        Pin(embeded_pin_name="PA2", io_type="INPUT", used_for=None, current_value=None, active=False),
        Pin(embeded_pin_name="PR1", io_type="OUTPUT", used_for=None, current_value=None, active=False),
        Pin(embeded_pin_name="PR2", io_type="OUTPUT", used_for=None, current_value=None, active=False),
        Pin(embeded_pin_name="PS", io_type="INPUT", used_for=None, current_value=None, active=False),
        Pin(embeded_pin_name="PPMW1", io_type="OUTPUT", used_for=None, current_value=None, active=False),
        Pin(embeded_pin_name="PPMW2", io_type="OUTPUT", used_for=None, current_value=None, active=False),
        Pin(embeded_pin_name="PP1", io_type="INPUT", used_for=None, current_value=None, active=False),
        Pin(embeded_pin_name="PP2", io_type="INPUT", used_for=None, current_value=None, active=False)
    ]
    new_uC = Microcontroller(mac_address=msg.payload.decode('UTF-8'), controller_name=None, active=False)
    new_uC.pins = default_pins
    with session_scope() as sess:
        sess.add(new_uC)
        sess.commit()
    print("Added new microcontroller: " + msg.payload.decode('UTF-8'))


def get_active_clients():
    # todo: ovo se izvalci iz baze ovisno o tome jeli kontroler aktivan
    raise NotImplemented


def uc_state(client, userdata, message):
    raise NotImplemented
