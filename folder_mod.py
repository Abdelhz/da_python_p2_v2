import pathlib
import os

def chemin_courant(): #return current directory path
    path_current_directory = pathlib.Path(__file__).parent.absolute()
    return path_current_directory

def chemin_parent(): #return parent directory path
    path_parent_directory = os.getcwd()
    return path_parent_directory

def chemin_dossier(path_given, folder_name): #create a child directory path
    chemin_cree = os.path.join(path_given, folder_name)
    return chemin_cree

def creer_dossier(chemin_dossier): #create a directory
        os.makedirs(chemin_dossier)

