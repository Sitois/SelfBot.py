debug_mode = False # (beta)
"""CONFIG  GENERAL COMMANDES"""
# Token du compte pour les commandes.
commands_token = ""
# Votre ID du compte qui éxécutera les commandes.
account_id = [""]
# ID du salon par défaut (vous pourrez ajouter d'autre salon en fesant: la commande en-dessous et l'id du salon. )
CHANNEL_ID = "" # Laisser vide pour avoir la demande au démarrage.
add_channel = "add"
del_channel = "del"
list_channel = "list"
# Prefix des commandes
prefix = "-"
#
commande_aled = "danger"


"""CONFIG COMMANDES"""
# fr: Nom de la commande QUI ENVERRA LE MESSAGE D'AIDE  (fonctionne seulement avec votre ID)
# en: Name of the command THAT WILL SEND THE HELP (work only with your ID)
commande_help = "help"
# Description de la commande
help_definition = "Send the help of the SelfBot."

#
eval_command = "eval"
# DO NOT ENTER "True" unless you are aware of the risks (eval command allows you to execute arbitrary code)
eval_toggle = False

# ai
commande_ai = "ai"
#
commande_ia_clear = "suppr"
# fr: Si vous possédez Nitro entrez ici 3900, si vous ne possédez pas nitro, entrez ici 1900.
is_nitro = 3900
# fr: Identifiants et mot de passe pour la commande -ai.
hug_chat_email = ""
hug_chat_password = ""
#
ai_for_all = False # True / False
#
language_ai = "english"

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
