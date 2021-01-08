import urllib.request
from urllib.request import urlopen, HTTPError, URLError
import pandas as pd
import numpy as np
import os

def create_img(url_books_image, title_image, images_folder):
    chars = '\\:;,\'"`*{}[]()>#+-.!$?/^¨£¤µ~|@ ' #list of excluded characters
    for c in chars: #normalising file name for images
        title_image = title_image.replace(c, '_')
        title_image = title_image.replace('__', '_')
    try:
        urllib.request.urlretrieve(url_books_image, os.path.join(images_folder, os.path.basename(title_image + ".jpg"))) #saving image using its url
        print("Image : "+ title_image + " is saved", "\n" )
    except HTTPError:
        print("HTTP Error, Image not available\n")
    except URLError:
        print("URL Error, Image cant be downloaded\n")

def create_csv(data_category_csv, filename_category_csv):
    df_category = pd.DataFrame(data_category_csv) #create data frame for the csv file
    df_category.to_csv(filename_category_csv + '.csv', encoding = 'utf-8-sig') # create csv file using dataframe and name. dataframe encoded in UTF-8
