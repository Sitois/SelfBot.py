import requests
import json
import time
import config, config_commands
from colorama import Fore, Back, Style
import random
import ressources_commands
import fr_en_commands
from hugchat import hugchat
from hugchat.login import Login
import base64
from datetime import datetime


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


poetry = {
    "fr": [
     "Jour meilleur n'existe qu'avec douleur.",
     "La seule personne que vous êtes destiné à devenir est la personne que vous décidez d'être.",
     "L'avenir appartient à ceux qui croient en la beauté de leurs rêves.",
     "L'échec est le fondement de la réussite.",
     "Ne rêvez pas votre vie, vivez vos rêves.",
     "Crois en toi, et les autres suivront.",
     "Sois le changement que tu veux voir dans le monde.",
     "Poursuis tes rêves, ils connaissent le chemin.",
     "La vie récompense l'action.",
     "Tu es plus fort que tu ne le crois.",
     "Le succès commence par l'action.",
     "La persévérance bat le talent.",
     "Ne remettez pas à demain.",
     "Chaque effort compte.",
     "Les montagnes les plus hautes ont les pentes les plus raides.",
     "Les éclats de lumière percent l'obscurité la plus profonde."
    ],
    "en": [
     "Your attitude determines your direction.",
     "Progress, not perfection.",
     "Embrace the challenges, for they are the stepping stones to success.",
     "Embrace failure as a stepping stone, not a stumbling block.",
     "The only limits that exist are the ones you place on yourself.",
     "Courage is not the absence of fear but the triumph over it.",
     "Dreams don't work unless you do",
     "Opportunities don't happen. You create them.",
     "Don't wait for the perfect moment; take the moment and make it perfect.",
     "The only way to do great work is to love what you do.",
     "Believe you can, and you're halfway there.",
     "Don't watch the clock; do what it does. Keep going"
    ],
}



print(Fore.LIGHTRED_EX + fr_en_commands.account_id_info[config.langue], config_commands.account_id, Fore.LIGHTCYAN_EX, fr_en_commands.info_channel[config.langue], config_commands.CHANNEL_ID, Style.RESET_ALL)

requests.get('https://api.thecatapi.com/v1/images/search')

if requests.get('https://api.thecatapi.com/v1/images/search').status_code == 200:
      data = json.loads(requests.get('https://api.thecatapi.com/v1/images/search').text)
      if len(data) > 0:
          cat_image_url = data[0]['url']
          print("Cat command URL :", cat_image_url)
      else:
          print(fr_en_commands.cat_error[config.langue])
else:
       print(fr_en_commands.request_not_success[config.langue], requests.get('https://api.thecatapi.com/v1/images/search').text, requests.get('https://api.thecatapi.com/v1/images/search').status_code)

cat_image_url = data[0]['url']


if config_commands.commands_token == "":
    config_commands.commands_token = input(Fore.LIGHTYELLOW_EX + "Token :")
    Style.RESET_ALL
else:
    1 + 1

if config_commands.account_id == "":
    config_commands.account_id = input(Fore.LIGHTRED_EX + "ID :")
    Style.RESET_ALL
else:
    1 + 1


if config_commands.CHANNEL_ID == "":
    config_commands.CHANNEL_ID = input(Fore.LIGHTCYAN_EX + fr_en_commands.info_channel[config.langue])
    Style.RESET_ALL
else:
    1 + 1


if config_commands.nitro_toggle == True and config_commands.notifier_channel_id == "":
    config_commands.notifier_channel_id = input(Fore.LIGHTCYAN_EX + fr_en_commands.info_nitro[config.langue])
    Style.RESET_ALL
else:
    1 + 1

print(Fore.LIGHTGREEN_EX + "---------")
print(Fore.LIGHTYELLOW_EX, "Logs :")
Fore.LIGHTCYAN_EX

dernier_message_id = None

message_id_log = []

list_custom_channel = []






def detecter_message():
    global dernier_message_id
    for channel_id in [config_commands.CHANNEL_ID] + list_custom_channel:
     url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
     headers = {
            "Authorization": f"{config_commands.commands_token}",
            "Content-Type": "application/json"}
     params = {"after": dernier_message_id} 
     response = requests.get(url, headers=headers, params=params)
     if response.status_code == 200:
        messages = response.json()
        for message in messages:
            nitro_content = message["content"]
            if message["content"].lower() == f"{config_commands.prefix}{config_commands.cat_command}" and message["author"]["id"] in config_commands.account_id:
                dernier_message_id = message["id"]
                message_id_log.append(dernier_message_id)
                ressources_commands.modifier_message(channel_id, cat_image_url, dernier_message_id)
                if config_commands.debug_mode == True:
                    ressources_commands.notifier(f"<@{config_commands.account_id}> command: : {nitro_content}")
            elif message["content"].lower() == f"{config_commands.prefix}{config_commands.nitro_command}" and message["author"]["id"] in config_commands.account_id:
                dernier_message_id = message["id"]
                message_id_log.append(dernier_message_id)                
                ressources_commands.modifier_message(channel_id, f"https://discord.gift/{alphabet_aleatoire}{alphabet_aleatoire_un}{alphabet_aleatoire_deux}{alphabet_majuscule_aleatoire}{alphabet_aleatoire_trois}{alphabet_majuscule_aleatoire_un}{alphabet_majuscule_aleatoire_deux}{alphabet_aleatoire_quatre}{alphabet_majuscule_aleatoire_trois}{alphabet_aleatoire_cinq}{alphabet_aleatoire_six}{alphabet_majuscule_aleatoire_quatre}{alphabet_aleatoire_sept}{alphabet_majuscule_aleatoire_cinq}{chiffres_aleatoire_un}", dernier_message_id)
                if config_commands.debug_mode == True:
                    ressources_commands.notifier(f"<@{config_commands.account_id}> command: : {nitro_content}")
            elif message["content"].lower() == f"{config_commands.prefix}{config_commands.snipe_command}" and message["author"]["id"] in config_commands.account_id:
                dernier_message_id = message["id"]
                message_id_log.append(dernier_message_id)
                ressources_commands.modifier_message(channel_id, f"{config_commands.snipe_answer}", dernier_message_id)
                if config_commands.debug_mode == True:
                    ressources_commands.notifier(f"<@{config_commands.account_id}> command: : {nitro_content}")
            elif message["content"].lower() == f"{config_commands.prefix}{config_commands.commande_un}" and message["author"]["id"] in config_commands.account_id:
                dernier_message_id = message["id"]
                message_id_log.append(dernier_message_id)
                ressources_commands.modifier_message(channel_id, f"{config_commands.reponse_un}", dernier_message_id)
                if config_commands.debug_mode == True:
                    ressources_commands.notifier(f"<@{config_commands.account_id}> command: : {nitro_content}")
            elif message["content"].lower() == f"{config_commands.prefix}{config_commands.commande_deux}" and message["author"]["id"] in config_commands.account_id:
                dernier_message_id = message["id"]
                message_id_log.append(dernier_message_id)
                ressources_commands.modifier_message(channel_id, f"{config_commands.reponse_deux}", dernier_message_id)
                if config_commands.debug_mode == True:
                    ressources_commands.notifier(f"<@{config_commands.account_id}> command: : {nitro_content}")
            elif message["content"].lower().startswith(f"{config_commands.prefix}{config_commands.commande_trois}") and message["author"]["id"] in config_commands.account_id:
                dernier_message_id = message["id"]
                message_id_log.append(dernier_message_id)
                message_content = message["content"][len(f"{config_commands.prefix}{config_commands.commande_trois}"):]
                ressources_commands.modifier_message(channel_id, f"{config_commands.reponse_trois}", dernier_message_id)
                if config_commands.debug_mode == True:
                    ressources_commands.notifier(f"<@{config_commands.account_id}> command: : {nitro_content}")
            elif message["content"].lower().startswith(f"{config_commands.prefix}{config_commands.token_to_id}") and message["author"]["id"] in config_commands.account_id:
                dernier_message_id = message["id"]
                message_id_log.append(dernier_message_id)
                id = message["content"][len(f"{config_commands.prefix}{config_commands.token_to_id}"):]
                id = id.strip()
                encode_text = base64.b64encode(id.encode('utf-8'))
                ressources_commands.modifier_message(channel_id, f"🌠| Résultat: `{encode_text.strip()}`", dernier_message_id)
                if config_commands.debug_mode == True:
                    ressources_commands.notifier(f"<@{config_commands.account_id}> command: : {nitro_content}")
            elif message["content"].lower() == f"{config_commands.prefix}{config_commands.commande_quatre}" and message["author"]["id"] in config_commands.account_id:
                dernier_message_id = message["id"]
                message_id_log.append(dernier_message_id)
                ressources_commands.modifier_message(channel_id, f"{config_commands.reponse_quatre}", dernier_message_id)
                if config_commands.debug_mode == True:
                    ressources_commands.notifier(f"<@{config_commands.account_id}> command: : {nitro_content}")
            elif message["content"].lower() == f"{config_commands.prefix}{config_commands.commande_cinq}" and message["author"]["id"] in config_commands.account_id:
                dernier_message_id = message["id"]
                message_id_log.append(dernier_message_id)
                ressources_commands.modifier_message(channel_id, f"{config_commands.reponse_cinq}", dernier_message_id)
                if config_commands.debug_mode == True:
                    ressources_commands.notifier(f"<@{config_commands.account_id}> command: : {nitro_content}")
            elif message["content"].lower() == f"{config_commands.prefix}{config_commands.commande_aled}" and message["author"]["id"] in config_commands.account_id:
                dernier_message_id = message["id"]
                message_id_log.append(dernier_message_id)
                for element in message_id_log:
                    ressources_commands.modifier_message(channel_id, random.choice(poetry[config.langue]), element)
                    time.sleep(0.8)
                for i in range(len(message_id_log)):
                    message_id_log.pop()
                print("Danger Command. Cleared messages.")
                ressources_commands.modifier_message(channel_id, random.choice(poetry[config.langue]), message_id_log)
                time.sleep(0.5)
                if config_commands.debug_mode == True:
                    ressources_commands.notifier(f"<@{config_commands.account_id[0]}> command: : {nitro_content}")             
            elif message["content"].lower() == f"{config_commands.prefix}{config_commands.stop_command}" and message["author"]["id"] in config_commands.account_id:
                dernier_message_id = message["id"]
                ressources_commands.modifier_message(channel_id, f"🌠| __**Clint(Self)Bot:**__ arrêt...", dernier_message_id)
                time.sleep(0.6)
                ressources_commands.modifier_message(channel_id, f"{random.choice(poetry[config.langue])}", dernier_message_id)
                exit()
            elif f"discord.com/gift/" in message["content"].lower():
                dernier_message_id = message["id"]
                if config_commands.nitro_toggle == True:
                    ressources_commands.nitro_sniper(f"<@{config_commands.account_id[0]}> Nitro : {nitro_content}")
            elif "discord.gift/" in message["content"].lower():
                dernier_message_id = message["id"]
                if config_commands.nitro_toggle == True:
                    nitro_content = message["content"]
                    ressources_commands.nitro_sniper(f"<@{config_commands.account_id[0]}> Nitro : {nitro_content}")
            elif message["content"].lower().startswith(f"{config_commands.prefix}{config_commands.add_channel}") and message["author"]["id"] in config_commands.account_id:
                dernier_message_id = message["id"]
                message_id_log.append(dernier_message_id)
                if len(list_custom_channel) < 5:
                        new_channel = message["content"][len(f"{config_commands.prefix}{config_commands.add_channel}"):]
                        if len(new_channel.strip()) == 19:
                            if new_channel in list_custom_channel:
                                    ressources_commands.modifier_message(channel_id, f"❌| Ce salon a déjà été défini !", dernier_message_id)
                            else:
                                    list_custom_channel.append(new_channel.strip())
                                    ressources_commands.modifier_message(channel_id, f"✅| Channel successfully added. (<#{new_channel.strip()}>)", dernier_message_id)
                        else:
                            ressources_commands.modifier_message(channel_id, f"❌| Incorrect Channel ID.", dernier_message_id)
                else:
                    ressources_commands.modifier_message(channel_id, f"🔴| Salons complet ! (faites `{config_commands.prefix}{config_commands.del_channel}` pour supprimer le dernier salon de la liste des salons !)", dernier_message_id)
                if config_commands.debug_mode == True:
                    ressources_commands.notifier(f"<@{config_commands.account_id}> command: {nitro_content}")
            elif message["content"].lower() == f"{config_commands.prefix}{config_commands.list_channel}" and message["author"]["id"] in config_commands.account_id:
                dernier_message_id = message["id"]
                message_id_log.append(dernier_message_id)
                if len(list_custom_channel) == 1:
                    ressources_commands.modifier_message(salon=channel_id, texte=fr"""__**📔| Channel Dashboard :**__ 
🧶| 1. <#{list_custom_channel[0]}>""", message_id=dernier_message_id)
                elif len(list_custom_channel) == 2:
                    ressources_commands.modifier_message(salon=channel_id, texte=rf"""__**📔| Channel Dashboard :**__ 
🧶| 1. <#{list_custom_channel[0]}>
🧵| 2. <#{list_custom_channel[1]}>""", message_id=dernier_message_id)
                elif len(list_custom_channel) == 3:
                    ressources_commands.modifier_message(salon=channel_id, texte=rf"""__**📔| Channel Dashboard :**__ 
🧶| 1. <#{list_custom_channel[0]}>
🧵| 2. <#{list_custom_channel[1]}>
🪡| 3. <#{list_custom_channel[2]}>""", message_id=dernier_message_id)
                elif len(list_custom_channel) == 4:
                    ressources_commands.modifier_message(salon=channel_id, texte=rf"""__**📔| Channel Dashboard :**__ 
🧶| 1. <#{list_custom_channel[0]}>
🧵| 2. <#{list_custom_channel[1]}>
🪡| 3. <#{list_custom_channel[2]}>
🪢| 4. <#{list_custom_channel[3]}>""", message_id=dernier_message_id)
                elif len(list_custom_channel) == 5:
                    ressources_commands.modifier_message(salon=channel_id, texte=rf"""__**📔| Channel Dashboard :**__ 
🧶| 1. <#{list_custom_channel[0]}>
🧵| 2. <#{list_custom_channel[1]}>
🪡| 3. <#{list_custom_channel[2]}>
🪢| 4. <#{list_custom_channel[3]}>
🎟️| 5. <#{list_custom_channel[4]}>""", message_id=dernier_message_id)
                else:
                    ressources_commands.modifier_message(channel_id, rf"""__**📔| Channel Dashboard :**__
❌| No channel.""", dernier_message_id)

                if config_commands.debug_mode == True:
                    ressources_commands.notifier(f"<@{config_commands.account_id}> command: {nitro_content}")
            elif message["content"].lower().startswith(f"{config_commands.prefix}{config_commands.del_channel}") and message["author"]["id"] in config_commands.account_id:
                dernier_message_id = message["id"]
                message_id_log.append(dernier_message_id)
                if len(list_custom_channel) > 0:
                    list_custom_channel.pop()
                    ressources_commands.modifier_message(channel_id, f"🧨| Channel successfully deleted.", dernier_message_id)
                else:
                    ressources_commands.modifier_message(channel_id, f"❌| Channel list is empty !", dernier_message_id)
                if config_commands.debug_mode == True:
                    ressources_commands.notifier(f"<@{config_commands.account_id}> command: {nitro_content}")
            elif message["content"].lower() == f"{config_commands.prefix}{config_commands.commande_help}" and message["author"]["id"] in config_commands.account_id:
                dernier_message_id = message["id"]
                message_id_log.append(dernier_message_id) # ☀ 
                ressources_commands.modifier_message(channel_id, rf'''☄ __**SelfBot.py, *Clint(Self)Bot*  :**__ ☄
  ☄ "{random.choice(poetry[config.langue])}" ☄
  
  🏮| __**GENERAL:**__: `{config_commands.prefix}{config_commands.general_help_command}`
  🌠| __**{fr_en_commands.part_two_help[config.langue]}:**__ `{config_commands.prefix}{config_commands.perso_help_command}`
  ☣️| __**DANGER ZONE:**__ `{config_commands.prefix}{config_commands.danger_help_command}`''', dernier_message_id)
            elif message["content"].lower() == f"{config_commands.prefix}{config_commands.general_help_command}" and message["author"]["id"] in config_commands.account_id:
                dernier_message_id = message["id"]
                message_id_log.append(dernier_message_id)
                ressources_commands.modifier_message(channel_id, rf'''☄ __**SelfBot.py, *Clint(Self)Bot*  :**__ ☄:
                                                     
  🏮| __**GENERAL:**__
  __Prefix:__ `{config_commands.prefix}`,  {fr_en_commands.ai_for_all_boo[config.langue]}: `{f"{fr_en_commands.true_bool[config.langue]}" if config_commands.ai_for_all == True else f'{fr_en_commands.false_bool[config.langue]}'}`
  __**Add_Channel:**__ `{config_commands.prefix}{config_commands.add_channel}`, Channel Counter: `{len(list_custom_channel)}`, Channel List: `{config_commands.prefix}{config_commands.list_channel}`, Delete Channel: `{config_commands.prefix}{config_commands.del_channel}`
  __**Nitro Sniper**__ : `{f"{fr_en_commands.true_bool[config.langue]}" if config_commands.nitro_toggle == True else f'{fr_en_commands.false_bool[config.langue]}'}` ,  **{fr_en_commands.info_channel[config.langue]} <#{config_commands.notifier_channel_id}>**
  __**{fr_en_commands.ai_command_help[config.langue]}:**__ `{config_commands.prefix}{config_commands.commande_ai}`,  IsNitro : `{f"{fr_en_commands.true_bool[config.langue]}" if config_commands.is_nitro == 3900 else f'{fr_en_commands.false_bool[config.langue]}'}`
  __**{fr_en_commands.clear_ai_help[config.langue]} :**__ `{config_commands.prefix}{config_commands.commande_ia_clear}`
  __**Clear:**__ `{config_commands.prefix}{config_commands.clear_command}` (__Max:__ __{config_commands.max_clear}__)''', dernier_message_id)
            elif message["content"].lower() == f"{config_commands.prefix}{config_commands.perso_help_command}" and message["author"]["id"] in config_commands.account_id:
                dernier_message_id = message["id"]
                message_id_log.append(dernier_message_id)
                ressources_commands.modifier_message(channel_id, rf'''☄ __**SelfBot.py, *Clint(Self)Bot*  :**__ ☄
                                                     
  🌠| __**{fr_en_commands.part_two_help[config.langue]}:**__
  **{config_commands.prefix}{config_commands.commande_help}**: {config_commands.help_definition}
  **{config_commands.prefix}{config_commands.cat_command}**: {config_commands.cat_definition}
  **{config_commands.prefix}{config_commands.nitro_command}**: {config_commands.nitro_definition}
  **{config_commands.prefix}{config_commands.snipe_command}**: {config_commands.snipe_definition}
  **{config_commands.prefix}{config_commands.commande_un}**: {config_commands.un_definition}
  **{config_commands.prefix}{config_commands.commande_deux}**: {config_commands.deux_definition}
  **{config_commands.prefix}{config_commands.commande_trois}**: {config_commands.trois_definition}
  **{config_commands.prefix}{config_commands.commande_quatre}**: {config_commands.quatre_definition}
  **{config_commands.prefix}{config_commands.commande_cinq}**: {config_commands.cinq_definition}''', dernier_message_id)
            elif message["content"].lower() == f"{config_commands.prefix}{config_commands.danger_help_command}" and message["author"]["id"] in config_commands.account_id:
                dernier_message_id = message["id"]
                message_id_log.append(dernier_message_id)
                ressources_commands.modifier_message(channel_id, rf'''☄ __**SelfBot.py, *Clint(Self)Bot*  :**__ ☄
  
  ☣️| __**DANGER ZONE:**__
  Danger Command: `{config_commands.prefix}{config_commands.commande_aled}`
  Eval Command: `{config_commands.prefix}{config_commands.eval_command}`,  IsEnabled: `{f"{fr_en_commands.true_bool[config.langue]}" if config_commands.eval_toggle == True else f"{fr_en_commands.false_bool[config.langue]}"}`
  **Stop Command:** `{config_commands.prefix}{config_commands.stop_command}`''', dernier_message_id)
            elif message["content"].lower() == f"{config_commands.prefix}{config_commands.commande_ia_clear}" and message["author"]["id"] in config_commands.account_id:
                dernier_message_id = message["id"]
                message_id_log.append(dernier_message_id) 
                # AI CONFIGURATION
                sign = Login(config_commands.hug_chat_email, config_commands.hug_chat_password)
                cookies = sign.login()
                chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
                chatbot.delete_all_conversations()
                ressources_commands.modifier_message(channel_id, f"🚮🤖| All AI conversations have been deleted.", dernier_message_id)
                if config_commands.debug_mode == True:
                    ressources_commands.notifier(f"<@{config_commands.account_id}> command: {nitro_content}")
            elif message["content"].lower().startswith(f"{config_commands.prefix}{config_commands.eval_command}") and message["author"]["id"] in config_commands.account_id:
                dernier_message_id = message["id"]
                message_id_log.append(dernier_message_id)
                message_content =  message["content"][len(f"{config_commands.prefix}{config_commands.eval_command}"):]
                message_content = message_content.strip()
                if config_commands.eval_toggle == True:
                    if message_content == f"exit()":
                        ressources_commands.modifier_message(channel_id, f"❌| __Error__: Use __**{config_commands.prefix}{config_commands.stop_command}**__ instead.", dernier_message_id)
                    else:
                        try:
                           eval_result = eval(message_content)
                           ressources_commands.modifier_message(channel_id, rf"""✅| Success:
```py
{eval_result}
```""", dernier_message_id)
                        except Exception as e:
                           ressources_commands.modifier_message(channel_id, rf"""❌| An error has occured:
```py
{e}
```""", dernier_message_id)
                else:
                    ressources_commands.modifier_message(channel_id, f"❌| Eval is currently disabled.", dernier_message_id)
                if config_commands.debug_mode == True:
                    ressources_commands.notifier(f"<@{config_commands.account_id}> command: : {nitro_content}")               
            elif message["content"].lower().startswith(f"{config_commands.prefix}{config_commands.commande_ai}") and message["author"]["id"] in config_commands.account_id:
                dernier_message_id = message["id"]
                message_id_log.append(dernier_message_id)
                sign = Login(config_commands.hug_chat_email, config_commands.hug_chat_password)
                cookies = sign.login()
                chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
                ai_ask = message["content"][len(f"{config_commands.prefix}{config_commands.commande_ai}"):]
                ressources_commands.modifier_message(channel_id, f"⌚| wait...", dernier_message_id)
                query_result = chatbot.query(f"{ai_ask}")
                ressources_commands.modifier_message(channel_id, fr"""❓| Question: {ai_ask}
✅| Réponse: {query_result}""", dernier_message_id)
                if config_commands.debug_mode == True:
                    ressources_commands.notifier(f"<@{config_commands.account_id}> command: : {nitro_content}")    
            elif message["content"].lower().startswith(f"{config_commands.prefix}{config_commands.commande_ai}") and not message["author"]["id"] in config_commands.account_id:
                dernier_message_id = message["id"]
                if config_commands.ai_for_all == True:
                    sign = Login(config_commands.hug_chat_email, config_commands.hug_chat_password)
                    cookies = sign.login()
                    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
                    ai_ask = message["content"][len(f"{config_commands.prefix}{config_commands.commande_ai}"):]
                    ressources_commands.envoyer_message(channel_id, f"⌚| wait...")
                    query_result = chatbot.query(f"{ai_ask}")
                    ressources_commands.supprimer_messages(channel_id, 1)
                    ressources_commands.envoyer_message(channel_id, fr"""❓| Question: {ai_ask.strip()}
✅| Réponse: {query_result}""")
                    if config_commands.debug_mode == True:
                       ressources_commands.notifier(f"<@{config_commands.account_id}> command: : {nitro_content}")            
            elif message["content"].lower().startswith(f"{config_commands.prefix}{config_commands.clear_command}") and message["author"]["id"] in config_commands.account_id:
              try:
                  words = message["content"].split()

                  if len(words) > 1:
                        nombre_messages = int(words[1])
                  else:
                     nombre_messages = 3

                  if nombre_messages > config_commands.max_clear:
                      ressources_commands.envoyer_message(channel_id, f"{fr_en_commands.clear_fail[config.langue]} {config_commands.max_clear}")
                      time.sleep(0.5)
                      ressources_commands.supprimer_messages(channel_id, 1)
                  else:
                      ressources_commands.supprimer_messages(channel_id, nombre_messages)
                      ressources_commands.envoyer_message(channel_id, f"> 🚮|   {nombre_messages} {fr_en_commands.deleted_messages[config.langue]}")
                      time.sleep(0.4)
                      ressources_commands.supprimer_messages(channel_id, 0)
              except:
                  ressources_commands.envoyer_message(channel_id, f"{fr_en_commands.clear_fail[config.langue]} {config_commands.max_clear}")
                  time.sleep(0.5)
                  ressources_commands.supprimer_messages(channel_id, 1)
     else:
        print(fr_en_commands.request_not_success[config.langue], response.status_code, response.text)
        print(Fore.RED + "Token error. / Channel error. / Rate limited." + Style.RESET_ALL)
        exit()



while True:
    detecter_message()
    time.sleep(1)
