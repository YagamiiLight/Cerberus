import time
from core.colors import red,purple,blue,blue_green,end,green,blue_green_banner,red_banner
from concurrent.futures import ThreadPoolExecutor
time = time.strftime('%H:%M:%S')

def show_banner():
    banner = f"""{blue_green}
                     ▄████▄  ▓█████  ██▀███   ▄▄▄▄   ▓█████  ██▀███   █     ████████ 
            ▒██▀ ▀█  ▓█   ▀ ▓██ ▒ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒ ██  ▓██▒▒██   ▒ 
            ▒▓█    ▄ ▒███   ▓██ ░▄█ ▒▒██▒ ▄██▒███   ▓██ ░▄█ ▒▓██  ▒██░░  ▓██▄   
            ▒▓▓▄ ▄██▒▒▓█  ▄ ▒██▀▀█▄  ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  ▓▓█  ░██░  ▒   ██▒
            ▒ ▓███▀ ░░▒████▒░██▓ ▒██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒▒▒█████▓ ▒██████▒▒ {end}
            ░ ░▒ ▒  ░░░ ▒░ ░░ ▒▓ ░▒▓░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░
            {red_banner}░{end}  ▒    ░ ░  {green}░{end}  ░▒ ░ {green}▒░▒░▒{end}   ░  ░ ░  ░  {red_banner}░▒{end} ░ ▒░░░▒░ ░ ░ {red_banner}░{end} ░▒  ░ ░ 
            ░           ░   ░░   ░  ░    ░    ░     ░░   ░  {green}░░░ ░ ░{end} ░  ░  ░  
            ░ ░         ░  ░   {red_banner}░      ░{end}         ░  ░   ░        ░           ░  
            {red_banner}░{end}░
    
            {green}[{time}]{end} {purple}Cerberus v1.0{end}
            """
    print(banner)



if __name__ == '__main__':
    show_banner()