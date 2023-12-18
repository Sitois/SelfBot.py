import json
import time
from datetime import datetime
import requests
import fr_en_commands, config, config_commands


def print_with_timestamp(message):
    timestamp = datetime.now().strftime("[%H:%M:%S]")
    print(f"{timestamp} {message}")



def modifier_message(salon, texte, message_id):
    url = f"https://discord.com/api/v9/channels/{salon}/messages/{message_id}"
    headers = {
        "Authorization": f"{config_commands.commands_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "content": texte
    }
  
    response = requests.patch(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        print_with_timestamp("Le message a été modifié avec succès.")
    else:
        print_with_timestamp(f"Erreur lors de l'envoi de la réponse : Code d'erreur : {response.status_code} Message d'erreur : {response.text}")

def envoyer_message(salon, texte):
    url = f"https://discord.com/api/v9/channels/{salon}/messages"
    headers = {
        "Authorization": f"{config_commands.commands_token}",
        "Content-Type": "application/json"
    }
    data = {
        "content": texte
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print_with_timestamp("Réponse à la commande envoyée.")
    else:
        print_with_timestamp(f"Erreur lors de l'envoi de la réponse : Code d'erreur : {response.status_code} Message d'erreur : {response.text}")

def nitro_sniper(texte):
    url = f"https://discord.com/api/v9/channels/{config_commands.notifier_channel_id}/messages"
    headers = {
        "Authorization": f"{config_commands.notifier_token}",
        "Content-Type": "application/json"
    }
    data = {
        "content": texte
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print_with_timestamp("Nitro found. Check the channel.")
    else:
        print_with_timestamp(f"Erreur lors de l'envoi de la réponse : Code d'erreur : {response.status_code} Message d'erreur : {response.text}")


def notifier(texte):
    url = f"https://discord.com/api/v9/channels/{config_commands.notifier_channel_id}/messages"
    headers = {
        "Authorization": f"{config_commands.notifier_token}",
        "Content-Type": "application/json"
    }
    data = {
        "content": texte
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print_with_timestamp("Debug Mode. Check the notifier channel.")
    else:
        print_with_timestamp(f"Erreur lors de l'envoi de la réponse : Code d'erreur : {response.status_code} Message d'erreur : {response.text}")



def supprimer_messages(salon, nombre_messages):
    url = f"https://discord.com/api/v9/channels/{salon}/messages"
    headers = {
        "Authorization": f"{config_commands.commands_token}",
        "Content-Type": "application/json"
    }
    params = {"limit": nombre_messages + 1}
    
    
    response = requests.get(url, headers=headers, params=params)
    time.sleep(0.7)
    if response.status_code == 200:
        messages = response.json()
        for message in messages:
            delete_url = f"https://discord.com/api/v9/channels/{salon}/messages/{message['id']}"
            delete_response = requests.delete(delete_url, headers=headers)
            if delete_response.status_code != 204:
                print_with_timestamp(f"Erreur lors de la suppression d'un message : Code d'erreur : {delete_response.status_code} Message d'erreur :  {delete_response.text}")
    else:
        print_with_timestamp(f"Erreur lors de l'envoi de la réponse : Code d'erreur : {response.status_code} Message d'erreur : {response.text}")


def send_cat_image(salon, message_id):


    requests.get('https://api.thecatapi.com/v1/images/search')

    if requests.get('https://api.thecatapi.com/v1/images/search').status_code == 200:
        data = json.loads(requests.get('https://api.thecatapi.com/v1/images/search').text)
    else:
        print(fr_en_commands.request_not_success[config.langue], requests.get('https://api.thecatapi.com/v1/images/search').text, requests.get('https://api.thecatapi.com/v1/images/search').status_code)

    cat_image_url = data[0]['url']

    url = f"https://discord.com/api/v9/channels/{salon}/messages/{message_id}"
    headers = {
        "Authorization": f"{config_commands.commands_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "content": cat_image_url
    }
  
    response = requests.patch(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        print_with_timestamp("Le message a été modifié avec succès.")
    else:
        print_with_timestamp(f"Erreur lors de l'envoi de la réponse : Code d'erreur : {response.status_code} Message d'erreur : {response.text}")