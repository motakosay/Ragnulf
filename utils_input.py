import sys

if sys.platform.startswith("win"):
    import msvcrt

    def get_key():
        """Get a single key press (Windows)."""
        key = msvcrt.getch()
        if key == b'\xe0':  # special key (arrows, etc.)
            key = msvcrt.getch()
            if key == b'K':
                return "LEFT"
            elif key == b'M':
                return "RIGHT"
        elif key == b'\r':
            return "ENTER"
        return key.decode(errors="ignore")

else:
    import tty, termios

    def get_key():
        """Get a single key press (Unix)."""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            key = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        if key == "\x1b[D":  # Left arrow
            return "LEFT"
        elif key == "\x1b[C":  # Right arrow
            return "RIGHT"
        elif key == "\n" or key == "\r":
            return "ENTER"
        return key
