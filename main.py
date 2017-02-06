# Imports
import os
import jinja2
import webapp2
import logging
import json
import urllib

# this is used for constructing URLs to google's APIS
from googleapiclient.discovery import build

# This uses discovery to create an object that can talk to the 
# fusion tables API using the developer key
service = build('fusiontables', 'v1', developerKey=API_KEY)
