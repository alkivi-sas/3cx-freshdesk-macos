#!/usr/bin/env python
# -*-coding:utf-8 -*

"""
Script to do CTI with 3CX and Freshdesk on macOS
"""

import sys
import logging
import requests
import json
import os
from freshdesk.api import API
import subprocess

def usage():
    """Small helper to use when --help is pass
    """
    print("Usage: "+sys.argv[0]+" -h -d -your own options"+"\n")
    print("-h     --help            Display help")
    print("-c     --caller_number   Caller's phone number")

def main(argv):
    """Where the magic happen
    """
    logging.basicConfig(filename='/var/log/3cx-freshdesk-macos.log',level=logging.DEBUG)

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
    api_key = config.get('freshdesk', 'api_key')
    agent_id = int(config.get('freshdesk', 'agent_id'))

    postscript = None
    if config.has_option('freshdesk', 'postscript'):
        postscript = config.get('freshdesk', 'postscript')

    if len(caller_number) < 4:
        logging.info('Exiting because internal')
        exit(0)

    if caller_number == 'MakeCall':
        logging.info('Exiting because MakeCall')
        exit(0)

    # Do your code here
    logging.info("Program Start")
    freshdesk_API = API(domain, api_key, version=2)
    pop_call =  freshdesk_API.cti.pop_call(caller_number,agent_id)
    logging.info(pop_call)

    #call to wiki
    if postscript:
        dirname = os.path.dirname(os.path.abspath(__file__))
        python_path = sys.executable
        logging.info(f"Python Path : {python_path}")
        logging.info(f"Dirname : {dirname}")
        postscript_path = os.path.join(dirname,postscript)
        subprocess.call([python_path,postscript_path,"-c","{}".format(caller_number)])



if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception as exception:
        print(exception)
