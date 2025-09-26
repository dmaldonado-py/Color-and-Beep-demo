Color and Beep Demo
===================

This project comes from the old QBasic days, when functions like ``SCREEN`` and 
``BEEP`` were some of the only ways to bring life to console programs. You could 
show errors in red, confirmations in green, and use a beep to signal the user’s 
attention. Simple features like these made programs easier to use and gave them 
personality at a time when GUIs were not common.

Today, multimedia systems have replaced most of that, but these ideas are still 
useful. Colored text makes scripts easier to follow, and a quick beep is still one 
of the fastest ways to give feedback without building a full interface. This project 
shows how to do both in Python:

- **Colorama** for console text color (cross-platform).
- **Beep** using ``winsound`` on Windows or the ASCII bell (``\a``) on Linux/macOS.

Install
-------
Run this command to install the required library:

.. code-block:: bash

   pip install colorama

Run
---
.. code-block:: bash

   python main.py

Example
-------
.. code-block:: python

   from colorama import init, Fore, Back, Style
   import platform

   init()

   # basic colors
   print(Fore.RED + "Error: Something went wrong")
   print(Fore.GREEN + "Success: Operation completed")
   print(Fore.CYAN + "Info: This is cyan text")
   print(Fore.MAGENTA + "Debug: Value is out of range")

   # background colors
   print(Back.YELLOW + Fore.BLACK + "Warning with yellow background" + Style.RESET_ALL)

   # bright/bold style
   print(Style.BRIGHT + Fore.BLUE + "Bright blue text" + Style.RESET_ALL)

   # blinking text (may not work in all terminals)
   print("\033[5m" + Fore.YELLOW + "Blinking yellow text" + Style.RESET_ALL)

   # reset back to normal
   print(Style.RESET_ALL + "Back to normal text")

   # beep example
   if platform.system() == "Windows":
       import winsound
       winsound.Beep(1000, 500)  # 1000 Hz for 0.5 seconds
   else:
       print("\a")  # ASCII bell (Linux/macOS)

Notes
-----
- ``winsound.Beep`` only works on Windows.
- On Linux/macOS, the ASCII bell (``\a``) is used. Some terminals may have the bell disabled.
- Colab, Replit, and other online interpreters often do not show colors or play the beep.
- ``Style.RESET_ALL`` resets the style so colors don’t bleed into the next line.
