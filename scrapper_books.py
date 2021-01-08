import requests
from bs4 import BeautifulSoup
import urls_mod
import folder_mod
import file_saver

path_file = folder_mod.chemin_parent() #creat parent folder's path
categories_folder = folder_mod.chemin_dossier(path_file, 'Book_to_scrap') #create main folder's path for categories
images_folder = folder_mod.chemin_dossier(categories_folder, 'books_images') #create images folder's path
folder_mod.creer_dossier(categories_folder) #create folder
folder_mod.creer_dossier(images_folder)
url_books_imgs = [] #list of image's url
titles_imgs = [] #list of image's title

#method using the list of categories'urls to create csv files for each category :
def category_csv(list_url_categories): 
    category_number = 0
    for url in list_url_categories: #looping in list of gategories's urls
        category_number = category_number + 1
        category_number_str = str(category_number)
        #Saving books information
        raww_scrap_category = books_scrapper(url, category_number_str, url_books_imgs, titles_imgs)
        
        raw_new_scrap_category = raww_scrap_category[0]
        filename_category_csv = raww_scrap_category[1]
        dictionary = raw_new_scrap_category[0] #All information of each book of a category saved in a dictionary
        #list_urls_img = raww_scrap_category[1]
        print('\n\n')
        file_saver.create_csv(dictionary, filename_category_csv) #creating the .csv file for the current category
        print('finished saving category :' + filename_category_csv)
        print('\n\n\n')
        print('------------------------------------------')  

def category_img(): #method to save all books images of a category
    print('Saving images')
    print('\n\n\n')
    print('------------------------------------------')
    for i in range(len(url_books_imgs)):
        url_img = url_books_imgs[i]
        title_img = titles_imgs[i]
        print('\n')
        print('------------------------------------------')
        file_saver.create_img(url_img, title_img, images_folder)

def books_scrapper(urls_category, number, url_books_imgs,titles_imgs): #methodes that returnes all information of 
    url_current = urls_category
    url_page = urls_category[:-10]
    response0 = requests.get(urls_category)
    response1 = requests.get(url_current)
    if response0.ok:
        soup0 = BeautifulSoup(response0.content, 'html.parser')
        title_category = soup0.find('div', attrs={'class': 'page-header action'}).find('h1')
        title_category = str(title_category.text)
        title_category_folder = number + "_" + title_category
            
        category_folder = folder_mod.chemin_dossier(categories_folder, title_category_folder) #creating cathegory folder's path 
        filename_category_csv = folder_mod.chemin_dossier(category_folder, title_category) #creating csv file name and path
        folder_mod.creer_dossier(category_folder) #creating category folder
    

    list_url_books = urls_mod.scrap_books_urls(response1, url_page) #fetching books urls
    
    
    raw_scrap_category = urls_mod.scrap_book_information(list_url_books, title_category, url_books_imgs, titles_imgs) #collecting information for each book of the given list_url_books

    return raw_scrap_category, filename_category_csv #returning content for csv file and csv file name
    
