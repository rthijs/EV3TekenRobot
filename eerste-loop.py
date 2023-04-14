from ev3dev2.motor import OUTPUT_B, OUTPUT_C
from ev3dev2.motor import LargeMotor, MoveTank, SpeedPercent

tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

tank_drive.on_for_seconds(SpeedPercent(50), SpeedPercent(-50), 3)

for i in range(10):
    tank_drive.on_for_seconds(SpeedPercent(20), SpeedPercent(20), 2)
    tank_drive.on_for_seconds(SpeedPercent(20), SpeedPercent(-20), 1)