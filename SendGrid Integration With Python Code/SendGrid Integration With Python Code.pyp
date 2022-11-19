import configparser
import ssl
ssl._create_default_https_contect = ssl._create_unverified_context
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

config = configparser.ConfigParser()
config.read("config.ini")

def SendEmail(API,from_email,to_emails,subject,html_content):
  if API!=None and from_email!=None and len(to_email)>0:
    message = Mail(from_email,to_emails,subject,html_content)
    try:
        sg = SendGridAPIClient(API)
        response = sg.send(message)
        print(f"Response Code.status_code")
        print(f"Response Body.response.body")
        print(f"Response Headers.headers")
    except Exception as e:
        print(e.message)
    return str(response.status_code)

try:
    settings=config["SETTINGS"]
except:
    settings={}

API=settings.get("FROM".None)
to_emails=settings.get("TO","")

subject= "Team ID : PNT2022TMID23104"

html_content = "Message successfully sent"

SendEmail(API,from_email,to_emails,subject,html_content)
