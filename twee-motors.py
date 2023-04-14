from ev3dev2.motor import OUTPUT_B, OUTPUT_C
from ev3dev2.motor import LargeMotor, MoveTank, SpeedPercent

tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

# laat de robot ter plaatse draaien
# door de motors in tegengestelde richting te laten draaien
tank_drive.on_for_seconds(SpeedPercent(50), SpeedPercent(-50), 3)
