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

def usage():
    """Small helper to use when --help is pass
    """
    print("Usage: "+sys.argv[0]+" -h -d -your own options"+"\n")
    print("-h     --help            Display help")
    print("-c     --caller_number   Caller's phone number")

def main(argv):
    """Where the magic happen
    """
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

    print("Loading conf file")
    import configparser
    config_file = os.path.dirname(os.path.realpath(__file__))+'/freshdesk.conf'
    print (config_file)
    config = configparser.RawConfigParser()
    config.read(config_file)
    domain = config.get('freshdesk', 'domain')
    api_key = config.get('freshdesk', 'api_key')
    agent_id = int(config.get('freshdesk', 'agent_id'))

    # Do your code here
    print("Program Start")
    freshdesk_API = API(domain, api_key, version=2)
    pop_call =  freshdesk_API.cti.pop_call(caller_number,agent_id)
    print(pop_call)

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception as exception:
        print(exception)
