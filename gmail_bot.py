import smtplib
import os
from os import getenv
from dotenv import load_dotenv
from dotenv import find_dotenv

project_folder = os.path.expanduser("F:\Zain's folder\python\Auto gmail bot")
load_dotenv(os.path.join(project_folder, 'gmail_bot.env'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login(getenv('ADDRESS'), getenv('PASSWORD'))

server.sendmail(getenv('ADDRESS'), 'zazwolf77@gmail.com', 'The bot is working')