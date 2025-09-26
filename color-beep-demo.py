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
