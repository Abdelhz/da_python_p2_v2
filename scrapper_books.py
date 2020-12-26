import requests
from bs4 import BeautifulSoup
import urls_mod
import folder_mod
import file_saver

path_file = folder_mod.chemin_parent() #creat parent folder's path
categories_folder = folder_mod.chemin_dossier(path_file, 'Book_to_scrap')
images_folder = folder_mod.chemin_dossier(categories_folder, 'books_images')
folder_mod.creer_dossier(categories_folder)
folder_mod.creer_dossier(images_folder)

def category_csv(list_url_categories):
    category_number = 0
    url_books_images = []
    for url in list_url_categories:
        category_number = category_number + 1
        category_number_str = str(category_number)
        
        raww_scrap_category = books_scrapper(url, category_number_str)
        
        raw_new_scrap_category = raww_scrap_category[0]
        filename_category_csv = raww_scrap_category[1]
        dictionary = raw_new_scrap_category[0]
        list_urls_img = raww_scrap_category[1]
        for list_img in list_urls_img:
            url_books_images.append(list_img)
        file_saver.create_csv(dictionary, filename_category_csv)
        
    file_saver.create_img(url_books_images, images_folder)

    #file_saver.create_img(url_books_images, images_folder)
    #saving_images(urls, titles)

def books_scrapper(urls_category, number):
    url_current = urls_category
    url_page = urls_category[:-10]
    response0 = requests.get(urls_category)
    response1 = requests.get(url_current)
    if response0.ok:
        soup0 = BeautifulSoup(response0.text, 'lxml')
        title_category = soup0.find('div', attrs={'class': 'page-header action'}).find('h1')
        title_category = str(title_category.text)
        title_category_folder = number + "_" + title_category
            
        category_folder = folder_mod.chemin_dossier(categories_folder, title_category_folder)
        filename_category_csv = folder_mod.chemin_dossier(category_folder, title_category)
        folder_mod.creer_dossier(category_folder)
    

    list_url_books = urls_mod.scrap_books_urls(response1, url_page)
    
    
    raw_scrap_category = urls_mod.scrap_book_information(list_url_books, title_category)

    return raw_scrap_category, filename_category_csv
    
