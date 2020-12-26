import urllib.request
from urllib.request import urlopen, HTTPError, URLError
import pandas as pd
import numpy as np
import os

chars = '\\:;,\'"`*{}[]()>#+-.!$?/^¨£¤µ~|@ '
def create_img(data_img, images_folder):
    for data in data_img:
        url_img = data[0]
        title_img = data[1]
        for c in chars:
            title_img = title_img.replace(c, '_')
        try:
            urllib.request.urlretrieve(url_img, os.path.join(images_folder, os.path.basename(title_img + ".jpg")))
            print("Image : "+ title_img + " is saved", "\n" )
        except HTTPError:
            print("HTTP Error, Image not available\n")
        except URLError:
            print("URL Error, Image cant be downloaded\n")

def create_csv(data_category_csv, filename_category_csv):
    df_category = pd.DataFrame(data_category_csv)
    df_category.to_csv(filename_category_csv + '.csv', encoding = 'utf-8') #encoder en UTF-8
