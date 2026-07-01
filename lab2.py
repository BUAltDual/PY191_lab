import curses

text = """Hello world!
This is a tiny text editor.
Edit me!"""

cursor = 0


def draw(screen):
    screen.clear()

    # ==========================================================
    # INITIALIZE THE DISPLAY
    #
    # Display the document with the cursor at the current
    # cursor position.
    #
    # Example
    #
    # text    = "Hello"
    # cursor  = 0
    #
    # display = "|Hello"
    #
    # ---------------- TODO ----------------

    display = text[:cursor] + "|" + text[cursor:]

    # ----------------------------------------

    for row, line in enumerate(display.split("\n")):
        screen.addstr(row, 0, line)

    screen.addstr(
        len(display.split("\n")) + 1,
        0,
        "← → Move   Type Insert   Backspace Delete   Enter New Line   Esc Quit"
    )

    screen.refresh()


def main(screen):
    global text, cursor

    while True:
        draw(screen)

        key = screen.getch()

        if key == 27:
            break

        # ==========================================================
        # LEFT ARROW
        #
        # Move the cursor one position to the left.
        #
        # Example
        #
        # Before
        # text    = "Hello"
        # cursor  = 3
        # display = "Hel|lo"
        #
        # After
        # text    = "Hello"
        # cursor  = 2
        # display = "He|llo"
        #
        # ---------------- ANSWER ----------------

        elif key == curses.KEY_LEFT:

            if cursor > 0:
                cursor -= 1

            display = text[:cursor] + "|" + text[cursor:]

        # ----------------------------------------

        # ==========================================================
        # RIGHT ARROW
        #
        # Move the cursor one position to the right.
        #
        # Example
        #
        # Before
        # text    = "Hello"
        # cursor  = 3
        # display = "Hel|lo"
        #
        # After
        # text    = "Hello"
        # cursor  = 4
        # display = "Hell|o"
        #
        # ---------------- ANSWER ----------------

        elif key == curses.KEY_RIGHT:

            cursor += 1

            display = text[:cursor] + "|" + text[cursor:]

        # ----------------------------------------

        # ==========================================================
        # BACKSPACE
        #
        # Delete the character immediately before the cursor.
        #
        # Example
        #
        # Before
        # text    = "Hello"
        # cursor  = 3
        # display = "Hel|lo"
        #
        # After
        # text    = "Helo"
        # cursor  = 2
        # display = "He|lo"
        #
        # ---------------- ANSWER ----------------

        elif key in (8, 127, curses.KEY_BACKSPACE):
            if cursor > 0:
                text = text[:cursor - 1] + text[cursor:]
                cursor -= 1

        # ----------------------------------------

        # ==========================================================
        # ENTER
        #
        # Insert a newline at the cursor.
        #
        # Example
        #
        # Before
        # text    = "Hello"
        # cursor  = 3
        # display = "Hel|lo"
        #
        # After
        # text    = "Hel\nlo"
        # cursor  = 4
        # display = "Hel\n|lo"
        #
        # ---------------- ANSWER ----------------

        elif key == 10:

            text = text[:cursor] + "\n" + text[cursor:]

            cursor += 1

        # ----------------------------------------

        # ==========================================================
        # INSERT CHARACTER
        #
        # Insert the typed character at the cursor.
        #
        # Example
        #
        # Before
        # text    = "Hello"
        # cursor  = 3
        # display = "Hel|lo"
        #
        # Typing X
        #
        # After
        # text    = "HelXlo"
        # cursor  = 4
        # display = "HelX|lo"
        #
        # ---------------- ANSWER ----------------

        elif 32 <= key <= 126:

            text = text[:cursor] + chr(key) + text[cursor:]

            cursor += 1
        # ----------------------------------------

        # BONUS: Can you figure out how to select one line up/down by yourself?

        elif key == curses.KEY_UP:

            display = text[:cursor] + "|" + text[cursor:]
        elif key == curses.KEY_DOWN:
            count = 0
            char = text[cursor]
            space_count = 0
            while char != "\n" or (cursor - count) == 0:
                space_count += 1
                count += 1
                char = text[cursor - count]
            i = 0
            while char != "\n":
                if (cursor + i) == (len(text) - 1):
                    break
            if (cursor + i) == (len(text) - 1):
                continue
            else:
                cursor += i
                cursor += space_count
            display = text[:cursor] + "|" + text[cursor:]


curses.wrapper(main)
