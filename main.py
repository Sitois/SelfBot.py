import subprocess
try:
    import os
    import sys
    import random
    from colorama import Fore, Back, Style
    import requests
    import config
    import json
    import time
    import ressources
    import fr_en
    from hugchat import hugchat
    from hugchat.login import Login
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", '-r' , 'requirements.txt'])
    import os
    import sys
    import random
    from colorama import Fore, Back, Style
    import requests
    import config
    import json
    import time
    import ressources
    import fr_en
    from hugchat import hugchat
    from hugchat.login import Login






if config.disclaimer == "yes":
    print(Fore.LIGHTRED_EX + r'''
  █     █░ ▄▄▄       ██▀███   ███▄    █  ██▓ ███▄    █   ▄████    
 ▓█░ █ ░█░▒████▄    ▓██ ▒ ██▒ ██ ▀█   █ ▓██▒ ██ ▀█   █  ██▒ ▀█▒   
 ▒█░ █ ░█ ▒██  ▀█▄  ▓██ ░▄█ ▒▓██  ▀█ ██▒▒██▒▓██  ▀█ ██▒▒██░▄▄▄░   
 ░█░ █ ░█ ░██▄▄▄▄██ ▒██▀▀█▄  ▓██▒  ▐▌██▒░██░▓██▒  ▐▌██▒░▓█  ██▓   
 ░░██▒██▓  ▓█   ▓██▒░██▓ ▒██▒▒██░   ▓██░░██░▒██░   ▓██░░▒▓███▀▒   
 ░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▒░   ▒ ▒ ░▓  ░ ▒░   ▒ ▒  ░▒   ▒    
   ▒ ░ ░    ▒   ▒▒ ░  ░▒ ░ ▒░░ ░░   ░ ▒░ ▒ ░░ ░░   ░ ▒░  ░   ░    
   ░   ░    ░   ▒     ░░   ░    ░   ░ ░  ▒ ░   ░   ░ ░ ░ ░   ░    
    ░          ░  ░   ░              ░  ░           ░       ░    
                                                                 
''' + Style.RESET_ALL)
    print('')
    print(Fore.RED + fr_en.warning_message[config.langue] + Style.RESET_ALL)
    time.sleep(4)
    exit_second = input(Fore.MAGENTA + fr_en.exit_ask_warning[config.langue])
    print(Style.RESET_ALL)
    if exit_second == exit_second:
      os.system('cls' if os.name == 'nt' else 'clear')



texte = r'''

 $$$$$$\  $$\       $$\            $$\      $$$\  $$$$$$\            $$\  $$$$$$\$$$\   $$$$$$$\             $$\     
$$  __$$\ $$ |      \__|           $$ |    $$  _|$$  __$$\           $$ |$$  __$$\\$$\  $$  __$$\            $$ |    
$$ /  \__|$$ |      $$\ $$$$$$$\ $$$$$$\  $$  /  $$ /  \__| $$$$$$\  $$ |$$ /  \__|\$$\ $$ |  $$ | $$$$$$\ $$$$$$\   
$$ |      $$ |      $$ |$$  __$$\\_$$  _| $$ |   \$$$$$$\  $$  __$$\ $$ |$$$$\      $$ |$$$$$$$\ |$$  __$$\\_$$  _|  
$$ |      $$ |      $$ |$$ |  $$ | $$ |   $$ |    \____$$\ $$$$$$$$ |$$ |$$  _|     $$ |$$  __$$\ $$ /  $$ | $$ |    
$$ |  $$\ $$ |      $$ |$$ |  $$ | $$ |$$\\$$\   $$\   $$ |$$   ____|$$ |$$ |      $$  |$$ |  $$ |$$ |  $$ | $$ |$$\ 
\$$$$$$  |$$$$$$$$\ $$ |$$ |  $$ | \$$$$  |\$$$\ \$$$$$$  |\$$$$$$$\ $$ |$$ |    $$$  / $$$$$$$  |\$$$$$$  | \$$$$  |
 \______/ \________|\__|\__|  \__|  \____/  \___| \______/  \_______|\__|\__|    \___/  \_______/  \______/   \____/                                                                                                     
                                                                                                                     
'''
colored_text = Fore.GREEN + texte + Style.RESET_ALL
print(colored_text)


# Simplification de Colorama.
red = Fore.RED
blue = Fore.BLUE
cyan = Fore.CYAN
yellow = Fore.YELLOW
magenta = Fore.MAGENTA
back_green = Back.GREEN
green = Fore.GREEN
light_green = Fore.LIGHTGREEN_EX
reset_color = Style.RESET_ALL




print(magenta + "                       The only Self-Bot that is easy to use !", reset_color)
print("")
print(blue + "                       Made by someone ! ", reset_color)
print("")
print("")


if config.langue == "fr":
    1 + 1
elif config.langue == "en":
    1 + 1
else:
    print(Fore.LIGHTRED_EX + "fr: Langue Incorrecte (voir config.py) | en: Incorrect Language. (see config.py)", reset_color)

token = input(red + fr_en.login_token_message[config.langue])
reset_color
print("")


if token == "":
   token = config.token
elif token == "restart":
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system(f'py "{config.main_path}"')


if token == "" and config.token == "":
    print(fr_en.error_token[config.langue])



print(cyan + "[1]", reset_color, yellow + fr_en.choix_ecriture[config.langue], reset_color, red + fr_en.barriere_un[config.langue], reset_color, cyan + "[2]", reset_color, yellow + fr_en.choix_envoyer[config.langue])

print(cyan + "[quit]", reset_color, yellow + fr_en.choix_quit[config.langue], reset_color, red + fr_en.barriere_deux[config.langue], reset_color, cyan + "[3]", reset_color, yellow + fr_en.choix_customiser_statut[config.langue], reset_color)

print(cyan + "[4]", reset_color, yellow + fr_en.choix_change_status[config.langue], reset_color, red + fr_en.barriere_trois[config.langue], reset_color, cyan + "[5]", reset_color, yellow + fr_en.choix_fake_nitro[config.langue], reset_color)


print("")


print("               ", cyan +  "[command]", reset_color, light_green + fr_en.choix_command[config.langue], reset_color)

print("")


choix = input(fr_en.choix_des_options[config.langue])

if choix.lower() == "restart":
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system(f'py "{config.main_path}"')
elif choix == "":
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system(f'py "{config.main_path}"')
elif choix.lower() == "quit":
    exit()
elif choix == "1":
   print(yellow + "------------", reset_color)

   CHANNEL_ID = input(fr_en.input_channel[config.langue])
 

   ressources.fake_typing(token, CHANNEL_ID)
 


   print(red + "------------", reset_color)
   exit_first = input(magenta + fr_en.exit_ask[config.langue])
   print(reset_color)
   if exit_first == exit_first:
     os.system('cls' if os.name == 'nt' else 'clear')
     os.system(f'py "{config.main_path}"')
elif choix == "2":
  print(yellow + "------------", reset_color)
  CHANNEL_ID = input(fr_en.input_channel[config.langue])
  contenu = input(fr_en.message_content[config.langue])

  ressources.send_message(token, contenu, CHANNEL_ID)

  print(red + "------------", reset_color)
  exit_second = input(magenta + fr_en.exit_ask[config.langue])
  print(reset_color)
  if exit_second == exit_second:
     os.system('cls' if os.name == 'nt' else 'clear')
     os.system(f'py "{config.main_path}"')
elif choix == "3":  
   print(yellow + "------------", reset_color)
   game = input(blue + fr_en.new_status_ask[config.langue])
   print(reset_color)
   


   ressources.set_status(token, game)
    


   print(red + "------------", reset_color)
   exit_fourth = input(magenta + fr_en.exit_ask[config.langue])
   print(reset_color)
   if exit_fourth == exit_fourth:
         os.system('cls' if os.name == 'nt' else 'clear')
         os.system(f'py "{config.main_path}"')
elif choix == "4":
    print(yellow + "------------", reset_color)
    statut = input(fr_en.status_ask[config.langue])
    
    ressources.changer_statut(token, statut)

    print(red + "------------", reset_color)
    exit_fifth = input(magenta + fr_en.exit_ask[config.langue])
    print(reset_color)
    if exit_fifth == exit_fifth:
          os.system('cls' if os.name == 'nt' else 'clear')
          os.system(f'py "{config.main_path}"')
elif choix == "5":
  print(yellow + "------------", reset_color)
  CHANNEL_ID = input(fr_en.input_channel[config.langue])
  
  
  ressources.fake_nitro(token, CHANNEL_ID)


  print(red + "------------", reset_color)
  exit_six = input(magenta + fr_en.exit_ask[config.langue])
  print(reset_color)

  if exit_six == exit_six:
     os.system('cls' if os.name == 'nt' else 'clear')
     os.system(f'py "{config.main_path}"')
elif choix.lower() == "command":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored_text)
    print(red + fr_en.command_success[config.langue], reset_color)
    print(light_green + fr_en.command_wait[config.langue], reset_color)
    import commands
elif choix.lower() == "commande":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored_text)
    print(red + fr_en.command_success[config.langue], reset_color)
    print(light_green + fr_en.command_wait[config.langue], reset_color)
    import commands
elif choix.lower() == "commandes":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored_text)
    print(red + fr_en.command_success[config.langue], reset_color)
    print(light_green + fr_en.command_wait[config.langue], reset_color)
    import commands
elif choix.lower() == "commands":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored_text)
    print(red + fr_en.command_success[config.langue], reset_color)
    print(light_green + fr_en.command_wait[config.langue], reset_color)
    import commands
elif choix.lower() == "comand":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored_text)
    print(red + fr_en.command_success[config.langue], reset_color)
    print(light_green + fr_en.command_wait[config.langue], reset_color)
    import commands
else:
      print(red + "------------", reset_color)
      print(Fore.LIGHTYELLOW_EX + fr_en.error_choice[config.langue])
      exit_six = input(magenta + fr_en.exit_ask[config.langue])
      print(reset_color)

      if exit_six == exit_six:
         os.system('cls' if os.name == 'nt' else 'clear')
         os.system(f'py "{config.main_path}"')
