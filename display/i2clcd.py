#! /usr/bin/env python3
from rpi_lcd import LCD
import os
import sys

display_height = 2
display_width  = 16
fifo_path      = "/home/pi/display"
verbose        = False

# lines: two lines separated by \n
def print_screen(lcd: LCD, lines_str: str):
    lines = lines_str.splitlines()

    if len(lines) > display_height and verbose:
        print("Input is {} lines long. Display can only show {} lines.".format(len(lines_str), display_height))

    for line in lines[:display_height]:
        if len(line) > display_width and verbose:
            print("Line is {} characters long. Display can only show {} characters.".format(len(line), display_width))

    # Need to manually truncate the line because the display behaves strangely
    # otherwise, if the line is too long.
    for index, line in enumerate(lines):
        if index > display_height:
            break

        lcd.text(lines[index][:display_width], index + 1)



def main():
    lcd = LCD()

    if not os.path.exists(fifo_path):
        print("Pipe doesn't exist, trying to create it at {}".format(fifo_path), file=sys.stderr)
        print("If it doesn't work, do it yourself:", file=sys.stderr)
        print("sudo mkfifo {}".format(fifo_path), file=sys.stderr)
        print("sudo chown pi {}".format(fifo_path), file=sys.stderr)
        os.mkfifo(fifo_path)

    while True:
        if verbose:
            print("Opening fifo at {}".format(fifo_path))

        with open(fifo_path) as fifo:
            #lcd.clear()
            input_str = fifo.read()
            print_screen(lcd, input_str)

if __name__ == "__main__":
    main()
