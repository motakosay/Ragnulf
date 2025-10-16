# tuto_manual.py
#in win10 Command Prompt font is MS Gothic, color opacity 75% for best appearance.
from colorama import Fore, Style, init

class ForeX:
    # Custom color
    ORANGE = '\033[38;5;208m'

init(autoreset=True)

def clear_screen():
    print("\n" * 3)

def get_key():
    key = input("Type NEXT for next, EXIT to quit, or enter a page number: ").strip().upper()
    if key == "NEXT":
        return "NEXT"
    elif key == "EXIT":
        return "EXIT"
    elif key.isdigit():
        return int(key)
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

# Axis rotation diagram
rot_x = """\
           Y
           ↑
           |
           |      ↷  (rotate cube around X-axis 90°)
           |         (↷ = clockwise)
           |
           |
           O────────────→ X
          / 
         /
         Z 
"""

# ---------- Coloring + Cube/OLL Rendering ----------
def render_cube(name="cross_corners"):
    default_color = Fore.LIGHTBLACK_EX

    cube_template = """\
                              
                              
                              
                              
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

    def apply_colors(base_str, positions):
        lines = base_str.split("\n")
        for idx, line in enumerate(lines):
            new_line = ""
            for i, ch in enumerate(line):
                if idx in positions and i in positions[idx]:
                    new_line += positions[idx][i] + ch + Style.RESET_ALL
                else:
                    new_line += default_color + ch + Style.RESET_ALL
            lines[idx] = new_line
        return "\n".join(lines)

    # ---- Cross Corners ----
    if name == "cross_corners":
        lines = cube_cross_corners.split("\n")
        colored_positions = {}
        def cmc(idx, cmap):
            colored_positions.setdefault(idx, {}).update(cmap)
        cmc(6, {20: Fore.BLUE, 21: Fore.BLUE, 22: Fore.BLUE})
        cmc(7, {18: Fore.BLUE, 19: Fore.BLUE, 20: Fore.BLUE, 21: Fore.BLUE, 22: Fore.BLUE, 23: Fore.RED})
        cmc(8, {24: Fore.RED, 23: Fore.RED, 21: Fore.WHITE, 17: Fore.WHITE})
        cmc(9, {24: Fore.RED, 23: Fore.RED, 22: Fore.RED, 21: Fore.WHITE, 20: Fore.WHITE, 19: Fore.WHITE,
                                 18: Fore.WHITE, 17: Fore.WHITE, 16: Fore.BLUE, 15: Fore.BLUE, 14: Fore.BLUE})
        cmc(10, {13: Fore.BLUE, 17: Fore.BLUE})
        cmc(11, {13: Fore.BLUE, 14: Fore.BLUE, 15: Fore.BLUE, 16: Fore.BLUE, 17: Fore.BLUE,
                                  18: Fore.YELLOW, 19: Fore.YELLOW, 20: Fore.YELLOW, 22: Fore.BLUE, 23: Fore.BLUE})
        cmc(12, {17: Fore.YELLOW, 21: Fore.YELLOW, 23: Fore.BLUE})
        cmc(13, {17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW,
                                  20: Fore.YELLOW, 21: Fore.YELLOW, 22: Fore.BLUE})
        return apply_colors("\n".join(lines), colored_positions)

    # ---- F2L ----
    if name == "F2L":
        lines = cube_f2l.split("\n")
        colored_positions = {}
        def cmc(idx, cmap):
            colored_positions.setdefault(idx, {}).update(cmap)
        cmc(2, {11: Fore.BLUE, 12: Fore.BLUE, 13: Fore.BLUE, 15: Fore.BLUE , 16: Fore.BLUE, 17: Fore.BLUE, 19:Fore.BLUE, 20:Fore.BLUE, 31:Fore.BLUE, 32:Fore.BLUE, 33:Fore.BLUE, 35:Fore.BLUE, 36:Fore.BLUE, 37:Fore.BLUE, 39:Fore.BLUE, 40:Fore.BLUE })
        cmc(3, {9: Fore.BLUE, 13: Fore.BLUE, 17: Fore.BLUE, 21: Fore.BLUE, 22: Fore.BLUE, 29:Fore.BLUE, 33:Fore.BLUE, 37:Fore.BLUE, 41:Fore.BLUE})
        cmc(4, {9: Fore.BLUE, 10: Fore.BLUE, 11:Fore.BLUE, 12:Fore.BLUE, 13: Fore.BLUE, 14:Fore.BLUE, 15: Fore.BLUE, 16: Fore.BLUE , 17: Fore.BLUE, 18: Fore.BLUE, 19: Fore.BLUE, 20: Fore.BLUE ,21: Fore.BLUE, 22: Fore.BLUE, 29:Fore.BLUE, 30:Fore.BLUE, 31:Fore.BLUE, 32:Fore.BLUE, 33:Fore.BLUE, 34:Fore.BLUE, 35:Fore.BLUE, 36:Fore.BLUE, 37:Fore.BLUE, 38:Fore.BLUE, 39:Fore.BLUE, 40:Fore.BLUE, 41:Fore.BLUE})
        cmc(5, {13: Fore.BLUE, 17:Fore.BLUE, 33:Fore.BLUE, 37:Fore.BLUE,41:Fore.BLUE})
        cmc(6, {13: Fore.BLUE, 14: Fore.BLUE, 15:Fore.BLUE, 16:Fore.BLUE ,17:Fore.BLUE, 33:Fore.BLUE, 34:Fore.BLUE, 35:Fore.BLUE, 36:Fore.BLUE, 37:Fore.BLUE,38 :Fore.BLUE, 39:Fore.BLUE, 40:Fore.BLUE, 41:Fore.BLUE})
        cmc(7, {13: Fore.BLUE, 17:Fore.BLUE})
        cmc(8, {13: Fore.BLUE, 14: Fore.BLUE, 15:Fore.BLUE, 16:Fore.BLUE ,17:Fore.BLUE})
        return apply_colors("\n".join(lines), colored_positions)

    # ---- OLL Cases ----
    positions = {}
    def cmc(idx, cmap):
        positions.setdefault(idx, {}).update(cmap)

    if name == "OLL-Line":
        cmc(5, {13: Fore.YELLOW, 14: Fore.YELLOW, 15: Fore.YELLOW, 17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW, 21: Fore.YELLOW, 22: Fore.YELLOW, 23:Fore.YELLOW})
        cmc(6, {11: Fore.YELLOW, 12: Fore.YELLOW, 13: Fore.YELLOW, 14:Fore.YELLOW ,15: Fore.YELLOW, 16: Fore.YELLOW, 17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW, 20: Fore.YELLOW, 21: Fore.YELLOW, 22: Fore.YELLOW, 23:Fore.YELLOW})
        return apply_colors(cube_template, positions)

    if name == "OLL-L_shape":
        cmc(5, {17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW, 21: Fore.YELLOW, 22: Fore.YELLOW, 23:Fore.YELLOW})
        cmc(6, {15: Fore.YELLOW, 16: Fore.YELLOW, 17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW, 20: Fore.YELLOW, 21: Fore.YELLOW, 22: Fore.YELLOW, 23:Fore.YELLOW})
        cmc(7, {14: Fore.YELLOW, 15: Fore.YELLOW, 16: Fore.YELLOW, 17: Fore.YELLOW, 18: Fore.YELLOW})
        return apply_colors(cube_template, positions)

    if name == "OLL-Dot":
        cmc(5, {17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW})
        cmc(6, {15: Fore.YELLOW, 16: Fore.YELLOW, 17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW})
        return apply_colors(cube_template, positions)

    if name == "OLL-Sune":
        cmc(4, {17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW})
        cmc(5, {13: Fore.YELLOW, 14:Fore.YELLOW, 15 :Fore.YELLOW, 16:Fore.YELLOW, 17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW, 20: Fore.YELLOW, 21:Fore.YELLOW, 22:Fore.YELLOW, 23:Fore.YELLOW})
        cmc(6, {11:Fore.YELLOW, 12:Fore.YELLOW, 13:Fore.YELLOW, 14:Fore.YELLOW, 15: Fore.YELLOW, 16: Fore.YELLOW, 17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW, 20:Fore.YELLOW, 21: Fore.YELLOW, 22: Fore.YELLOW, 23:Fore.YELLOW})
        cmc(7, {10:Fore.YELLOW , 11 : Fore.YELLOW, 12:Fore.YELLOW, 13:Fore.YELLOW, 14:Fore.YELLOW , 15: Fore.YELLOW, 16: Fore.YELLOW, 17: Fore.YELLOW, 18: Fore.YELLOW})
        cmc(8, {17: Fore.YELLOW, 21: Fore.YELLOW})
        cmc(9, {17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW, 20:Fore.YELLOW , 21: Fore.YELLOW})
        return apply_colors(cube_template, positions)

    if name == "OLL-AntiSune":
        cmc(4, {17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW})
        cmc(5, {13: Fore.YELLOW, 14:Fore.YELLOW, 15 :Fore.YELLOW, 16:Fore.YELLOW, 17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW, 20: Fore.YELLOW, 21:Fore.YELLOW, 22:Fore.YELLOW, 23:Fore.YELLOW})
        cmc(6, {11:Fore.YELLOW, 12:Fore.YELLOW, 13:Fore.YELLOW, 14:Fore.YELLOW, 15: Fore.YELLOW, 16: Fore.YELLOW, 17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW, 20:Fore.YELLOW, 21: Fore.YELLOW, 22: Fore.YELLOW, 23:Fore.YELLOW})
        cmc(7, {14:Fore.YELLOW , 15: Fore.YELLOW, 16: Fore.YELLOW, 17: Fore.YELLOW, 18: Fore.YELLOW, 19:Fore.YELLOW, 20:Fore.YELLOW, 22:Fore.YELLOW})
        cmc(8, {9: Fore.YELLOW, 13: Fore.YELLOW})
        cmc(9, {9: Fore.YELLOW, 10: Fore.YELLOW, 11:Fore.YELLOW, 12:Fore.YELLOW , 13: Fore.YELLOW})
        return apply_colors(cube_template, positions)

    if name == "OLL-H":
        cmc(4, {17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW})
        cmc(5, {13: Fore.YELLOW, 14:Fore.YELLOW, 15 :Fore.YELLOW, 16:Fore.YELLOW, 17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW, 20: Fore.YELLOW, 21:Fore.YELLOW, 22:Fore.YELLOW, 23:Fore.YELLOW})
        cmc(6, {11:Fore.YELLOW, 12:Fore.YELLOW, 13:Fore.YELLOW, 14:Fore.YELLOW, 15: Fore.YELLOW, 16: Fore.YELLOW, 17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW, 20:Fore.YELLOW, 21: Fore.YELLOW, 22: Fore.YELLOW, 23:Fore.YELLOW})
        cmc(7, {14:Fore.YELLOW , 15: Fore.YELLOW, 16: Fore.YELLOW, 17: Fore.YELLOW, 18: Fore.YELLOW})
        cmc(8, {9: Fore.YELLOW, 21:Fore.YELLOW})
        cmc(9, {9: Fore.YELLOW, 10: Fore.YELLOW, 11:Fore.YELLOW, 12:Fore.YELLOW , 18:Fore.YELLOW, 19:Fore.YELLOW, 20:Fore.YELLOW, 21:Fore.YELLOW})
        return apply_colors(cube_template, positions)

    if name == "OLL-Pi":
        cmc(4, {17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW})
        cmc(5, {13: Fore.YELLOW, 14:Fore.YELLOW, 15 :Fore.YELLOW, 16:Fore.YELLOW, 17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW, 20: Fore.YELLOW, 21:Fore.YELLOW, 22:Fore.YELLOW, 23:Fore.YELLOW,25:Fore.YELLOW})
        cmc(6, {11:Fore.YELLOW, 12:Fore.YELLOW, 13:Fore.YELLOW, 14:Fore.YELLOW, 15: Fore.YELLOW, 16: Fore.YELLOW, 17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW, 20:Fore.YELLOW, 21: Fore.YELLOW, 22: Fore.YELLOW, 23:Fore.YELLOW, 24:Fore.YELLOW, 25:Fore.YELLOW})
        cmc(7, {14:Fore.YELLOW , 15: Fore.YELLOW, 16: Fore.YELLOW, 17: Fore.YELLOW, 18: Fore.YELLOW})
        cmc(8, {9: Fore.YELLOW, 21:Fore.YELLOW})
        cmc(9, {9: Fore.YELLOW, 10: Fore.YELLOW, 11:Fore.YELLOW, 12:Fore.YELLOW , 18:Fore.YELLOW, 19:Fore.YELLOW, 20:Fore.YELLOW, 21:Fore.YELLOW})
        return apply_colors(cube_template, positions)

    if name == "OLL-L":
        cmc(4, {13:Fore.YELLOW, 14:Fore.YELLOW, 15:Fore.YELLOW, 17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW})
        cmc(5, {12:Fore.YELLOW, 13: Fore.YELLOW, 14:Fore.YELLOW, 15 :Fore.YELLOW, 16:Fore.YELLOW, 17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW, 20: Fore.YELLOW, 21:Fore.YELLOW, 22:Fore.YELLOW, 23:Fore.YELLOW,25:Fore.YELLOW})
        cmc(6, {11:Fore.YELLOW, 12:Fore.YELLOW, 13:Fore.YELLOW, 14:Fore.YELLOW, 15: Fore.YELLOW, 16: Fore.YELLOW, 17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW, 20:Fore.YELLOW, 21: Fore.YELLOW, 22: Fore.YELLOW, 23:Fore.YELLOW, 24:Fore.YELLOW, 25:Fore.YELLOW})
        cmc(7, {14:Fore.YELLOW , 15: Fore.YELLOW, 16: Fore.YELLOW, 17: Fore.YELLOW, 18: Fore.YELLOW, 19:Fore.YELLOW, 20:Fore.YELLOW, 22:Fore.YELLOW})
        cmc(8, {9: Fore.YELLOW})
        cmc(9, {9: Fore.YELLOW, 10: Fore.YELLOW, 11:Fore.YELLOW, 12:Fore.YELLOW})
        return apply_colors(cube_template, positions)

    if name == "OLL-T":
        cmc(4, {17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW, 21: Fore.YELLOW, 22: Fore.YELLOW, 23: Fore.YELLOW, 24: Fore.YELLOW})
        cmc(5, {13: Fore.YELLOW, 14:Fore.YELLOW, 15 :Fore.YELLOW, 16:Fore.YELLOW, 17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW, 20: Fore.YELLOW, 21:Fore.YELLOW, 22:Fore.YELLOW, 23:Fore.YELLOW, 24:Fore.YELLOW})
        cmc(6, {11:Fore.YELLOW, 12:Fore.YELLOW, 13:Fore.YELLOW, 14:Fore.YELLOW, 15: Fore.YELLOW, 16: Fore.YELLOW, 17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW, 20:Fore.YELLOW, 21: Fore.YELLOW, 22: Fore.YELLOW, 23:Fore.YELLOW})
        cmc(7, {14:Fore.YELLOW , 15: Fore.YELLOW, 16: Fore.YELLOW, 17: Fore.YELLOW, 18: Fore.YELLOW, 19:Fore.YELLOW, 20:Fore.YELLOW, 22:Fore.YELLOW})
        cmc(8, {9: Fore.YELLOW})
        cmc(9, {9: Fore.YELLOW, 10: Fore.YELLOW, 11:Fore.YELLOW, 12:Fore.YELLOW})
        return apply_colors(cube_template, positions)

    if name == "OLL-U":
        cmc(4, {13:Fore.YELLOW, 14:Fore.YELLOW, 15:Fore.YELLOW, 17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW, 21: Fore.YELLOW, 22: Fore.YELLOW, 23: Fore.YELLOW, 24: Fore.YELLOW})
        cmc(5, {12:Fore.YELLOW, 13: Fore.YELLOW, 14:Fore.YELLOW, 15 :Fore.YELLOW, 16:Fore.YELLOW, 17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW, 20: Fore.YELLOW, 21:Fore.YELLOW, 22:Fore.YELLOW, 23:Fore.YELLOW, 24:Fore.YELLOW})
        cmc(6, {11:Fore.YELLOW, 12:Fore.YELLOW, 13:Fore.YELLOW, 14:Fore.YELLOW, 15: Fore.YELLOW, 16: Fore.YELLOW, 17: Fore.YELLOW, 18: Fore.YELLOW, 19: Fore.YELLOW, 20:Fore.YELLOW, 21: Fore.YELLOW, 22: Fore.YELLOW, 23:Fore.YELLOW})
        cmc(7, {14:Fore.YELLOW , 15: Fore.YELLOW, 16: Fore.YELLOW, 17: Fore.YELLOW, 18: Fore.YELLOW})
        cmc(8, {9: Fore.YELLOW, 21:Fore.YELLOW})
        cmc(9, {9: Fore.YELLOW, 10: Fore.YELLOW, 11:Fore.YELLOW, 12:Fore.YELLOW, 18:Fore.YELLOW,19:Fore.YELLOW,20:Fore.YELLOW,21:Fore.YELLOW})
        return apply_colors(cube_template, positions)

    if name == "PLL-Diagonal_Swap":
        cmc(5, {17:Fore.YELLOW , 18:Fore.YELLOW, 19:Fore.YELLOW, 24:Fore.GREEN, 25:Fore.GREEN})
        cmc(6, {15:Fore.YELLOW, 16:Fore.YELLOW, 17:Fore.YELLOW, 18: Fore.YELLOW, 19:Fore.YELLOW, 24:Fore.GREEN, 25:Fore.GREEN})
        cmc(7, {11:Fore.RED, 12:Fore.RED, 13:Fore.RED, 19: ForeX.ORANGE, 20: ForeX.ORANGE, 21:Fore.BLUE, 22:Fore.BLUE, 23:Fore.BLUE, 24:Fore.GREEN})
        cmc(8, {9:Fore.RED, 13:Fore.RED, 17: ForeX.ORANGE, 21: ForeX.ORANGE, 23:ForeX.ORANGE, 24:ForeX.ORANGE})
        cmc(9, {9:Fore.RED, 10:Fore.RED, 11:Fore.RED, 12:Fore.RED, 13:Fore.RED, 14: Fore.GREEN,15: Fore.GREEN,16: Fore.GREEN, 17: ForeX.ORANGE, 18: ForeX.ORANGE, 19: ForeX.ORANGE, 20: ForeX.ORANGE, 21: ForeX.ORANGE, 22:Fore.BLUE , 23: ForeX.ORANGE})
        cmc(10, {13:Fore.GREEN, 17: Fore.GREEN, 23:ForeX.ORANGE})
        cmc(11, {13:Fore.GREEN, 14:Fore.GREEN, 15:Fore.GREEN, 16:Fore.GREEN , 17: Fore.GREEN})
        return apply_colors(cube_template, positions)

    if name == "PLL-Adjacent_Corner_Swap":
        cmc(5, {17:Fore.YELLOW , 18:Fore.YELLOW, 19:Fore.YELLOW, 24:Fore.GREEN, 25:Fore.GREEN})
        cmc(6, {15:Fore.YELLOW, 16:Fore.YELLOW, 17:Fore.YELLOW, 18: Fore.YELLOW, 19:Fore.YELLOW, 24:Fore.GREEN, 25:Fore.GREEN})
        cmc(7, {11:Fore.GREEN, 12:Fore.GREEN, 13:Fore.GREEN, 19: ForeX.ORANGE, 20: ForeX.ORANGE, 21:Fore.BLUE, 22:Fore.BLUE, 23:Fore.BLUE, 24:Fore.GREEN})
        cmc(8, {9:Fore.GREEN, 13:Fore.GREEN, 17: ForeX.ORANGE, 21: ForeX.ORANGE, 23:ForeX.ORANGE, 24:ForeX.ORANGE})
        cmc(9, {9:Fore.GREEN, 10:Fore.GREEN, 11:Fore.GREEN, 12:Fore.GREEN, 13:Fore.GREEN, 14: Fore.GREEN,15: Fore.GREEN,16: Fore.GREEN, 17: ForeX.ORANGE, 18: ForeX.ORANGE, 19: ForeX.ORANGE, 20: ForeX.ORANGE, 21: ForeX.ORANGE, 22:Fore.BLUE , 23: ForeX.ORANGE})
        cmc(10, {13:Fore.GREEN, 17: Fore.GREEN, 23:ForeX.ORANGE})
        cmc(11, {13:Fore.GREEN, 14:Fore.GREEN, 15:Fore.GREEN, 16:Fore.GREEN , 17: Fore.GREEN})
        return apply_colors(cube_template, positions)

    if name == "PLL-Edge_Cycle#1":
        cmc(5, {17:Fore.YELLOW , 18:Fore.YELLOW, 19:Fore.YELLOW})
        cmc(6, {15:Fore.YELLOW, 16:Fore.YELLOW, 17:Fore.YELLOW, 18: Fore.YELLOW, 19:Fore.YELLOW, 23:Fore.RED, 24:Fore.RED})
        cmc(7, {15:ForeX.ORANGE, 16:ForeX.ORANGE, 17:ForeX.ORANGE, 23:Fore.RED})
        cmc(8, {13:ForeX.ORANGE, 17:ForeX.ORANGE, 23:ForeX.ORANGE, 24:ForeX.ORANGE})
        cmc(9, {13:ForeX.ORANGE, 17:ForeX.ORANGE, 14:Fore.GREEN, 15:Fore.GREEN, 16:Fore.GREEN , 23: ForeX.ORANGE})
        cmc(10, {13:Fore.GREEN, 17 :Fore.GREEN, 23:ForeX.ORANGE})
        cmc(11, {13:Fore.GREEN, 14:Fore.GREEN, 15:Fore.GREEN, 16:Fore.GREEN , 17: Fore.GREEN})
        return apply_colors(cube_template, positions)

    if name == "PLL-Edge_Cycle#2":
        cmc(5, {17:Fore.YELLOW , 18:Fore.YELLOW, 19:Fore.YELLOW})
        cmc(6, {15:Fore.YELLOW, 16:Fore.YELLOW, 17:Fore.YELLOW, 18: Fore.YELLOW, 19:Fore.YELLOW, 23:Fore.GREEN, 24:Fore.GREEN})
        cmc(7, {15:Fore.RED, 16:Fore.RED, 17:Fore.RED, 23:Fore.GREEN})
        cmc(8, {13:Fore.RED, 17:Fore.RED, 23:ForeX.ORANGE, 24:ForeX.ORANGE})
        cmc(9, {13:Fore.RED, 17:Fore.RED, 14:Fore.GREEN, 15:Fore.GREEN, 16:Fore.GREEN , 23: ForeX.ORANGE})
        cmc(10, {13:Fore.GREEN, 17 :Fore.GREEN, 23:ForeX.ORANGE})
        cmc(11, {13:Fore.GREEN, 14:Fore.GREEN, 15:Fore.GREEN, 16:Fore.GREEN , 17: Fore.GREEN})
        return apply_colors(cube_template, positions)

    if name == "PLL-Opposite_Edge_Swap":
        cmc(5, {17:Fore.YELLOW , 18:Fore.YELLOW, 19:Fore.YELLOW})
        cmc(6, {15:Fore.YELLOW, 16:Fore.YELLOW, 17:Fore.YELLOW, 18: Fore.YELLOW, 19:Fore.YELLOW, 23:Fore.BLUE, 24:Fore.BLUE})
        cmc(7, {15:Fore.RED, 16:Fore.RED, 17:Fore.RED, 23:Fore.BLUE})
        cmc(8, {13:Fore.RED, 17:Fore.RED, 23:ForeX.ORANGE, 24:ForeX.ORANGE})
        cmc(9, {13:Fore.RED, 17:Fore.RED, 14:Fore.GREEN, 15:Fore.GREEN, 16:Fore.GREEN , 23: ForeX.ORANGE})
        cmc(10, {13:Fore.GREEN, 17 :Fore.GREEN, 23:ForeX.ORANGE})
        cmc(11, {13:Fore.GREEN, 14:Fore.GREEN, 15:Fore.GREEN, 16:Fore.GREEN , 17: Fore.GREEN})
        return apply_colors(cube_template, positions)

    if name == "PLL-Adjacent_Edge_Swap":
        cmc(5, {17:Fore.YELLOW , 18:Fore.YELLOW, 19:Fore.YELLOW})
        cmc(6, {15:Fore.YELLOW, 16:Fore.YELLOW, 17:Fore.YELLOW, 18: Fore.YELLOW, 19:Fore.YELLOW, 23:Fore.GREEN, 24:Fore.GREEN})
        cmc(7, {15:ForeX.ORANGE, 16:ForeX.ORANGE, 17:ForeX.ORANGE, 23:Fore.GREEN})
        cmc(8, {13:ForeX.ORANGE, 17:ForeX.ORANGE, 23:ForeX.ORANGE, 24:ForeX.ORANGE})
        cmc(9, {13:ForeX.ORANGE, 17:ForeX.ORANGE, 14:Fore.GREEN, 15:Fore.GREEN, 16:Fore.GREEN , 23: ForeX.ORANGE})
        cmc(10, {13:Fore.GREEN, 17 :Fore.GREEN, 23:ForeX.ORANGE})
        cmc(11, {13:Fore.GREEN, 14:Fore.GREEN, 15:Fore.GREEN, 16:Fore.GREEN , 17: Fore.GREEN})
        return apply_colors(cube_template, positions)

    if name == "OLL-L-rot":
        return default_color + rot_x + Style.RESET_ALL
    if name == "OLL-T-rot":
        return default_color + rot_x + Style.RESET_ALL

    return "<Unknown figure>"

# ---------- Tutorial ----------
def tuto_manual():
    steps = [
        {
            "title": "Rubik Concepts",
            "desc": [
                "corner: each corner has 3 colors.",
                "Edge: each edge has 2 colors.",
                "center: each face has one center, centers determine the color of each face.",
            ],
            "algo": None,
            "show_cube": False
        },
        {
            "title": "cross",
            "desc": [
                "Cross pieces align with the center colors.",
                "Just simple movements to do cross.",
                "In this step, you'll probably need to F2L Algorithm, follow tutorial!"
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
                "- White front: U R U' R'",
                "- White right: R U R'",
                "- White up: R U2 R' U' R U R'"
            ],
            "algo": None,
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
        },
        {
            "title": "OLL",
            "desc": ["OLL has 57 Algs, but there are 10 Algs that can solve all cases '2-Look Oll'."],
            "algo": None,
            "show_cube": False
        },
        {
            "title": "OLL - Line",
            "desc": ["1-Line: make sure line is horizontal"],
            "algo": "F R U R' U' F'",
            "show_cube": "OLL-Line"
        },
        {
            "title": "OLL - L shape",
            "desc": ["2-L shape: hold cube like in figure"],
            "algo": "f R U R' U' f'  'f = Double Layer' ",
            "show_cube": ["OLL-L_shape"]
        },
        {
            "title": "OLL - Dot",
            "desc": ["3-Dot: only yellow center"],
            "algo": "F R U R' U' F' (f R U R' U' f')  'in bracket to solve L shape.' ",
            "show_cube": "OLL-Dot"
        },
        {
            "title": "OLL - Sune",
            "desc": ["4-Sune: hold cube as in figure"],
            "algo": "R U R' U R U2 R'",
            "show_cube": "OLL-Sune"
        },
        {
            "title": "OLL - AntiSune",
            "desc": ["5-Anti-Sune: hold cube as in figure"],
            "algo": "L' U' L U' L' U2 L",
            "show_cube": "OLL-AntiSune"
        },
        {
            "title": "OLL - H",
            "desc": ["6-H: front face like back face"],
            "algo": "F (R U R' U')3 F'",
            "show_cube": "OLL-H"
        },
        {
            "title": "OLL - Pi",
            "desc": ["7-Pi: look like 'H 'previous Alg'' but right face like left face, in back no yellow"],
            "algo": "R U2' R2' U' R2 U' R2' U2' R",
            "show_cube": "OLL-Pi"
        },
        {
            "title": "OLL - L (2 corners)",
            "desc": ["8-L: two corners already done 'diagonal from each other' be white is your face then apply Alg."],
            "algo": "R' U R D' R' U' R D",
            "show_cube": ["OLL-L", "OLL-L-rot"]
        },
        {
            "title": "OLL - T",
            "desc": ["9-T: in figure in front there is Yellow in left upper corner and in back there is Yellow in right upper corner 'hold cube like in figuare' and rotate to make white is face"],
            "algo": "L U R' U' L' U R U'",
            "show_cube": ["OLL-T", "OLL-T-rot"]
        },
        {
            "title": "OLL - U",
            "desc": ["10-U: hold the cube like figure and apply algorithm"],
            "algo": "R2 D R' U2 R D' R' U2 R'",
            "show_cube": "OLL-U"
        },
        {
            "title": "PLL",
            "desc": ["You have solved Yellow face, congrates! in demonstration for PLL I just paint Yellow center, but you know the whole face get solved!"],
            "algo": None,
            "show_cube": None
        },
        {
            "title":"",
            "desc": ["we 'll study 2-Look PLL (6 Algorithms), PLL has 21 Algs"],
            "algo": None,
            "show_cube": None
        },
        {
            "title":"All Different = Diagonal Swap",
            "desc": ["look at pairs of corner stickers on each side. i.e.front face has red corner and orange corner 'different colors', right face has blue and green 'two different colors' and so on."],
            "algo": "F R U' R U' R U R' F' R U R' U' R' F R F'",
            "show_cube": "PLL-Diagonal_Swap"
        },
        {
            "title":"Adjacent Corner Swap",
            "desc": ["two corners need to be swapped, corner orange and blue need swap with corner green and orange , hold cube like in figure and apply Alg."],
            "algo": "R U R' U' R' F R2 U' R' U' R U R' F'",
            "show_cube": "PLL-Adjacent_Corner_Swap"
        },
        {
            "title":"corners solved!",
            "desc": ["the next step is to solve edges."],
            "algo": None,
            "show_cube": None
        },
        {
            "title":"Edge Cycle #1",
            "desc": ["one of the edges is already solved, if that case make it in back face, now there are 2 possible cases for what to do next. how to tell the difference? which side of these two sides 'Right, Lefft' has the piece that need to move to opposite side? if right want to go left like red piece want to go left apply Following Alg."],
            "algo": "R U' R U R U R U' R' U' R2",
            "show_cube": "PLL-Edge_Cycle#1"
        },
        {
            "title":"Edge Cycle #2",
            "desc": ["this is second case, the piece is in left side need to go to Right side, so apply Following Alg."],
            "algo": "L' U L' U' L' U' L' U L U L2'",
            "show_cube": "PLL-Edge_Cycle#2"
        },
        {
            "title":"Opposite Edge Swap",
            "desc": ["the front need swap with back, right need swap with left, so apply Following Alg."],
            "algo": "M2 U' M2 U2 M2 U' M2   'M is rotate middle layer.' ",
            "show_cube": "PLL-Opposite_Edge_Swap"
        },
        {
            "title":"Adjacent Edge Swap",
            "desc": ["the piece on front face need to swap with right face, the piece in back want to swap with left face, so apply Following Alg."],
            "algo": "M' U' M2 U' M2 U' M' U2 M2      'M is rotate middle layer.' ",
            "show_cube": "PLL-Adjacent_Edge_Swap"
        },
    ]

    idx = 0
    while idx < len(steps):
        step = steps[idx]
        clear_screen()
        print(Fore.CYAN + f"Page {idx+1}: {step['title']}" + Style.RESET_ALL)
        for line in step["desc"]:
            print("  " + line)
        if step["algo"]:
            print(Fore.GREEN + "Algorithm: " + Style.RESET_ALL + step["algo"])
        if step["show_cube"]:
            if isinstance(step["show_cube"], list):
                for fig in step["show_cube"]:
                    print("\n" + render_cube(fig))
            else:
                print("\n" + render_cube(step["show_cube"]))

        key = get_key()
        if key == "NEXT":
            if idx < len(steps) - 1:
                idx += 1
            else:
                print("\nTutorial completed!")
                break
        elif key == "EXIT":
            print("\nTutorial exited.")
            break
        elif isinstance(key, int):
            if 1 <= key <= len(steps):
                idx = key - 1
            else:
                print(f"Invalid page number. Enter a number between 1 and {len(steps)}.")
        else:
            print("Invalid input. Type NEXT, EXIT, or a page number.")
