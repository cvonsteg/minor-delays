import smtplib
import os


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(os.environ['TUBE_FROM'], os.environ['PWD'])

msg = 'tester one, two'
server.sendmail(os.environ['TUBE_FROM'], os.environ['TUBE_TO'], msg)
server.quit()