# tuto_manual.py
from colorama import Fore, Style, init
init(autoreset=True)

# ⚙️ Choose theme manually: "dark" (black background) or "light" (white background)
theme = "dark"   # change to "light" if your terminal background is white

def clear_screen():
    print("\n" * 3)

def get_key():
    key = input("Type NEXT for NEXT or EXIT to quit: ").strip().upper()
    if key == "NEXT":
        return "NEXT"
    elif key == "EXIT":
        return "EXIT"
    return "OTHER"

# Cube ASCII art (structure)
cube_str = """\
                              
                              
                              
                              
             ___ ___ ____      
            /___/___/___/|     
           /___/___/___/||     
          /___/___/__ /|/|     
         |   |   |   | /||     
         |___|___|___|/|/|     
         |   |   |   | /||     
         |___|___|___|/|/      
         |   |   |   | /       
         |___|___|___|/        
                              
                              
                              
                              
"""

def render_cube():
    # Theme-dependent colors
    if theme == "dark":
        line_color = Fore.LIGHTBLACK_EX   # cube lines = gray
        white_color = Fore.WHITE         # stickers = white
    else:  # light background
        line_color = Fore.BLACK          # cube lines = black
        white_color = Fore.LIGHTBLACK_EX # stickers = gray

    lines = cube_str.split("\n")
    colored_positions = {}

    def color_multiple_chars(line_idx, char_color_map):
        if line_idx not in colored_positions:
            colored_positions[line_idx] = {}
        colored_positions[line_idx].update(char_color_map)

    # 🎨 Example coloring for cross_corners
    color_multiple_chars(6, {20: Fore.BLUE, 21: Fore.BLUE, 22: Fore.BLUE})
    color_multiple_chars(7, {18: Fore.BLUE, 19: Fore.BLUE, 20: Fore.BLUE, 21: Fore.BLUE, 22: Fore.BLUE, 23: Fore.RED})
    color_multiple_chars(8, {24: Fore.RED, 23: Fore.RED, 21: white_color, 17: white_color})
    color_multiple_chars(9, {24: Fore.RED, 23: Fore.RED, 22: Fore.RED, 
                             21: white_color, 20: white_color, 19: white_color,
                             18: white_color, 17: white_color,
                             16: Fore.BLUE, 15: Fore.BLUE, 14: Fore.BLUE})
    color_multiple_chars(10, {13: Fore.BLUE, 17: Fore.BLUE})
    color_multiple_chars(11, {13: Fore.BLUE, 14: Fore.BLUE, 15: Fore.BLUE, 16: Fore.BLUE, 17: Fore.BLUE,
                              18: Fore.YELLOW, 19: Fore.YELLOW, 20: Fore.YELLOW,
                              22: Fore.BLUE, 23: Fore.BLUE})
    color_multiple_chars(12, {17: Fore.YELLOW, 21: Fore.YELLOW, 23: Fore.BLUE})
    color_multiple_chars(13, {17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW,
                              20: Fore.YELLOW, 21: Fore.YELLOW, 22: Fore.BLUE})

    # Apply default line color
    for idx, line in enumerate(lines):
        new_line = ""
        for i, ch in enumerate(line):
            if idx in colored_positions and i in colored_positions[idx]:
                new_line += colored_positions[idx][i] + ch + Style.RESET_ALL
            else:
                new_line += line_color + ch + Style.RESET_ALL
        lines[idx] = new_line

    return "\n".join(lines)

def tuto_manual():
    steps = [
        {
            "title": "cross",
            "desc": [
                "Cross pieces align with the center colors",
                "Just simple movements to do cross"
            ],
            "algo": None,
            "show_cube": False
        },
        {
            "title": "cross_corners",
            "desc": [
                "Find corners that have white on one face.",
                "Put the corner above its correct position (corner colors same as centers).",
                "Place the corner to move into the position shown in the figure.",
                "There are 3 cases:",
                "- White front: R U R' U'",
                "- White right: R U R'",
                "- White up: R U2 R' U' R U R'"
            ],
            "algo": "Final Alg: R U R' U'",
            "show_cube": True
        }
    ]

    idx = 0
    while True:
        clear_screen()

        step = steps[idx]
        print(f"{step['title']}\n")
        for line in step["desc"]:
            print(f"- {line}")
        if step["algo"]:
            print(f"\nAlgorithm: {Fore.CYAN}{step['algo']}{Style.RESET_ALL}")

        if step["show_cube"]:
            print("\n" + render_cube())

        print("\nType NEXT → for NEXT | EXIT to quit")

        key = get_key()
        if key == "NEXT":
            if idx < len(steps) - 1:
                idx += 1
            else:
                print("\nTutorial finished. 🎉")
                break
        elif key == "EXIT":
            print("\nTutorial finished. 🎉")
            break
