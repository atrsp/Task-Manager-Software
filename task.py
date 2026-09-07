
def read_command_line () :

def read_fichier (nom_fichier) :

def add_task () :

def change_task () :

def delete_task () :

def list_tasks () :



nom_fichier, fonction = read_command_line ()
tasks = read_fichier (nom_fichier)

if fonction == "add" :
    add_task ()

elif fonction == "change" :
    change_task ()

elif fonction == "delete" :
    delete_task ()

elif fonction == "list" :
    list_tasks ()

else :
    print ("Fonction non reconnue. Veuillez utiliser 'add', 'change', 'delete' ou 'list'.")