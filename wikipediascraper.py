import requests, bs4

covid_data = requests.get("https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory")
# print(covid_data.content)
soup = bs4.BeautifulSoup(markup= covid_data.content, features="html.parser" )
covid_table = soup.find_all(["table",{"class":"wikitable plainrowheaders sortable jquery-tablesorter"}])
# countries = soup.find_all(["th",{"class":"covid-country-narrow-on-mobile headerSort"}])
# print(countries)
# cases = soup.find_all(["th",{"class":"headerSort"}])

rows = soup.find_all("tr")

data = []
for i,item in enumerate(rows):
    
    if i == 0:
        
        data.append(item.text.strip().split("\n")[:13])
        
    else:
        data.append(item.text.strip().split("\n")[:12])
print(data)