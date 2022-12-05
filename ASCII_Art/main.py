from pyfiglet import Figlet
from termcolor import colored

list_font = ["slant", "3-d", "3x5", "5lineoblique", "alphabet", "banner3-D", "doh", "isometric1", "letters", "alligator", "dotmatriz", "bubble", "bulbhead", "digital"]

result = Figlet(font="isometric1", width=110)
print()
print(colored(result.renderText("Rocha Gabriell"), color="green"))
print()