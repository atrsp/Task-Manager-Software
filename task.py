import argparse


def read_command_line () :

def read_file (filename) :

def add_task (id_str, description) :
    file_content = read_file(filename)
    if id_str in file_content.keys():
        raise ValueError("choosen id is already taken")
    with open('mon_file','a') as f :
        f.write(str(id_str)+', '+ description+'\n')
        f.close()
        return id

def modify_task (id_str, new_description) :
    file_content = read_file(filename)
    if id_str not in file_content:
        return "erreur, id non trouvé"
    file_content[id_str]=new_description
    with open('mon_file','w') as f :
        for elt in file_content :
            f.write(str(elt)+', '+ file_content[elt] + '\n')



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