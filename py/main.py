import mqtt_helper
import ibquery

ib = ibquery.InfoBeamerQuery()
s = ib.node('root').io(raw=True)
asset_name= s.readline()
print(asset_name) # this should read the value sent in client_write above
print(mqtt_helper.send_data_to_adafruit_io('current-asset-name', str(asset_name)))

