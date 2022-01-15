def runz:
    import bs4
    import requests
    
    from bs4 import BeautifulSoup as soup
    
    my_url = 'https://www.worldometers.info/coronavirus/country/india/'
    res = requests.get(my_url)
    page_html = res.text
    page_soup = soup(page_html, 'html.parser')
    
    ze=page_soup.find('span',style="color:#aaa")   
    cases=(ze.getText())

    death= page_soup.findAll('span')[5]
    deaths =(death.getText())

    recovered = page_soup.findAll('span')[6]
    recover = recovered.getText()

    print("No of cases in india :" , cases)
    print("No of death in india :" , deaths)
    print("No of recovered cases in india :" , recover)