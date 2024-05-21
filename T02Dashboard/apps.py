from django.apps import AppConfig
from gpiozero import LED, Button  #IMPORTS FOR GPIOZERO

class T02DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'T02Dashboard'

def toggleButton(state):
# ADD THIS CODE TO YOUR DJANGO APPLICATION OUTSIDE ANY FUNCTION
    led = LED(17) #LED TO GPIO17

    # TOGGLE THE LED CONNECTED TO GPIO17
    if (state): #CURRENTLY OFF
        led.on()
    else: #CURRENTLY ON
        led.off()

