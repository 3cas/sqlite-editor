import curses
import os
import sys
import sqlite3


curses.curs_set(0)


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


def cmenu(stdscr, options: dict):
    active = True

    while active:
        



def edit_mode(stdscr, db_path: str):
    stdscr.addstr(0, 0, "Edit Mode")

    cmenu(
        stdscr,
        (),
        {
            ""
        }
    )


def design_mode(stdscr, db_path: str):
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