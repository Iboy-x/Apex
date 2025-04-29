# Apex
# Space Sonic

> Measuring the speed of sound using Raspberry Pi, ultrasonic sensors, and custom PCB design.

## Project Idea

Apex is a hardware project built to measure the speed of sound using a Raspberry Pi Zero 2 W, an ultrasonic sensor, and a buzzer. It features a custom PCB to make the circuit compact and efficient. The idea is to calculate the speed of sound by firing ultrasonic pulses, measuring the echo time, and using simple physics formulas. It merges physics, electronics, and coding into one solid project.

## Materials Used

- Raspberry Pi Zero 2 W
- Ultrasonic Sensor (HC-SR04)
- Buzzer
- Custom PCB (designed in KiCad)
- Jumper Wires
- Power Supply (5V micro USB)
- Basic Resistors and Capacitors
  
## PCB Pictures

### schematics

https://hackclub.slack.com/files/U07U0CMNWGP/F08LVFSCQHH/image.png

## How It Works

1. The Raspberry Pi sends a 10µs pulse to the ultrasonic sensor.
2. The sensor emits an ultrasonic wave and waits for it to bounce back.
3. The time taken for the echo to return is recorded.
4. The speed of sound is calculated using the formula:

```
Speed of Sound = (2 × Distance) / Time
```

## Outcomes
-we will be able to see the trend in the variation of speed of sound as altitudes changes.

## Future Improvements
Also add a raspberry pi camera to capture beautiful pics 

## MADE by :

@iboy-x and @itzLamo  
