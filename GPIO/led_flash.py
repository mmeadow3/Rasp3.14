import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Log a message
logging.info("This is a log message.")

from gpiozero import LED
import time
led = LED(17); #this is the GPIO pin I have it set to 


# Using a for loop
for i in range(1, 11):  # Counts from 1 to 10
    print(i);
    led.on();
    time.sleep(0.5);
    led.off();
    time.sleep(0.5);
