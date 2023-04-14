from ev3dev2.motor import OUTPUT_B, OUTPUT_C
from ev3dev2.motor import LargeMotor, SpeedPercent

motor_links = LargeMotor(OUTPUT_B)
motor_rechts = LargeMotor(OUTPUT_C)

motor_links.stop(stop_action='brake')
motor_rechts.stop(stop_action='brake')