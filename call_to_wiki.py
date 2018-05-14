#!/usr/bin/env python
# -*-coding:utf-8 -*

"""
Script to get Company name from a phone number based on freshdesk contacts and open wiki
"""

import sys
import logging
import requests
import json
import os
from freshdesk.api import API
import urllib.parse
import webbrowser

def usage():
    """Small helper to use when --help is pass
    """
    print("Usage: "+sys.argv[0]+" -h -d -your own options"+"\n")
    print("-h     --help            Display help")
    print("-c     --caller_number   Caller's phone number")

def main(argv):
    """Where the magic happen
    """
    logging.basicConfig(filename='/var/log/call_to_wiki.log',level=logging.DEBUG)

    import getopt
    # initiate that opt use
    caller_number = None

    # Variable that opt use
    try:
        opts, dummy_args = getopt.getopt(argv, "hdc:",
                ["help", "caller_number=", 'debug'])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-c", "--caller_number"):
            caller_number = arg
            logging.info("Caller Number :{}".format(caller_number))

    logging.info("Loading conf file")
    import configparser
    config_file = os.path.dirname(os.path.realpath(__file__))+'/freshdesk.conf'
    logging.info(config_file)
    config = configparser.RawConfigParser()
    config.read(config_file)
    domain = config.get('freshdesk', 'domain')
    wiki_url = config.get('freshdesk', 'wiki_url')
    api_key = config.get('freshdesk', 'api_key')
    freshdesk_API = API(domain, api_key, version=2)

    # Do your code here
    logging.info("Program Start")
    logging.info("Search Contact")
    search_query = "\"mobile:%27{}%27\"".format(urllib.parse.quote_plus(caller_number))
    logging.info("Search Contact Query : {}".format(search_query))
    contacts = freshdesk_API.contacts.search_contact(search_query)
    if len(contacts['results']) > 0:
        if contacts['results'][0]['company_id']:
            first_contact_company_id =  contacts['results'][0]['company_id']
            logging.info("Company ID : {}".format(first_contact_company_id))
            logging.info("Search Company Name")
            company = freshdesk_API.companies.get_company(first_contact_company_id)
            logging.info(f"Company Name : {company}")

            url = wiki_url + str(company)
            # MacOS
            chrome_path = "open -a /Applications/Google\ Chrome.app %s"
            webbrowser.get(chrome_path).open(url)

        else:
            logging.info("This contact doesn't have a company")
    else:
        logging.info("No contact with this number")



if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception as exception:
        print(exception)
