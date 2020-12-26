import urls_module
import scrapper_books


url = 'http://books.toscrape.com/index.html'

url_categories_list = urls_module.scrap_category_urls(url) #Creating a list containing the url of each of the 50 categories

print("---------------------------------------", "\n\n\n")
print(*url_categories_list, sep = "\n")
print("---------------------------------------", "\n\n\n")

scrapper_books.category_csv(url_categories_list)
