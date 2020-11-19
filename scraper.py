from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.macrotrends.net/countries/BGD/bangladesh/life-expectancy').text
soup = BeautifulSoup(source, 'html.parser')

csv_file = open('healthdata.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Country', 'Life Expectancy'])

art = soup.find('div', class_='main_content_container container-fluid')
art_div = art.find('div', class_='col-xs-5',
                   style="background-color:#fff; margin: 30px 0px 30px 0px; padding:0px 0px 0px 0px;")
tbody = art_div.table.tbody

for tr in tbody.find_all('tr'):
    try:

        my_list = tr.text.split('\n')
        country = my_list[1]
        life_expectancy = my_list[2]
        # For better visualization in the bar charts, I have omitted some of the countries.
        csv_writer.writerow([country, life_expectancy])
    except Exception as e:
        my_list = None
        country = None
        life_expectancy = None
csv_file.close()
