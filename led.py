import pyfirmata
board = pyfirmata.Arduino('COM3')
pyfirmata.util.Iterator(board).start()

sensor = board.get_pin('d:7:i')
sensor.enable_reporting()
led = board.get_pin('d:8:o')

while True:
    if sensor.read():
        led.write(True)
        print("Encendido")
        print(sensor.read())
    else:
        led.write(False)
        print("Apagado")
        print(sensor.read())
