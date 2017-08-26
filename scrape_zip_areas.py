from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

if __name__ == "__main__":

    r = requests.get("http://www.city-data.com/zipmaps/New-York-New-York.html")

    data = r.text
    soup = BeautifulSoup(data, 'html.parser')

    # # get all zip codes
    # for link in soup.find_all('strong'):
    #     if link.find(text=re.compile('Zip code')):
    #         print(link.text.split('code ')[1].split(' ')[0])
    #
    # # get all areas
    # for link in soup.find_all('b'):
    #     if link.find(text=re.compile('Land area:')):
    #         print(link.nextSibling)

    zips = []
    areas = []
    for link in soup.find_all(class_='zip data-block'):
        text = link.text
        zipc = text.split('Zip code ')[1].split(' ')[0]
        if 'Land area' in text:
            area = text.split('Land area: ')[1].split(' sq.')[0]
            zips.append(zipc)
            areas.append(area)

    df = pd.DataFrame()
    df['zip_code'] = zips
    df['area'] = areas

    df.to_csv('~/Downloads/zips.csv', index=False)
