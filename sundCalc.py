import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
TRIG = 17
ECHO = 27
BUZZER = 22

# Set GPIO pins as output/input
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(BUZZER, GPIO.OUT)

# Function to calculate distance and speed of sound
def measure_distance():
    # Send a pulse
    GPIO.output(TRIG, GPIO.LOW)
    time.sleep(0.5)  # Wait for a while to avoid overlapping pulses
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)  # 10 microseconds pulse duration
    GPIO.output(TRIG, GPIO.LOW)
    
    # Wait for the echo to return
    while GPIO.input(ECHO) == GPIO.LOW:
        pulse_start = time.time()

    while GPIO.input(ECHO) == GPIO.HIGH:
        pulse_end = time.time()

    # Calculate the time difference between sending and receiving the pulse
    pulse_duration = pulse_end - pulse_start
    
    # Distance calculation (in cm)
    distance = pulse_duration * 17150  # 17150 is the speed of sound in cm/s
    distance = round(distance, 2)  # Round to two decimal places
    
    return distance

def play_buzzer():
    GPIO.output(BUZZER, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(BUZZER, GPIO.LOW)

# Main loop
try:
    while True:
        distance = measure_distance()
        print(f"Distance: {distance} cm")
        
        # Trigger the buzzer if distance is below a certain threshold
        if distance < 50:  # Set threshold distance (e.g., 50 cm)
            play_buzzer()
            print("Object detected, buzzer triggered!")
        
        # Wait before taking another reading
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by User")

finally:
    GPIO.cleanup()  # Clean up GPIO to reset the pins
