OLED.init(128, 64)
ESP8266_IoT.initWIFI(SerialPin.P8, SerialPin.P12, BaudRate.BaudRate115200)
ESP8266_IoT.connectWifi("your_ssid", "your_pwd")
basic.forever(function () {
    OLED.writeString("Pols ug/m3: ")
    OLED.writeNum(Environment.ReadDust(DigitalPin.P16, AnalogPin.P1))
    OLED.newLine()
    OLED.writeString("Temperatura C: ")
    OLED.writeNum(Environment.octopus_BME280(Environment.BME280_state.BME280_temperature_C))
    OLED.newLine()
    OLED.writeString("Humitat 0-100: ")
    OLED.writeNum(Environment.octopus_BME280(Environment.BME280_state.BME280_humidity))
    OLED.newLine()
    OLED.writeString("Pressió hPa: ")
    OLED.writeNum(Environment.octopus_BME280(Environment.BME280_state.BME280_pressure))
    OLED.newLine()
    OLED.writeString("Altitud (msnm): ")
    OLED.writeNum(Environment.octopus_BME280(Environment.BME280_state.BME280_altitude))
    OLED.newLine()
    if (ESP8266_IoT.wifiState(true)) {
        basic.showString("WiFi OK!")
        ESP8266_IoT.connectThingSpeak()
        ESP8266_IoT.setData(
        "your_write_api_key",
        Environment.ReadDust(DigitalPin.P16, AnalogPin.P1),
        Environment.octopus_BME280(Environment.BME280_state.BME280_temperature_C),
        Environment.octopus_BME280(Environment.BME280_state.BME280_humidity),
        Environment.octopus_BME280(Environment.BME280_state.BME280_pressure),
        Environment.octopus_BME280(Environment.BME280_state.BME280_altitude)
        )
        ESP8266_IoT.uploadData()
        if (ESP8266_IoT.thingSpeakState(true)) {
            OLED.writeString("ThingSpeak Link OK!")
            OLED.newLine()
        }
    }
    basic.pause(30000)
})
