import urls_mod
import scrapper_books


url = 'http://books.toscrape.com/index.html'

print('fetching categories urls')
url_categories_list = urls_mod.scrap_category_urls(url) #Creating a list containing the url of each of the 50 categories
print('list of categories urls created')

print('\n\n\n')
print('------------------------------------------')
print('creating csv files')
print('\n\n\n')
print('------------------------------------------')
scrapper_books.category_csv(url_categories_list) #creating csv files for each category

print('saving images')
print('\n\n\n')
print('------------------------------------------')
scrapper_books.category_img() #saving image of each book