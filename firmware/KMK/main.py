import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306

keyboard = KMKKeyboard()

# Matrix setup
# Rows: D0, D1, D2, D3
keyboard.col_pins = (board.D10, board.D9, board.D8)
keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

# I2C setup for OLED (SDA=D4, SCL=D5)
i2c = busio.I2C(board.D5, board.D4)

# Display setup (0.91" OLED is typically 128x32)
display_driver = SSD1306(
    i2c=i2c,
    device_address=0x3C, # Default I2C address for SSD1306
    width=128,
    height=32
)

display = Display(
    display=display_driver,
    entries=[
        TextEntry(text='cherryblossom pad', x=0, y=0, y_anchor='B'),
        TextEntry(text='Layer: BASE', x=0, y=10, y_anchor='B'),
    ],
    width=128,
    height=32,
    dim_time=10,
    dim_target=0.2,
    off_time=1200,
    brightness=1,
)

keyboard.extensions.append(display)

# Keymap configuration
keyboard.keymap = [
    [
        KC.N1, KC.N2, KC.N3,
        KC.N4, KC.N5, KC.N6,
        KC.N7, KC.N8, KC.N9,
        KC.N0, KC.A,  KC.B
    ]
]

if __name__ == '__main__':
    keyboard.go()
