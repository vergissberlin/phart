import os

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
