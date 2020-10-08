import os

# Lights
PIN_LIGHT_GREEN = os.environ.get('PIN_LIGHT_GREEN') or 2
PIN_LIGHT_YELLOW = os.environ.get('PIN_LIGHT_YELLOW') or 3
PIN_LIGHT_RED = os.environ.get('PIN_LIGHT_RED') or 4
PIN_LIGHT_FLASH = os.environ.get('PIN_LIGHT_FLASH') or 17

# SERVOs
PIN_SERVO_A = os.environ.get('PIN_SERVO_A') or 14
PIN_SERVO_B = os.environ.get('PIN_SERVO_B') or 15
PIN_SERVO_C = os.environ.get('PIN_SERVO_C') or 18

# Onboard button
PIN_BUTTON = os.environ.get('PIN_BUTTON') or 27
