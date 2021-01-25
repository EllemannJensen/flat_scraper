import smtplib

server = smtplib.SMTP('smtp-mail.outlook.com', 587) # email server      
#server.starttls()
#print(server.starttls())
server.ehlo() # greeting to server and starting connetion process'
print(server.ehlo())
server.starttls() # encryption for connection puts sMTP in TLS mode
# print(server.starttls())
server.login('email@outlook.de', 'Password')
server.sendmail('email@outlook.de', 'email@outlook.de', 'Subject: \n*eigentlich das aus h3 einfühen')
server.quit()