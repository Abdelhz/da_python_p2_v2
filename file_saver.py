import urllib.request
from urllib.request import urlopen, HTTPError, URLError
import pandas as pd
import numpy as np
import os

chars = '\\:;,\'"`*{}[]()>#+-.!$?/^¨£¤µ~|@ '
def create_img(url_books_image, title_image, images_folder):
    # url_img = url_books_images[0]
    # title_img = url_books_images[1]
    for c in chars:
        title_img = title_image.replace(c, '_')
    try:
        urllib.request.urlretrieve(url_books_image, os.path.join(images_folder, os.path.basename(title_img + ".jpg")))
        print("Image : "+ title_img + " is saved", "\n" )
    except HTTPError:
        print("HTTP Error, Image not available\n")
    except URLError:
        print("URL Error, Image cant be downloaded\n")

def create_csv(data_category_csv, filename_category_csv):
    df_category = pd.DataFrame(data_category_csv)
    df_category.to_csv(filename_category_csv + '.csv', encoding = 'utf-8') #encoder en UTF-8
