from logging import debug
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
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class Google_Authorizate():
    def  __init__(self, creds, site_api, storage, code):
        self.storage = storage
        self.code = code

    def authorize_creds(self, creds):
        # Variable parameter that controls the set of resources that the access token permits.
        SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']
    
        # Path to client_secrets.json file
        CLIENT_SECRETS_PATH = creds
    
        # Create a parser to be able to open browser for Authorization
        parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            parents=[tools.argparser])
        flags = parser.parse_args(['--noauth_local_webserver'])
    
        flow = client.flow_from_clientsecrets(
            CLIENT_SECRETS_PATH, scope = SCOPES,
            message = tools.message_if_missing(CLIENT_SECRETS_PATH))
    
        # Prepare credentials and authorize HTTP
        # If they exist, get them from the storage object
        # credentials will get written back to a file.
        storage = self.storage
        storage = file.Storage(storage)
        credentials = storage.get()
    
        # If authenticated credentials don't exist, open Browser to authenticate
        if credentials is None or credentials.invalid:
            print("")
            #credentials = tools.run_flow(flow, storage, flags)
            CLIENT_ID = '124538964907-7n68c101qtdml0v8g3bgdacus0ju4bhf.apps.googleusercontent.com'
            CLIENT_SECRET = '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'

            # Check https://developers.google.com/webmaster-tools/v1/ for all available scopes
            OAUTH_SCOPE = 'https://www.googleapis.com/auth/webmasters.readonly'

            # Redirect URI for installed apps
            REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

            # Run through the OAuth flow and retrieve credentials
            flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
            
            code = self.code
            storage = self.storage
            storage = file.Storage(storage)
            codes = code.strip()
            print(codes)
            print(storage)
            credentials = flow.step2_exchange(codes)

            
            
            #print(credentials)


            storage.put(credentials)
            credentials.set_store(storage)
            print('Authentication successful.')


        http = credentials.authorize(http=httplib2.Http())
        webmasters_service = build('searchconsole', 'v1', http=http)
        return webmasters_service

    def domains_founder(self, service, property_uri, request): 
        return service.sites().list().execute()

    def execute_request(self, service, property_uri, request): 
        return service.searchanalytics().query(siteUrl=property_uri, body=request).execute()



class Google_Authorizate_sec():
    def  __init__(self, creds, site_api, storage):
        self.storage = storage


    def authorize_creds(self, creds):
        # Variable parameter that controls the set of resources that the access token permits.
        SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']
    
        # Path to client_secrets.json file
        CLIENT_SECRETS_PATH = creds
    
        # Create a parser to be able to open browser for Authorization
        parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            parents=[tools.argparser])
        flags = parser.parse_args(['--noauth_local_webserver'])
    
        flow = client.flow_from_clientsecrets(
            CLIENT_SECRETS_PATH, scope = SCOPES,
            message = tools.message_if_missing(CLIENT_SECRETS_PATH))
    
        # Prepare credentials and authorize HTTP
        # If they exist, get them from the storage object
        # credentials will get written back to a file.
        storage = self.storage
        storage = file.Storage(storage)
        credentials = storage.get()


        http = credentials.authorize(http=httplib2.Http())
        webmasters_service = build('searchconsole', 'v1', http=http)
        return webmasters_service

    def domains_founder(self, service, property_uri, request): 
        return service.sites().list().execute()

    def execute_request(self, service, property_uri, request): 
        return service.searchanalytics().query(siteUrl=property_uri, body=request).execute()














