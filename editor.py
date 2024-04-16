import curses
import os
import sys
import sqlite3


def main():
    if len(sys.argv) > 2:
        print("Too many arguments provided! Use: editor.py [database_file]")
        return
    
    elif len(sys.argv) == 2:
        db_path = sys.argv[1]

    else:
        db_path = input("Path to database: ")

    if not os.path.isfile(db_path):
        cont = input("That file does not exist yet. Create it and enter design mode? [y/N]").lower()
        if cont == "y":
            curses.wrapper(design_mode, db_path)

        else:
            print("Goodbye")

    else:
        curses.wrapper(edit_mode, db_path)


def cmenu(stdscr, coords: tuple, options: tuple, values: tuple):
    y, x = coords

    max_len = max([len(opt) for opt in options]) + 3
    opt_count = len(options)

    active = True
    selected = 0

    while active:
        offset = 0

        for option in options:
            if selected == options.index(option):
                prefix = " > "
                style = curses.A_REVERSE
            else:
                prefix = "   "
                style = curses.A_NORMAL

            ay = y + offset

            stdscr.addstr(ay, x, " "*max_len)
            stdscr.addstr(ay, x, prefix+option, style)

        key = stdscr.getch()
        if key == "KEY_UP":
            selected += 1
        elif key == "KEY_DOWN":
            selected -= 1
        elif key == "\n":
            return values[selected]
        
        if selected >= opt_count:
            selected = 0
        elif selected < 0:
            selected = opt_count-1


def view_tables(stdscr):
    pass


def exit_program(stdscr):
    sys.exit(1)


def edit_mode(stdscr, db_path: str):
    curses.curs_set(0)

    stdscr.addstr(0, 0, "Edit Mode")

    cmenu(
        stdscr,
        (2, 0),
        ("Tables", "Exit"),
        (view_tables, exit_program)
    )(stdscr)


def design_mode(stdscr, db_path: str):
    curses.curs_set(0)

    print("This feature is incomplete. Goodbye!")


def app(stdscr):
    pass


"""
exit_msg = curses.wrapper(app)
    if exit_msg:
        print(exit_msg)

"""

if __name__ == "__main__":
    os.environ.setdefault("ESCDELAY", "25")
    main()
