# tuto_manual.py
import os

def get_key():
    """
    Simplified key input for Colab.
    Ask the user to type LEFT, RIGHT, or ENTER (case-insensitive).
    """
    key = input("Type LEFT, RIGHT or ENTER: ").strip().upper()
    if key in ("LEFT", "RIGHT", "ENTER"):
        return key
    return "OTHER"

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
        # clear the screen (optional, just adds separation in Colab)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nManual Tutorial Mode (Colab version)\n")
        print(f"{steps[idx]}\n")
        print("Type LEFT ← | RIGHT → | ENTER to exit")

        key = get_key()
        if key == "LEFT" and idx > 0:
            idx -= 1
        elif key == "RIGHT" and idx < len(steps) - 1:
            idx += 1
        elif key == "ENTER":
            print("\nTutorial finished. 🎉")
            break
