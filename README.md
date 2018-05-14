# 3cx-cti-macos

A library for the [Freshdesk](http://freshdesk.com/) helpdesk cti system for Python 3.

Support for the v2 API CTI

## On the freshdesk platform
You have to be sure that the application 'CTI' has been installed on your platform

## Installation

The easiest way to install is inside a virtualenv and with our python-freshdesk fork (https://github.com/alkivi-sas/python-freshdesk)

1. If you don't have its already, Install Brew, Python3 and Pipenv

First, Install X-Code from the app store

    ```
    $ xcode-select --install
    $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    $ export PATH=/usr/local/bin:$PATH
    ```
Restart your Terminal

    ```
    $ brew install python3
    $ brew install pipenv
    ```

2. Clone and pipenv:

    ```
    $ git clone https://github.com/alkivi-sas/3cx-freshdesk-macos
    $ cd 3cx-freshdesk-macos
    $ pipenv install
    $ pipenv shell
    $ which python #result of this commande will help you to config 3CX
    ```

3. Change the conf file :

    ```
    $ cp freshdesk-example.conf freshdesk.conf
    $ vim freshdesk.conf
    ```
Change values with your platform, you can have your caller ID going to a ticket you resolved and you put '.json' at the end of the URL
Example :  https://domain.freshdesk.com/helpdesk/tickets/62.json , you will see responder_id. It is your caller ID.

For the API Key :
- Login to your Support Portal
- Click on your profile picture on the top right corner of your portal
- Go to Profile settings Page
- Your API key will be available below the change password section to your right

4. Create the log file :
    ```bash
    $ sudo touch /var/log/3cx-freshdesk-macos.log
    $ sudo chmod 660 /var/log/3cx-freshdesk-macos.log
    $ sudo chown $(whoami):staff /var/log/3cx-freshdesk-macos.log
    $ sudo chmod 660 /var/log/call_to_wiki.log
    $ sudo chown $(whoami):staff /var/log/call_to_wiki.log
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
   /Users/myuser/.local/share/virtualenvs/3cx-freshdesk-macos-rz7dl8z3/bin/python #you can know this dir using which python in the pipenv shell
   ```     
Parameters :
   ```
   --args /Users/myuser/path_of_3cx-freshdesk-macos/3cx_to_fresdesk.py -c %CallerNumber%
   ```  
