
def read_command_line () :

def read_file (nom_file) :

def add_task (description, id) :
    file_content = read_file(mon_file)
    if id in file_content.keys():
        raise ValueError("choosen id is already taken")
    with open('mon_file','w') as f :
        f.write(id, description)
        return id

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