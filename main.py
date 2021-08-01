
from mqtt import MQTTClient
import time
import machine
import ujson
import constants as CONST

adc = machine.ADC()
apin = adc.channel(pin='P16')


def sub_cb(topic, msg):
   print(msg)

# Inspo from Leyla's project (moist_sensor)
def moist_sensor(p_in='P15', p_out='P12'):
    adc = machine.ADC() #default 12
    apin = adc.channel(pin=p_in, attn=machine.ADC.ATTN_11DB)
    p_out = machine.Pin(p_out, mode=machine.Pin.OUT, pull=machine.Pin.PULL_DOWN)
    p_out.value(1)
    time.sleep(2)
    volts = apin.value()
    p_out.value(0)
    time.sleep(2)
    return volts
    
# MQTT Setup
client = MQTTClient(client_id,
                    CONST.UBIDOTS_MQTT_URL,
                    user=CONST.UBIDOTS_TOKEN,
                    password='',
                    port=CONST.UBIDOTS_MQTT_PORT)

client.set_callback(sub_cb)
client.connect()
print('Connected')


my_topic = CONST.UBIDOTS_MQTT_TOPIC + "My_Device"

payload = {}
toggled = False

while True:
 #  millivolts = apin.voltage()
# celsius = (millivolts - 500.0) / 10.0
   voltage = apin()*(5/4095)
   celsius = (voltage-0.5)*10
   payload['temperature'] = celsius
  # payload['humidity'] = 39.85
   payload['soil_moisture'] = moist_sensor()
    
   json_payload = ujson.dumps(payload)
   print(json_payload)

   client.publish(topic=my_topic, msg=json_payload)

   toggled = not toggled

   client.check_msg()
   time.sleep(3)