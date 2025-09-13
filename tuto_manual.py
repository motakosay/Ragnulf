# tuto_manual.py
import os
from utils_input import get_key

INSTRUCTIONS = [
    "Hold the cube with the white face on the bottom and the blue face in front.",
    "Build the white cross by aligning the white edge pieces with the centers.",
    "Insert the white corner pieces to complete the first layer.",
    "Solve the middle layer by inserting the edge pieces.",
    "Orient the last layer (OLL) so the top face is all yellow.",
    "Permute the last layer (PLL) to finish the cube.",
    "Congratulations! Your cube is solved!"
]

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def tuto_manual():
    """
    Interactive manual tutorial with navigation:
    → or Enter = next step
    ← = previous step
    q = quit
    """
    idx = 0
    while 0 <= idx < len(INSTRUCTIONS):
        clear_screen()
        step_text = INSTRUCTIONS[idx]
        print("Manual Tutorial (Step-by-Step)")
        print("→ or Enter = next, ← = previous, q = quit\n")
        print(f"[ Step {idx+1}/{len(INSTRUCTIONS)} ]\n{step_text}")

        key = get_key()

        if key in ("RIGHT", "ENTER"):
            idx += 1
        elif key == "LEFT":
            idx = max(0, idx - 1)
        elif key.lower() == "q":
            clear_screen()
            print("Tutorial exited by user.")
            break
