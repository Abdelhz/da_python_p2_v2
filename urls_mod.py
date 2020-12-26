import requests
from bs4 import BeautifulSoup



def scrap_category_urls(url_book2scrap):
    response = requests.get(url_book2scrap)
    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        lists = soup.find('ul', attrs={'class': 'nav nav-list'}).findAll('a')
        list_categories = []
        for data in lists:
            url_category = data.attrs["href"]
            list_categories.append("http://books.toscrape.com/" + url_category)
    #del title_categories[0]
    del list_categories[0]
    
    return list_categories



def scrap_books_urls(response, url_page):
    list_urls_books = []
    while response.ok:
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
    return list_urls_books_2

def scrap_book_information(list_urls_books, title_category):
    titres = []
    p_d = []
    upc_s = []
    prix_tax = []
    prix_notax = []
    num_avail = []
    review_rate = []
    p_d_urls = []
    imgs_urls = []
    ii = 0
    for url_books in list_urls_books:
        response2 = requests.get(url_books)
        if response2.ok:
            soup = BeautifulSoup(response2.text, 'lxml')
            product_page_url = url_books
            p_d_urls.append(product_page_url)
            titre = soup.find('h1')
            titre = str(titre.text)
            titres.append(titre)
                
            ii = ii + 1
            ii1 = str(ii)
            print('II ='+ ii1)
            article = soup.find('article', attrs={'class': 'product_page'})
            print('\nits here\n')
            ps = article.findAll('p')
            product_description = ps[3]
            product_description = str(product_description.text)
                
            p_d.append(product_description)

            table = soup.find('table', attrs={'class': 'table table-striped'})
            tds = table.findAll('td')
                
            universal_product_code = tds[0]
            universal_product_code = str(universal_product_code.text)
                
            upc_s.append(universal_product_code)

            price_including_tax = tds[3].string
            price_including_tax = price_including_tax[2 :]
            prix_tax.append(price_including_tax)
                
            price_excluding_tax = tds[2].string
            price_excluding_tax = price_excluding_tax[2 :]
            prix_notax.append(price_excluding_tax)
                
            number_available = tds[5]
            number_available = str(number_available.text)
                
            num_avail.append(number_available)
                
            review_rating = tds[6]
            review_rating = str(review_rating.text)

            review_rate.append(review_rating)
            
            imgs = soup.find('div', attrs={'class': 'item active'}).find('img')
            img1 = imgs.attrs["src"]
            imgs_url = img1.replace('../..', 'http://books.toscrape.com')
                
            book_img_title = title_category + '_' + titre
            img_url_title = [imgs_url, book_img_title]
            imgs_urls.append(img_url_title)
            #titre_image_livre = titre_image_livre.replace('/[&\/\\#,+()$~%.'":*?<>{}]/g', '_')
            data_book_csv = [titre, product_description,universal_product_code, price_including_tax, price_excluding_tax, number_available, review_rating, product_page_url]
    data_category = {'Titre' : titres, 'Product description' : p_d, 'Universal product code' : upc_s, 'Price including tax in £' : prix_tax, 'Price excluding tax in £' : prix_notax, 'Number available' : num_avail, 'Review rating' : review_rate, 'Product page url' : p_d_urls, 'Images Urls' : imgs_urls}
    
    raw_data_category = [data_category, imgs_urls]
    return raw_data_category  


