debug_mode = False # (beta)
"""CONFIG  GENERAL COMMANDES"""
# fr: Token du compte pour les commandes.
# en: Account Token for commands
commands_token = ""
# fr: Votre ID de compte
# en: Account ID
account_id = [""]
# fr: ID du salon par défaut (vous pourrez ajouter d'autre salon en fesant: add [salon_id])
# en: Default Command Channel ID (you can add other channel with the -add [channel_id] command.)
CHANNEL_ID = "" # Laisser vide pour avoir la demande au démarrage.
add_channel = "add" # fr: Commande pour ajouter un salon avec son ID. / en: Add Channel Command.
del_channel = "del" # fr: Commande pour supprimer le dernier salon ajouté. / en: Delete Channel Command (Delete the last channel)
list_channel = "list" # fr: Comamnde pour voir la liste des salons. / en: Channel List Command
# fr: Prefix des commandes
# en: Commands Prefix
prefix = "-"
# fr: Commande danger. (modifie tout les messages auquel le selfbot a répondu.)
# en: Alert command. (edit all messages to which the selfbot has replied.)
commande_aled = "danger"


"""CONFIG COMMANDES"""
# fr: Nom de la commande QUI ENVERRA LE MESSAGE D'AIDE  (fonctionne seulement avec votre ID)
# en: Name of the command THAT WILL SEND THE HELP (work only with your ID)
commande_help = "help"
# fr: Description de la commande
# en: Command Description
help_definition = "Send the help of the SelfBot."

# fr: Commande Eval.
# en: Eval Command.
eval_command = "eval"
# en: DO NOT ENTER "True" unless you are aware of the risks (eval command allows you to execute arbitrary code to your machine; never run a script unless you know what it does)
# fr: NE PAS ENTRER "True" sauf si vous êtes en connaissance de risque (la commande eval permet d'éxécuter du code arbitraire sur votre machine; ne jamais lancer un script sauf si vous savez ce qu'il fait)
eval_toggle = False

# AI PART:
commande_ai = "ai"
# en: Delete all your conversations with the AI.
# fr: Supprime toutes les conversations avec l'IA.
commande_ia_clear = "suppr"
# fr: Si vous possédez Nitro entrez ici 3900, si vous ne possédez pas nitro, entrez ici 1900.
is_nitro = 3900
# fr: Identifiants et mot de passe pour la commande -ai.
# en: Email and Password for the ai command.
hug_chat_email = ""
hug_chat_password = ""
# fr: RECOMMENDé: "False"; Permet à n'importe qui d'utiliser la commande IA.
# en: RECOMMENDED: "False"; Allow everyone to use the AI command.
ai_for_all = False # True / False
# fr: langue dans laquelle l'IA dois vous répondre.
# en: Language for the AI answer.
language_ai = "english"

# fr: Commande pour transformer l'ID de l'utilisateur en DéBUT de son token (converti son ID en base 64)
# en: Command to transform the user's ID into the START of his token (convert the ID into base 64)
token_to_id = "tok"

# fr: Activé NitroSniper (True = oui et False = non)
# en: Enable NitroSniper (True = yes and False = no)
nitro_toggle = False # True / False
# fr: Salon où le Nitro sera envoyé. (il est recommendé d'entrer un salon privé (mp / dm))
# en: Channel ID for the Nitro Sniper. (recommended: an dm channel id.)
notifier_channel_id = ""
# Notifier Account
notifier_token = ""


# fr: Nom de la commande qui servira a clear ses messages. (fonctionne seulement avec votre ID)
# en: Name of the command that will clear messages. (only work with your ID)
clear_command = "clear"
#
clear_definition = "Clear messages. (Max:"
# Nombre maximum de clear ( RECOMMendée : 15 ) (PLUS LE NOMBRE EST HAUT, PLUS VOTRE COMPTE A DE CHANCE DE SE FAIRE BANNIR)
max_clear = 15

# fr: Nom de la commande QUI ENVERRA UNE PHOTO DE CHAT  (fonctionne seulement avec votre ID)
# en: Name of the command THAT WILL SEND A CAT PICTURE (work only with your ID)
cat_command = "cat"
# Description de la commande
cat_definition = "Send a cat picture."


# Nom de la seconde commande QUI ENVERRA UN FAUX NITRO (fonctionne seulement avec votre ID)
nitro_command = "fakenitro"
# Description de la commande
nitro_definition = "Send a FakeNitro"


# Nom de la quatrième commande (préféré pour raccourcir la commande d'un snipe), (fonctionne seulement avec votre ID)
snipe_command = "snipe"
# Nom de votre commande de snipe.
snipe_answer = "~iesnipe"
# Description de la commande
snipe_definition = "Snipe."



"""fr: COMMANDES PERZSONNALISéES
   en: CUSTOM COMMANDS"""

# Nom de la commande (fonctionne seulement avec votre ID)
commande_un = ""
# Réponse de la troisième commande
reponse_un = ""
# fr: Définition de la commande
un_definition =""

# Nom de la deuxième commande (fonctionne seulement avec votre ID)
commande_deux = ""
# Réponse de la deuxième commande
reponse_deux = ""
#
deux_definition =""

# Nom de la cinquième commande (fonctionne seulement avec votre ID)
commande_trois = ""
# Réponse de la cinquième commande
reponse_trois = ""
# Definition
trois_definition =""

# Nom de la quatrième commande (fonctionne seulement avec votre ID)
commande_quatre = ""
# Réponse de la quatrième commande
reponse_quatre = ""
#
quatre_definition =""

# Nom de la quatrième commande (fonctionne seulement avec votre ID)
commande_cinq = ""
# Réponse de la quatrième commande
reponse_cinq = ""
#
cinq_definition =""
