
def read_command_line () :

def read_file (nom_file) :

def add_task () :

def modify_task () :

def rm_task () :

def list_tasks () :



nom_file, fonction = read_command_line ()
tasks = read_file (nom_file)

if fonction == "add" :
    add_task ()

elif fonction == "modify" :
    modify_task ()

elif fonction == "rm" :
    rm_task ()

elif fonction == "show" :
    list_tasks ()

else :
    print ("Fonction non reconnue. Veuillez utiliser 'add', 'modify', 'rm' ou 'show'.")