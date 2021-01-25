import requests
from bs4 import BeautifulSoup
import pandas as pd

import re
import time
import smtplib
from datetime import datetime 


URL = 'https://www.saga.hamburg/immobiliensuche'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results_teaser = soup.find_all("h3", {'class': 'h3 teaser-h'}, text = True)
if not results_teaser:
    print('Nothing here')
else:
    for item in results_teaser: # print(item.text.strip())
        flats = item.text.strip()
        print(flats)
        
####################

now = datetime.now()
server = smtplib.SMTP('smtp-mail.outlook.com', 587) # email server      
server.ehlo()

#server.starttls()
#server.login(address,password) # login ?? mit imput oder ??? https://pypi.org/project/keyring/     
   

#now = dattime.now()
















