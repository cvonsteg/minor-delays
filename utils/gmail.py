from smtplib import SMTP 
import os

class Gmail(SMTP):
    def __init__(self):
        super().__init__('smtp.gmail.com', 587)

    def send(self, msg):
        self.ehlo_or_helo_if_needed()
        self.login(os.environ['TUBE_FROM'], os.environ['PWD'])
        self.sendmail(os.environ['TUBE_FROM'], os.environ['TUBE_TO'], msg)
        self.quit()
    
