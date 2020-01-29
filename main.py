import sys
import time 
import random
import os

from colorama import Fore, Back, Style
from functions import *

title = """
   _____ _                 _      _____               _____            
  / ____(_)               | |    |  __ \             / ____|           
 | (___  _ _ __ ___  _ __ | | ___| |__) |_ _ ___ ___| |  __  ___ _ __  
  \___ \| | '_ ` _ \| '_ \| |/ _ \  ___/ _` / __/ __| | |_ |/ _ \ '_ \ 
  ____) | | | | | | | |_) | |  __/ |  | (_| \__ \__ \ |__| |  __/ | | |
 |_____/|_|_| |_| |_| .__/|_|\___|_|   \__,_|___/___/\_____|\___|_| |_|
                    | |                                                
                    |_|                                                
"""

options = """
 [1] Generate a wordlist
 [2] Create a random password
"""

checkVersion()
clear()

print(title)
print(options)

try:
	while True:
		choice0 = input("")

		if choice0.lower() == "1":
			clear()
			print(title)
			listCreating()
except KeyboardInterrupt:
	sys.exit(Fore.BLUE + "\nThanks for using SimplePassGen by TheCountVEVO :)")
	print(Style.RESET_ALL)