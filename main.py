OLED.init(128, 64)
ESP8266_IoT.init_wifi(SerialPin.P8, SerialPin.P12, BaudRate.BAUD_RATE115200)
ESP8266_IoT.connect_wifi("your_ssid", "your_pwd")

def on_forever():
    OLED.write_string("Dust ug/m3: ")
    OLED.write_num(Environment.read_dust(DigitalPin.P16, AnalogPin.P1))
    OLED.new_line()
    OLED.write_string("Temperatura C: ")
    OLED.write_num(Environment.octopus_BME280(Environment.BME280_state.BME280_TEMPERATURE_C))
    OLED.new_line()
    OLED.write_string("Humitat 0-100: ")
    OLED.write_num(Environment.octopus_BME280(Environment.BME280_state.BME280_HUMIDITY))
    OLED.new_line()
    OLED.write_string("Pressió hPa: ")
    OLED.write_num(Environment.octopus_BME280(Environment.BME280_state.BME280_PRESSURE))
    OLED.new_line()
    OLED.write_string("Altitud (msnm): ")
    OLED.write_num(Environment.octopus_BME280(Environment.BME280_state.BME280_ALTITUDE))
    OLED.new_line()
    if ESP8266_IoT.wifi_state(True):
        basic.show_string("WiFi OK!")
        ESP8266_IoT.connect_thing_speak()
        ESP8266_IoT.set_data("your_write_api_key",
            Environment.read_dust(DigitalPin.P16, AnalogPin.P1),
            Environment.octopus_BME280(Environment.BME280_state.BME280_TEMPERATURE_C),
            Environment.octopus_BME280(Environment.BME280_state.BME280_HUMIDITY),
            Environment.octopus_BME280(Environment.BME280_state.BME280_PRESSURE),
            Environment.octopus_BME280(Environment.BME280_state.BME280_ALTITUDE))
        ESP8266_IoT.upload_data()
        if ESP8266_IoT.thing_speak_state(True):
            OLED.write_string("ThingSpeak Link OK!")
            OLED.new_line()
    basic.pause(30000)
basic.forever(on_forever)
