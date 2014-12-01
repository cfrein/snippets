"""
Who:    Claus Frein
Why:    Collection of small python-snippets
When:   20120131: Created
"""

import smtplib
from email.mime.text import MIMEText

def send_mail(recipients, subject="NoSubject", body="NoBody", sender="unknown@rzvnet.de"):
    """send an email

    requires at least one or more recipients, seperated by a comma
    """
    recipient_list  = recipients.split(",")
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients

    server = smtplib.SMTP('smtp')
#    server.set_debuglevel(1)
    server.sendmail(sender, recipient_list, msg.as_string())
    server.quit()

