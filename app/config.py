import os
from brachiograph import BrachioGraph

bg = BrachioGraph(
    inner_arm=os.environ.get('INNER_ARM') or 8,  # Oberarmlaenge cm
    outer_arm=os.environ.get('OUTER_ARM') or 8,  # Unterarmlaenge cm
    bounds=(-8, 4, 4, 13),                       # Koordinaten Zeichenbereich
    servo_1_degree_ms=-10,                       # Bewegung Schulterservo
    servo_2_degree_ms=10,                        # Bewegung Ellenbogenservo
    servo_1_centre=1500,                         # Mittelstellung Schulter
    servo_2_centre=1500,                         # Mittelstellung Ellenbogen
    pw_down=os.environ.get('PW_DOWN') or 1850,   # Position Stift unten
    pw_up=os.environ.get('PW_UP') or 1500,       # Position Stift angehoben
)

# Lights
PIN_LIGHT_YELLOW = 17
PIN_LIGHT_GREEN = 4

# Inputs
PIN_INPUT_A = 9
PIN_INPUT_B = 7
PIN_INPUT_C = 8
PIN_INPUT_D = 10

# Outputs
PIN_OUTPUT_A = 22
PIN_OUTPUT_B = 23
PIN_OUTPUT_C = 24
PIN_OUTPUT_D = 25

# Onboard button
PIN_BUTTON = 11

# Onboard buzzer
PIN_BUZZER = 18
