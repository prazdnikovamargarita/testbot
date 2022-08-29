from logging import debug
from httplib2 import RETRIES
import telebot
from requests import get
from telebot import types
from oauth2client.transport import request
import pandas as pd
import datetime
from datetime import date, timedelta
import httplib2
from googleapiclient.discovery import build
from oauth2client.client import OAuth2WebServerFlow
from collections import defaultdict
from dateutil import relativedelta
import argparse
from oauth2client import client
from oauth2client import file
from oauth2client import tools
import re
import os
from urllib.parse import urlparse
import telebot
from telebot import types
import requests
import numpy as np
import math
import schedule
import time

from telegram import Bot
from telegram import Update
from telegram.utils.request import Request
from datetime import datetime, timedelta


from telegram.ext import Updater
from telegram.ext import CommandHandler
from google_authiorasation  import Google_Authorizate, Google_Authorizate_sec


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from anticaptchaofficial.recaptchav2proxyless import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from webdriver_manager.chrome import ChromeDriverManager

import schedule
import telebot
from threading import Thread
from time import sleep
import os
from selenium import webdriver
import geckodriver_autoinstaller
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

site_api = 'https://www.googleapis.com/webmasters/v3/sites'   
creds = './client_secret_124538964907-7n68c101qtdml0v8g3bgdacus0ju4bhf.apps.googleusercontent.com.json'
bot = telebot.TeleBot('5617537541:AAGVQD7GFUl0-Gk3kjicAgzBQ6NAiYrjM0A')


storage="authorizedcreds.dat"
storage2="authorizedcreds-second.dat"
markup_choose_storage =  types.ReplyKeyboardMarkup(resize_keyboard=True)
choose_storage_button = types.KeyboardButton("seoteamessay@gmail.com")
choose_storage_button2 = types.KeyboardButton("eanna9790@gmail.com")
markup_choose_storage.row(choose_storage_button, choose_storage_button2)



markup_choose_period =  types.ReplyKeyboardMarkup(resize_keyboard=True)
choose_period_button = types.KeyboardButton("for 3 days")
choose_period_button2 = types.KeyboardButton("for 1 week")
choose_period_button5 =  types.KeyboardButton("for last 24 hours")
choose_period_button4 =  types.KeyboardButton("choose date")
markup_choose_period.row(choose_period_button5, choose_period_button)
markup_choose_period.row(choose_period_button2, choose_period_button4)

