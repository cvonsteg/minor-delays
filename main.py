import sys
import os
from smtplib import SMTP

from tubes.tfl import TFL

def main():
    TUBES = [tube for tube in sys.argv[1:] if tube is not None]
    print(" --- Loading TFL class --- ")
    tfl = TFL(TUBES)
    SUBJECT='Your Morning Tube Status'
    TUBE_DICT=str(tfl.status_dict())
    MSG=f'Subject: {SUBJECT}\n\n{TUBE_DICT}'

    print(" --- Loading GMAIL server --- ")
    gmail = SMTP('smtp.gmail.com', 587)
    gmail.starttls()
    gmail.login(os.environ['TUBE_FROM'], os.environ['PASS'])

    print(" --- Sending Email --- ")
    gmail.sendmail(from_addr=os.environ['TUBE_FROM'],
                   to_addrs=os.environ['TUBE_TO'],
                   msg=MSG)
    gmail.quit()
    print(" --- Email Sent --- ")


if __name__ == "__main__":
    main()
