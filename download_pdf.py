import pandas as pd
from urllib import request

urls = pd.read_csv('links/mar_2009.csv')

for ind in urls.index:
    tail = urls["link_pdf"][ind]
    name = urls["reg_num"][ind]
    url_final = 'https://www.registroficial.gob.ec' + str(tail)
    path = "pdf/2009/mar_2009/" + str(name) + '.pdf'
    request.urlretrieve(url_final, str(path))
    print('Processing ' + str(ind+1) + ' out of ' + str(len(urls)))

#scrapy runspider scraping_pdf_download.py -o dic_2007.csv -t csv