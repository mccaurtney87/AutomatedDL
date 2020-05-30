import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


sender_addr = 'yourmail.com'
sender_pass = '********'
receiver_addr = 'rmail.com'


message_body = "Dear Developer your Model has been trained successfully with desired accuracy.Kudos to your work!"
message = MIMEMultipart()
message['From'] = sender_addr
message['To'] = receiver_addr
message['Subject'] = 'Regarding successfully trained model'



message.attach(MIMEText(message_body, 'Plain'))

session = smtplib.SMTP('smtp.gmail.com', 25)
session.starttls()
session.login(sender_addr, sender_pass)
text = message.as_string()
session.sendmail(sender_addr, receiver_addr, text)
session.quit()

print ('Mail Sent')