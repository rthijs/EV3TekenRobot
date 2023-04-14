from ev3dev2.motor import OUTPUT_B
from ev3dev2.motor import LargeMotor, SpeedPercent

motor_links = LargeMotor(OUTPUT_B)
motor_links.on_for_rotations(SpeedPercent(75), 5)