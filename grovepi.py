import time
import grovepi

sound_sensor = 0
grovepi.pinMode(sound_sensor,"INPUT")


# The threshold to turn the led on 400.00 * 5 / 1024 = 1.95v
threshold_value = 200

while True:
    try:
        # Read the sound level
        sensor_value = grovepi.analogRead(sound_sensor)

        # If loud, illuminate LED, otherwise dim
        if sensor_value > threshold_value:
            grovepi.digitalWrite(led,1)
        else:
            grovepi.digitalWrite(led,0)

        print("sensor_value = %d" %sensor_value)
        time.sleep(.5)

    except IOError:
        print ("Error")