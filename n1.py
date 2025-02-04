import requests
import time
import os

delay = 0.1
# Regular Colors
BL = "\033[0;100m" # Black
R = "\033[0;101m" # Red
G = "\033[0;102m" # Green
Y = "\033[0;103m" # Yellow
B = "\033[0;104m" # Blue
P = "\033[0;105m" # Purple
C = "\033[0;106m" # Cyan
W = "\033[0;107m" # White
# Bold
bl = "\033[1;30m" # Black
r = "\033[1;31m" # Red
g = "\033[1;32m" # Green
y = "\033[1;33m" # Yellow
b = "\033[1;34m" # Blue
p = "\033[1;35m" # Purple
c = "\033[1;36m" # Cyan
w = "\033[1;37m" # White

def print_slow(text, d=delay):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(d)
      
print_slow(f"""\n\n\n\n\n\n\n
{R}{g}Black Cactus Hacking Group
{Y}{bl}🌐🏴‍☠HACKERS_WORLED
A channel for education - news - tricks - hacking - Kali and Termux tools
With support for three languages: English, Persian and Arabic

{B}Telegram ->\n {R}{y}@Grup_Hacking_Cactus_Black
{B}YouTube  ->\n {R}{y}@Grup_Hacking_Cactus_Black\n""",0.01)

input("enter 01010110001")
print("""\n\n\n\n
{C}{c}!!!  This is an old command and is for version 1.
{C}{c}!!!  This version is deprecated.
{C}{c}!!!  You can use the new version by referring to the SMS script""")

print("by!")
exit()
