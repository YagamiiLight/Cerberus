from sys import platform

if platform.startswith('win32'):
    red = purple = blue_green = blue_green_banner = red_banner = blue = green = end = ''

else:

    red = '\033[25;31m'
    purple = '\033[25;35m'
    blue_green = '\033[25;36m'
    blue_green_banner = '\033[5;36m'
    red_banner = '\033[5;31m'
    blue = '\033[25;34m'
    green = '\033[25;32m'

    end = '\033[0m'

"""
blue_green[+]
red [!]
purple [*]
green [~]
blue [#]
"""

