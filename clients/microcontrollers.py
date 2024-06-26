from database.session_generator import session_scope
from models.microcontrollers import Microcontroller, Pin
from sqlalchemy.orm import exc
import json

MQTT_ACTIVE_CLIENTS = [("init", 0), ("command_confirm", 0)]

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


def initialisation(client, userdata, msg):
    with session_scope() as s:
        try:
            duplicate = s.query(Microcontroller).filter_by(mac_address=msg.payload.decode('UTF-8')).one()
            if duplicate:
                print("Microcontroller " + msg.payload.decode('UTF-8') + " already in database")
        except exc.NoResultFound:
            new_uC = Microcontroller(mac_address=msg.payload.decode('UTF-8'), controller_name=None, active=False)
            new_uC.pins = default_pins
            s.add(new_uC)
            s.commit()
            print("Added new microcontroller: " + msg.payload.decode('UTF-8'))


def command_confirm(client, userdata, msg):
    json_obj = json.loads(msg.payload.decode('UTF-8'))
    changed_pin = list(json_obj.keys())[1]
    with session_scope() as s:
        microcontroller = s.query(Microcontroller).filter_by(mac_address="esp8266-80:7d:3a:7d:59:52").one()
        for pin in microcontroller.pins:
            if pin.embeded_pin_name == changed_pin:
                pin.current_value = json_obj[changed_pin]
                s.add(pin)
                s.commit()
