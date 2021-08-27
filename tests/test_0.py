import curses
def main(stdscr):
    stdscr.keypad(True)
    while 1:
        Key = stdscr.getkey()
        if Key == 'q':
            break
curses.wrapper(main)
