from os import environ
from brachiograph import BrachioGraph

bg = BrachioGraph(
    inner_arm=os.environ.get('ARM_INNER') or 8,  # Upper arm length cm
    outer_arm=os.environ.get('ARM_OUTER') or 8,  # Underarm length cm
    bounds=(-8, 4, 4, 13),                       # Coordinates drawing area
    servo_1_degree_ms=-10,                       # Movement shoulder servo
    servo_2_degree_ms=10,                        # Movement elbow servo
    servo_1_centre=1500,                         # Middle position shoulder
    servo_2_centre=1500,                         # Middle position elbow
    pw_down=os.environ.get('PW_DOWN') or 1850,   # Position pin bottom
    pw_up=os.environ.get('PW_UP') or 1500,       # Position pin lifted
)

# Lights
PIN_LIGHT_GREEN = os.environ.get('PIN_LIGHT_GREEN') or 4
PIN_LIGHT_YELLOW = os.environ.get('PIN_LIGHT_YELLOW') or 17
PIN_LIGHT_RED = os.environ.get('PIN_LIGHT_RED') or 21  # 27

# Inputs
PIN_INPUT_A = os.environ.get('PIN_INPUT_A') or 9
PIN_INPUT_B = os.environ.get('PIN_INPUT_B') or 7
PIN_INPUT_C = os.environ.get('PIN_INPUT_C') or 8
PIN_INPUT_D = os.environ.get('PIN_INPUT_D') or 10

# Outputs
PIN_OUTPUT_A = os.environ.get('PIN_OUTPUT_A') or 22
PIN_OUTPUT_B = os.environ.get('PIN_OUTPUT_B') or 23
PIN_OUTPUT_C = os.environ.get('PIN_OUTPUT_C') or 24
PIN_OUTPUT_D = os.environ.get('PIN_OUTPUT_D') or 25

# Onboard button
PIN_BUTTON = os.environ.get('PIN_BUTTON') or 11

# Onboard buzzer
PIN_BUZZER = os.environ.get('PIN_BUZZER') or 18
