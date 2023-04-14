from ev3dev2.motor import OUTPUT_B, OUTPUT_C
from ev3dev2.motor import LargeMotor, MoveTank, SpeedPercent

tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

def draai_links():
    tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(-50), 233.5)

def rijd_10_cm():
    tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(50), 360)

def teken_vierkant():
    for i in range(4):
        rijd_10_cm()
        draai_links()

teken_vierkant()
