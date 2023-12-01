import requests
import json
from colorama import Fore, Back, Style
import random
import fr_en
import config


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_majuscule = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
chiffres = [1, 2, 3, 4, 5 ,6, 7, 8, 9]
alphabet_aleatoire = random.choice(alphabet)
# FakeNitro
alphabet_aleatoire_un = random.choice(alphabet)
alphabet_aleatoire_deux = random.choice(alphabet)
alphabet_aleatoire_trois = random.choice(alphabet)
alphabet_aleatoire_quatre = random.choice(alphabet)
alphabet_aleatoire_cinq = random.choice(alphabet)
alphabet_aleatoire_six = random.choice(alphabet)
alphabet_aleatoire_sept = random.choice(alphabet)
alphabet_aleatoire_huit = random.choice(alphabet)
alphabet_aleatoire_neuf = random.choice(alphabet)
alphabet_aleatoire_dix = random.choice(alphabet)
# ---------------------------------------------
alphabet_majuscule_aleatoire = random.choice(alphabet_majuscule)
# FakeNitro majuscules
alphabet_majuscule_aleatoire_un = random.choice(alphabet_majuscule)
alphabet_majuscule_aleatoire_deux = random.choice(alphabet_majuscule)
alphabet_majuscule_aleatoire_trois = random.choice(alphabet_majuscule)
alphabet_majuscule_aleatoire_quatre = random.choice(alphabet_majuscule)
alphabet_majuscule_aleatoire_cinq = random.choice(alphabet_majuscule)
alphabet_majuscule_aleatoire_six = random.choice(alphabet_majuscule)
alphabet_majuscule_aleatoire_sept = random.choice(alphabet_majuscule)
alphabet_majuscule_aleatoire_huit = random.choice(alphabet_majuscule)
alphabet_majuscule_aleatoire_neuf = random.choice(alphabet_majuscule)
alphabet_majuscule_aleatoire_dix = random.choice(alphabet_majuscule)
# ---------------------------------------------
chiffres_aleatoire = random.choice(chiffres)
# FakeNitro chiffres
chiffres_aleatoire_un = random.choice(chiffres)
chiffres_aleatoire_deux = random.choice(chiffres)
chiffres_aleatoire_trois = random.choice(chiffres)
chiffres_aleatoire_quatre = random.choice(chiffres)
chiffres_aleatoire_cinq = random.choice(chiffres)
chiffres_aleatoire_six = random.choice(chiffres)
chiffres_aleatoire_sept = random.choice(chiffres)
chiffres_aleatoire_huit = random.choice(chiffres)
chiffres_aleatoire_neuf = random.choice(chiffres)
chiffres_aleatoire_dix = random.choice(chiffres)

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


def set_status(token, game):
      headers = {
          'Authorization': f'{token}',
      } 

      data = {
          'custom_status': {
              'text': f'{game}'
          }
      }

      response = requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, json=data)
 
      if response.status_code == 200:
          print(green + fr_en.status_success_part_un[config.langue], game, fr_en.status_success_part_deux[config.langue], reset_color)
      else:
          print(red + fr_en.status_fail_part_un[config.langue], {response.status_code}, fr_en.status_fail_part_deux[config.langue], response.text, reset_color) 


def fake_nitro(token, CHANNEL_ID):
  headers = {
      'Authorization': f'{token}',
      'Content-Type': 'application/json'
  }

  data = {
      'content': f"https://discord.gift/{alphabet_aleatoire}{alphabet_aleatoire_un}{alphabet_aleatoire_deux}{alphabet_majuscule_aleatoire}{alphabet_aleatoire_trois}{alphabet_majuscule_aleatoire_un}{alphabet_majuscule_aleatoire_deux}{alphabet_aleatoire_quatre}{alphabet_majuscule_aleatoire_trois}{alphabet_aleatoire_cinq}{alphabet_aleatoire_six}{alphabet_majuscule_aleatoire_quatre}{alphabet_aleatoire_sept}{alphabet_majuscule_aleatoire_cinq}{chiffres_aleatoire_un}"
  }

  response = requests.post(f'https://discord.com/api/v9/channels/{CHANNEL_ID}/messages', headers=headers, json=data)

  if response.status_code == 200:
      print(green + f'FakeNitro envoyé avec succès !', reset_color)
  else:
      print(red + "Erreur lors de l'envoi du message." + "Code d'erreur : ", response.status_code, "Message d'erreur :", response.text, reset_color)

def changer_statut(token, statut):
     headers = {
         "Authorization": f"{token}"
     }

     payload = {
         "status": statut
     }

     response = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=payload)

     if response.status_code == 200: 
         print(green + fr_en.status_set_part_un[config.langue], statut, fr_en.status_set_part_deux[config.langue], reset_color)
     else:
         print(red + "Erreur lors du changement de statut." + "Code d'erreur : ", response.status_code, "Message d'erreur :", response.text, reset_color)
   

def send_message(token, contenu, CHANNEL_ID):
  
  
 headers = {
     'Authorization': f'{token}',
     'Content-Type': 'application/json'
 }

 data = {
     'content': f'{contenu}'
 }

 response = requests.post(f'https://discord.com/api/v9/channels/{CHANNEL_ID}/messages', headers=headers, json=data)
 print(fr_en.request_success[config.langue], "(message :" + contenu + ")")

def fake_typing(token, CHANNEL_ID):
   url = f'https://discord.com/api/v9/channels/{CHANNEL_ID}/typing'
 
   headers = {
      'Authorization': f'{token}'
   }
 
   response = requests.post(url, headers=headers)
 
   if response.status_code == 204:
      print(fr_en.request_success[config.langue])
   else:
      print(fr_en.request_not_success[config.langue], {response.status_code}, "-", {response.text})
