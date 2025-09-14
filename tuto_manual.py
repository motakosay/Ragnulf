# tuto_manual.py
import os
import sys
import termios
import tty

def get_key():
    """Wait for a key press and return 'LEFT', 'RIGHT', 'ENTER', or 'OTHER'."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch1 = sys.stdin.read(1)
        if ch1 == "\x1b":  # Arrow keys start with ESC
            ch2 = sys.stdin.read(1)
            ch3 = sys.stdin.read(1)
            if ch3 == "D":
                return "LEFT"
            elif ch3 == "C":
                return "RIGHT"
            else:
                return "OTHER"
        elif ch1 == "\r":
            return "ENTER"
        else:
            return "OTHER"
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def tuto_manual():
    steps = [
        "Step 1: Hold the cube with the white face on the bottom and the blue face toward you.",
        "Step 2: Make the white cross on the bottom face.",
        "Step 3: Solve the white corners to finish the first layer.",
        "Step 4: Solve the middle layer edges.",
        "Step 5: Make the yellow cross on top.",
        "Step 6: Orient all yellow corners.",
        "Step 7: Permute the last layer edges.",
        "Step 8: Permute the last layer corners. Cube is solved!"
    ]

    idx = 0
    while True:
        # clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Manual Tutorial Mode (no ASCII art)\n")
        print(f"{steps[idx]}\n")
        print("← Previous | → Next | ENTER to exit")

        key = get_key()
        if key == "LEFT" and idx > 0:
            idx -= 1
        elif key == "RIGHT" and idx < len(steps) - 1:
            idx += 1
        elif key == "ENTER":
            break
