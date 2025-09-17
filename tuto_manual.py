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


# ------------------ Common cube renderer ------------------
def build_colored_ascii(cube_str, colored_positions):
    """Apply colors to ASCII cube based on dictionary of positions"""
    lines = cube_str.split("\n")
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


# ------------------ Cross Corners Cube ------------------
def render_cross_corners_cube():
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
    colors = {}
    def c(line, mapping): colors.setdefault(line, {}).update(mapping)

    # same coloring as your cross_corners step
    c(6, {20: Fore.BLUE, 21: Fore.BLUE, 22: Fore.BLUE})
    c(7, {18: Fore.BLUE, 19: Fore.BLUE, 20: Fore.BLUE, 21: Fore.BLUE, 22: Fore.BLUE, 23: Fore.RED})
    c(8, {24: Fore.RED, 23: Fore.RED, 21: Fore.WHITE, 17: Fore.WHITE})
    c(9, {24: Fore.RED, 23: Fore.RED, 22: Fore.RED, 21: Fore.WHITE, 20: Fore.WHITE, 
          19: Fore.WHITE, 18: Fore.WHITE, 17: Fore.WHITE, 16: Fore.BLUE, 15: Fore.BLUE, 14: Fore.BLUE})
    c(10, {13: Fore.BLUE, 17: Fore.BLUE})
    c(11, {13: Fore.BLUE, 14: Fore.BLUE, 15: Fore.BLUE, 16: Fore.BLUE, 17: Fore.BLUE,
           18: Fore.YELLOW, 19: Fore.YELLOW, 20: Fore.YELLOW, 22: Fore.BLUE, 23: Fore.BLUE})
    c(12, {17: Fore.YELLOW, 21: Fore.YELLOW, 23: Fore.BLUE})
    c(13, {17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW,
           20: Fore.YELLOW, 21: Fore.YELLOW, 22: Fore.BLUE})

    return build_colored_ascii(cube_str, colors)


# ------------------ F2L Cube ------------------
def render_f2l_cube():
    cube_str = """\
                                            
                                            
           ___ ___ __          ___ ___ __   
         |   |   |   |       |   |   |   |  
         |___|___|___|       |___|___|___|  
         |   |   |   | ----> |   |   |   |  
         |___|___|___|       |___|___|___|  
         |   |   |   |       |   |   |   |  
         |___|___|___|       |___|___|___|  
                                            
                                            
"""
    colors = {}
    def c(line, mapping): colors.setdefault(line, {}).update(mapping)

    # 🔵 Example: highlight edges moving right (adjust positions to your needs)
    c(2, {11: Fore.BLUE, 12: Fore.BLUE, 13: Fore.BLUE, 15: Fore.BLUE, 
          16: Fore.BLUE, 17: Fore.BLUE, 19: Fore.BLUE, 20: Fore.BLUE,
          31: Fore.BLUE, 32: Fore.BLUE, 33: Fore.BLUE, 35: Fore.BLUE,
          36: Fore.BLUE, 37: Fore.BLUE, 39: Fore.BLUE, 40: Fore.BLUE})
    c(3, {21: Fore.RED, 22: Fore.RED})   # red edge moving
    c(5, {37: Fore.RED, 41: Fore.RED})   # destination slot

    return build_colored_ascii(cube_str, colors)


# ------------------ Tutorial Steps ------------------
def tuto_manual():
    steps = [
        {
            "title": "cross",
            "desc": [
                "Cross pieces align with the center colors",
                "Just simple movements to do cross",
                "You'll need F2L Alg sometimes, follow the tutorial."
            ],
            "algo": None,
            "show_cube": None
        },
        {
            "title": "cross_corners",
            "desc": [
                "Find corners that have white on one face.",
                "Put the corner above its correct position (colors same as centers).",
                "There are 3 cases:",
                "White front: U R U' R'",
                "White right: R U R'",
                "White up: R U2 R' U' R U R'"
            ],
            "algo": "Final Alg: U R U' R'",
            "show_cube": "cross_corners"
        },
        {
            "title": "F2L",
            "desc": [
                "Now you build the first two layers (F2L).",
                "Look for an edge with 2 colors of two centers.",
                "In this case, the edge goes from bottom to the right slot.",
                "To right: D' R' D R D F D' F'",
                "To left: D L D' L' D' F' D F"
            ],
            "algo": "Example: D' R' D R D F D' F'",
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
            print(f"\nAlgorithm: {Fore.CYAN}{step['algo']}{Style.RESET_ALL}")

        if step["show_cube"] == "cross_corners":
            print("\n" + render_cross_corners_cube())
        elif step["show_cube"] == "F2L":
            print("\n" + render_f2l_cube())

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
