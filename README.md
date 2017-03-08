# 3cx-cti-macos

A library for the [Freshdesk](http://freshdesk.com/) helpdesk cti system for Python 3.

Support for the v2 API CTI

## Installation

The easiest way to install is inside a virtualenv and with our python-freshdesk fork (https://github.com/alkivi-sas/python-freshdesk)

1. Create the virtualenv (Python 3!) and activate it:

    ```
    $ git clone https://github.com/alkivi-sas/3cx-freshdesk-macos
    $ virtualenv -p python3 3cx-freshdesk-macos
    $ cd 3cx-freshdesk-macos
    $ source bin/activate
    $ git clone https://github.com/alkivi-sas/python-freshdesk.git
    $ pip install ./python-freshdesk
    ```

2. Change the conf file :

    ```
    $ vim freshdesk-example.conf
    ```
Change values with your platform, you can have your caller ID at https://domain.freshdesk.com/agents, you click on the agent and you 'll have the id in the url

    ```
    $ mv freshdesk-example.conf freshdesk.conf
    ```

## Usage
1. From a terminal :

   ```
   $ ./3cx_to_fresdesk.py -c 0836656565
   ```
2. from 3CX softphone on macOS :
Go to parameter --> Advanced --> Enable execute program on inbound calls and put
    
Path :
   ```
   /Users/myuser/path_of_3cx-freshdesk-macos/bin/python3 /Users/myuser/path_of_3cx-freshdesk-macos/3cx_to_fresdesk.py -c 0836656565
   ```     
Parameters :
   ```
   -c %CallerNumber%
   ```  
