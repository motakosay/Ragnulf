# tuto_manual.py
from colorama import Fore, Style, init
init(autoreset=True)

def clear_screen():
    print("\n" * 3)

def get_key():
    key = input("Type NEXT for NEXT or EXIT to quit: ").strip().upper()
    if key == "NEXT":
        return "NEXT"
    elif key == "EXIT":
        return "EXIT"
    return "OTHER"

# ---------- ASCII CUBE SHAPES ----------
cube_cross_corners = """\
                              
                              
                              
                              
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

cube_f2l = """\
                                            
                                            
           ___ ___ __          ___ ___ __   
         |   |   |   |       |   |   |   |  
         |___|___|___|       |___|___|___|  
         |   |   |   | ----> |   |   |   |  
         |___|___|___|       |___|___|___|  
         |   |   |   |       |   |   |   |  
         |___|___|___|       |___|___|___|  
                                            
                                            
"""

# ---------- Coloring function ----------
def render_cube(name="cross_corners"):
    if name == "cross_corners":
        lines = cube_cross_corners.split("\n")
        colored_positions = {}

        def color_multiple_chars(line_idx, char_color_map):
            if line_idx not in colored_positions:
                colored_positions[line_idx] = {}
            colored_positions[line_idx].update(char_color_map)

        # Example coloring for cross_corners
        color_multiple_chars(6, {20: Fore.BLUE, 21: Fore.BLUE, 22: Fore.BLUE})
        color_multiple_chars(7, {18: Fore.BLUE, 19: Fore.BLUE, 20: Fore.BLUE, 21: Fore.BLUE, 22: Fore.BLUE, 23: Fore.RED})
        color_multiple_chars(8, {24: Fore.RED, 23: Fore.RED, 21: Fore.WHITE, 17: Fore.WHITE})
        color_multiple_chars(9, {24: Fore.RED, 23: Fore.RED, 22: Fore.RED, 21: Fore.WHITE, 20: Fore.WHITE, 19: Fore.WHITE,
                                 18: Fore.WHITE, 17: Fore.WHITE, 16: Fore.BLUE, 15: Fore.BLUE, 14: Fore.BLUE})
        color_multiple_chars(10, {13: Fore.BLUE, 17: Fore.BLUE})
        color_multiple_chars(11, {13: Fore.BLUE, 14: Fore.BLUE, 15: Fore.BLUE, 16: Fore.BLUE, 17: Fore.BLUE,
                                  18: Fore.YELLOW, 19: Fore.YELLOW, 20: Fore.YELLOW, 22: Fore.BLUE, 23: Fore.BLUE})
        color_multiple_chars(12, {17: Fore.YELLOW, 21: Fore.YELLOW, 23: Fore.BLUE})
        color_multiple_chars(13, {17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW,
                                  20: Fore.YELLOW, 21: Fore.YELLOW, 22: Fore.BLUE})

        default_color = Fore.LIGHTBLACK_EX
        for idx, line in enumerate(lines):
            new_line = ""
            for i, ch in enumerate(line):
                if idx in colored_positions and i in colored_positions[idx]:
                    new_line += colored_positions[idx][i] + ch + Style.RESET_ALL
                else:
                    new_line += default_color + ch + Style.RESET_ALL
            lines[idx] = new_line
        return "\n".join(lines)

    elif name == "F2L":
        lines = cube_f2l.split("\n")
        colored_positions = {}

        def color_multiple_chars(line_idx, char_color_map):
            if line_idx not in colored_positions:
                colored_positions[line_idx] = {}
            colored_positions[line_idx].update(char_color_map)

        # Example coloring for F2L case (blue edge moving right)
        color_multiple_chars(2, {11: Fore.BLUE, 12: Fore.BLUE, 13: Fore.BLUE, 15: Fore.BLUE , 16: Fore.BLUE, 17: Fore.BLUE, 19:Fore.BLUE, 20:Fore.BLUE, 31:Fore.BLUE, 32:Fore.BLUE, 33:Fore.BLUE, 35:Fore.BLUE, 36:Fore.BLUE, 37:Fore.BLUE, 39:Fore.BLUE, 40:Fore.BLUE })
        color_multiple_chars(3, {9: Fore.BLUE, 13: Fore.BLUE, 17: Fore.BLUE, 21: Fore.BLUE, 22: Fore.BLUE, 29:Fore.BLUE, 33:Fore.BLUE, 37:Fore.BLUE, 41:Fore.BLUE})
        color_multiple_chars(4, {9: Fore.BLUE, 10: Fore.BLUE, 11:Fore.BLUE, 12:Fore.BLUE, 13: Fore.BLUE, 14:Fore.BLUE, 15: Fore.BLUE, 16: Fore.BLUE , 17: Fore.BLUE, 18: Fore.BLUE, 19: Fore.BLUE, 20: Fore.BLUE ,21: Fore.BLUE, 22: Fore.BLUE, 29:Fore.BLUE, 30:Fore.BLUE, 31:Fore.BLUE, 32:Fore.BLUE, 33:Fore.BLUE, 34:Fore.BLUE, 35:Fore.BLUE, 36:Fore.BLUE, 37:Fore.BLUE, 38:Fore.BLUE, 39:Fore.BLUE, 40:Fore.BLUE, 41:Fore.BLUE})
        color_multiple_chars(5, {13: Fore.BLUE, 17:Fore.BLUE, 33:Fore.BLUE, 37:Fore.BLUE,41:Fore.BLUE})
        color_multiple_chars(6, {13: Fore.BLUE, 14: Fore.BLUE, 15:Fore.BLUE, 16:Fore.BLUE ,17:Fore.BLUE, 33:Fore.BLUE, 34:Fore.BLUE, 35:Fore.BLUE, 36:Fore.BLUE, 37:Fore.BLUE,38 :Fore.BLUE, 39:Fore.BLUE, 40:Fore.BLUE, 41:Fore.BLUE})
        color_multiple_chars(7, {13: Fore.BLUE, 17:Fore.BLUE})
        color_multiple_chars(8, {13: Fore.BLUE, 14: Fore.BLUE, 15:Fore.BLUE, 16:Fore.BLUE ,17:Fore.BLUE})

        default_color = Fore.LIGHTBLACK_EX
        for idx, line in enumerate(lines):
            new_line = ""
            for i, ch in enumerate(line):
                if idx in colored_positions and i in colored_positions[idx]:
                    new_line += colored_positions[idx][i] + ch + Style.RESET_ALL
                else:
                    new_line += default_color + ch + Style.RESET_ALL
            lines[idx] = new_line
        return "\n".join(lines)

    return ""


# ---------- Tutorial ----------
def tuto_manual():
    steps = [
        {
            "title": "cross",
            "desc": [
                "Cross pieces align with the center colors.",
                "Just simple movements to do cross."
            ],
            "algo": None,
            "show_cube": False
        },
        {
            "title": "cross_corners",
            "desc": [
                "Find corners that have white on one face.",
                "Put the corner above its correct position (corner colors same as centers).",
                "Place the corner into the position shown in the figure.",
                "There are 3 cases:",
                "- White front: R U R' U'",
                "- White right: R U R'",
                "- White up: R U2 R' U' R U R'"
            ],
            "algo": "Final Alg: R U R' U'",
            "show_cube": "cross_corners"
        },
        {
            "title": "F2L",
            "desc": [
                "Now you built the first layer.",
                "You want finish the second layer.",
                "See edge that has 2 colors of 2 centers.",
                "in figure",
                "You 'll see when use Alg 'to right' edge move from bottom to right.",
                "Next, You 'll search for edge to move to left."
            ],
            "algo": "To Right: D' R' D R D F D' F'\nTo Left: D L D' L' D' F' D F",
            "show_cube": "F2L"
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
            print(f"\nAlgorithm:\n{Fore.CYAN}{step['algo']}{Style.RESET_ALL}")
        if step["show_cube"]:
            print("\n" + render_cube(step["show_cube"]))
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
