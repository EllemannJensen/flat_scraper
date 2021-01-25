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
















################################                               https://stackoverflow.com/questions/48095700/web-scraping-back-in-stock-notification









#if available == True:
    #send e-mail alert
    #print to console e-mail addresses where the alert was sent.
#else:
    #print to console that the food is not available.



# wann laden? Einmal am tag um 9h?


# Email schicken wenn event




#print(results_teaser[0].text) 



#results_teaser[0:20] 
#print(results_teaser.text)
#So you can extract text directly from it:

#for item in all:
#    print(item.text)



#for result_teaser in result_teasers:
    #teaser_text = tagresult_teaser.find("h3 teaser-h").text
    #print(teaser_text)

















#results_teaser = soup.findAll('div', {'class': 'teaser3 teaser3--listing teaser-simple--boxed'})

#results = soup.find("div", {"class": "teaser-content cf media__body"})
# results = soup.find(id='searchSubmitBtn')      #('h3', string='teaser3 teaser3--listing teaser-simple--boxed') # teaser3 teaser3--listing teaser-simple--boxed

             #   <div class="teaser-content cf media__body">
            # <h3 class="h3 teaser-h">1 1/2 Zimmer Seniorenwohnung in Lohb...</h3>
           
                                                                
#print(results_teaser)  

#print(results_teaser.prettify())


#flat_elems = results.find_all("section", class_='g two-thirds phone-one-whole main-content main-content-right')

#print(falt_elems)

 # <h3 class="h3 teaser-h"
#for flat_elem in flat_elems:
  #  print(flat_elem, end= '\n'*2)


############################################ versuch mit read_html.... problem jason

# how to scrap HTML with BS and Pandas

# all the list on the webpage in dfs
# URL = 'https://www.saga.hamburg/immobiliensuche'

# dfs = pd.read_html(URL)

# select df you whant to use, when you know which one you need

# df = dfs[4]

# list by columns names

#for df in dfs:
   # if df.columns == ['#', 'Team', 'r']:
       # target = df
       # break


# page = requests.get(URL)
#soup = BeautifulSoup(page.text, 'html.parser')

##dfs = pd.read_html(page.text)

#df = df[1]

#print(dfs)