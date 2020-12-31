import requests
from bs4 import BeautifulSoup



def scrap_category_urls(url_book2scrap): #methode to create the list of categories urls
    response = requests.get(url_book2scrap)
    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        lists = soup.find('ul', attrs={'class': 'nav nav-list'}).findAll('a')
        list_categories = []
        for data in lists:
            url_category = data.attrs["href"]
            list_categories.append("http://books.toscrape.com/" + url_category)
    del list_categories[0]
    
    return list_categories #returning the list of urls of the categories



def scrap_books_urls(response, url_page): #methode to create the list of books urls of a category
    list_urls_books = []
    while response.ok: #loop used to switch pages in a category
        soup1 = BeautifulSoup(response.text, 'lxml')
        lists2 = soup1.find('ol', attrs={'class': 'row'}).findAll('a')
        for data2 in lists2:
            url_books = data2.attrs["href"]
            url_books = "http://books.toscrape.com/catalogue/" + url_books[9:]
            list_urls_books.append(url_books)
            
        next_p = soup1.find('li', attrs={'class': 'next'})
        
        if not next_p == None:
            nextpp = next_p.find('a').attrs['href']
            url_current = url_page + nextpp
            response = requests.get(url_current)
        else:
            break
    list_urls_books_2 = list_urls_books[::2]
    return list_urls_books_2 #returning a list of ulrs for each book of a category

def scrap_book_information(list_urls_books, title_category,url_books_imgs,titles_imgs): #method that collect information for each book from a list of urls
    titres = []
    p_d = []
    upc_s = []
    prix_tax = []
    prix_notax = []
    num_avail = []
    review_rate = []
    p_d_urls = []
    imgs_urls = []
    categories = []
    ii = 0
    for url_books in list_urls_books:
        response2 = requests.get(url_books)
        if response2.ok:
            soup = BeautifulSoup(response2.text, 'lxml')
            product_page_url = url_books
            p_d_urls.append(product_page_url)
            titre = soup.find('h1')
            titre = str(titre.text)
            titres.append(titre) #saving titles
                
            ii = ii + 1
            ii1 = str(ii)
            print('II ='+ ii1)
            article = soup.find('article', attrs={'class': 'product_page'})
            print('\nits here\n')
            ps = article.findAll('p')

            product_description = ps[3]
            product_description = str(product_description.text)   
            p_d.append(product_description) #saving product description

            table = soup.find('table', attrs={'class': 'table table-striped'})
            tds = table.findAll('td')
                
            universal_product_code = tds[0]
            universal_product_code = str(universal_product_code.text)
            upc_s.append(universal_product_code) #saving upc

            price_including_tax = tds[3].string
            price_including_tax = price_including_tax[2 :]
            prix_tax.append(price_including_tax) #saving including taxes
                
            price_excluding_tax = tds[2].string
            price_excluding_tax = price_excluding_tax[2 :]
            prix_notax.append(price_excluding_tax) #saving price excluding taxes
                
            number_available = tds[5]
            number_available = str(number_available.text) 
            num_avail.append(number_available) #saving available number
                
            review_rating = tds[6]
            review_rating = str(review_rating.text)
            review_rate.append(review_rating) #saving review rating

            category = title_category
            categories.append(category)

            imgs = soup.find('div', attrs={'class': 'item active'}).find('img')
            img1 = imgs.attrs["src"]
            imgs_url = img1.replace('../..', 'http://books.toscrape.com')
                
            book_img_title = title_category + '_' + ii1 + '_' + titre #creating image title
            
            imgs_urls.append(imgs_url)
            url_books_imgs.append(imgs_url) #saving image url
            titles_imgs.append(book_img_title) #saving image title
    #creating a dictionary that contains books information
    data_category = {'Titre' : titres, 'Product description' : p_d, 'Universal product code' : upc_s, 'Price including tax in £' : prix_tax, 'Price excluding tax in £' : prix_notax, 'Number available' : num_avail, 'Category' : categories, 'Review rating' : review_rate, 'Product page url' : p_d_urls, 'Images Urls' : imgs_urls}
    
    raw_data_category = [data_category, imgs_urls]
    return raw_data_category  #returning dictionary and images urls


