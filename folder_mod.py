import pathlib
import os

def chemin_courant(): #return current directory path
    path_current_directory = pathlib.Path(__file__).parent.absolute()
    return path_current_directory

def chemin_parent(): #return current directory path
    path_parent_directory = os.getcwd()
    return path_parent_directory

def chemin_dossier(path_given, folder_name):
    chemin_cree = os.path.join(path_given, folder_name)
    return chemin_cree

def creer_dossier(chemin_dossier):
    if not os.path.exists(chemin_dossier):
        os.makedirs(chemin_dossier)

path1 = pathlib.Path(__file__).parent.absolute()
path = os.getcwd()
path2 = os.path.abspath(os.path.join(path, os.pardir))
print("\n\n")
print("Directory", path1) 
print("\n\n")
print("Current Directory", path) 
print("\n\n")
print("Directory", path2)
print("\n\n")


"""
dossier_category = os.path.join(path_file, 'dossier_category')
dossier_images = os.path.join(dossier_category, 'Images_books')

if not os.path.exists(dossier_category):
    os.makedirs(dossier_category)

if not os.path.exists(dossier_images):
    os.makedirs(dossier_images)
#print(dossier_category)


dossier_sous_categorie = os.path.join(dossier_category, title_category_folder)

filename_category_csv = os.path.join(dossier_sous_categorie, title_category)

dossier_images_sous_categorie = os.path.join(dossier_sous_categorie, 'images_livres')
    if not os.path.exists(dossier_sous_categorie):
        os.makedirs(dossier_sous_categorie)
    if not os.path.exists(dossier_images_sous_categorie):
        os.makedirs(dossier_images_sous_categorie)
"""