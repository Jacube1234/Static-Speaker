import time
import board
import digitalio
from rda5807 import RDA5807

# --- 1. Hardware Pin Setup ---
# Bluetooth Mute control connected to XIAO pin A3 (P29)
bt_mute = digitalio.DigitalInOut(board.A3)
bt_mute.direction = digitalio.Direction.OUTPUT

# Mode toggle button connected to SW1 (XIAO pin D8)
mode_button = digitalio.DigitalInOut(board.D8)
mode_button.direction = digitalio.Direction.IN
mode_button.pull = digitalio.Pull.UP

# --- 2. Initialize FM Radio ---
print("Initializing FM Radio chip...")
radio = RDA5807()
radio.set_volume(10)  # Volume scale: 0 to 15

# --- 3. Startup State ---
# Start in Bluetooth mode by default
bluetooth_mode = True
bt_mute.value = False  # False / LOW enables the M18 Bluetooth module audio

print("System Ready!")
print(" -> Current Mode: Bluetooth (Pair your phone to 'M18' or 'BT5.0')")
print(" -> Press the push button (SW1) to switch to FM Radio.")

last_button_state = mode_button.value

while True:
    current_button_state = mode_button.value
    
    # Detect button press (falling edge because of pull-up resistor)
    if last_button_state and not current_button_state:
        bluetooth_mode = not bluetooth_mode
        
        if bluetooth_mode:
            print("\n[Mode Switched] -> Bluetooth Active")
            bt_mute.value = False  # Unmute Bluetooth audio
        else:
            print("\n[Mode Switched] -> FM Radio Active")
            bt_mute.value = True   # Mute Bluetooth audio so it doesn't overlap
            radio.tune(92.1)       # Tune to your local station (change 99.5 as needed)
            
        # Short debounce delay
        time.sleep(0.3)
        
    last_button_state = current_button_state
    time.sleep(0.05)