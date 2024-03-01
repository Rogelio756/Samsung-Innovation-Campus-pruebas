import RPi.GPIO as GPIO
from RPLCD import CharLCD

# Configurar pines GPIO
GPIO.setmode(GPIO.BOARD)
RS = 16
E = 20
D4 = 18
D5 = 17
D6 = 27
D7 = 22

# Inicializar objeto LCD
lcd = CharLCD(cols=16, rows=2, pin_rs=RS, pin_e=E, pins_data=[D4, D5, D6, D7])

# Limpiar pantalla
lcd.clear()

# Escribir mensaje
lcd.write_string('Hello, World!')
