import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)#This means im using the pychical pins

#we can use "GPIO.BCM" however i only know how to use BOARD

#set all 4 GPIO pins for the motors
GPIO.setup(7,GPIO.OUT)#Set pychical pin 7 to OUTPUT
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

#pwm_frequency=60#ASK TO CHANGE
#time.sleep(10)
"""NOTE: for some reason we have to first run it at 60 hz then run it at 50 hz. Maybe it to war"""
pwm_frequency=50#ASK TO CHANGE
initial_duty_cycle=0#DONT CHANGE


pwm_pin7=GPIO.PWM(7,pwm_frequency)#WARIING the lower the frequency the faster the motor will move
pwm_pin11=GPIO.PWM(11,pwm_frequency)
pwm_pin13=GPIO.PWM(13,pwm_frequency)
pwm_pin15=GPIO.PWM(15,pwm_frequency)
#MIN 53.1hz - MAX 45hz
#KEEP TESTING
#hz 53.1 hz might be the min

#Starts duty cycle at 0% for safety for all 4 esc
pwm_pin7.start(initial_duty_cycle)
pwm_pin11.start(initial_duty_cycle)
pwm_pin13.start(initial_duty_cycle)
pwm_pin15.start(initial_duty_cycle)

print("starting  duty cycle at 4%")
time.sleep(8)#Wait 8 second
pwm_pin7.ChangeDutyCycle(4)
pwm_pin11.ChangeDutyCycle(4)
pwm_pin13.ChangeDutyCycle(4)
pwm_pin15.ChangeDutyCycle(4)

#target_duty_cycle=5.2
#pwm.ChangeDutyCycle(target_duty_cycle)#duty cycle in percentage :the lower duty cycle the less power
#5.22 min
#print(target_duty_cycle)
# Function to update drone speed based on keypress

try:
    """4.7 it will move """
    print("Press 'w' to increase speed, 's' to decrease speed, or 'q' to quit.")
    speed = 4.5
    print(f"START speed {speed}%")
    while True:
        # Your main program logic goes here
        # You can add more code to control the drone's other functions
        
        user_input = input("Enter 'w' to increase speed, 's' to decrease speed, or 'q' to quit: ")
        
        if user_input == 'w':
            # Increase speed
            speed += .05
            if speed > 10:
                speed = 10
                print(f"!! MAX SPEED {speed}% !!")
                continue
        elif user_input == 's':
            # Decrease speed
            speed -= .1
            if speed < 3.0:
                speed = 3.0
                print(f"!! MIN SPEED {speed}% !!")
                continue
        elif user_input == 'q':
            break
        else:
            print("!! INVALID INPUT !! Please enter 'w', 's', or 'q'.")

        # Set PWM duty cycle based on speed
        pwm_pin7.ChangeDutyCycle(speed)
        pwm_pin11.ChangeDutyCycle(speed)
        pwm_pin13.ChangeDutyCycle(speed)
        pwm_pin15.ChangeDutyCycle(speed)
        
        print(f"Speed (DutyCycle): {speed}%")

except KeyboardInterrupt:
    pass

#0% to slow or stop
pwm_pin7.ChangeDutyCycle(0)
pwm_pin11.ChangeDutyCycle(0)
pwm_pin13.ChangeDutyCycle(0)
pwm_pin15.ChangeDutyCycle(0)
print('STOP - Speed 0%')
    
print("END")

pwm_pin7.stop(0)
pwm_pin11.stop(0)
pwm_pin13.stop(0)
pwm_pin15.stop(0)
GPIO.cleanup()#realease resources


# TESTING
def print_cycle(target_duty_cycle):

    current_duty_cycle=target_duty_cycle
    print("DutyCycle:",current_duty_cycle)
    time.sleep(1)