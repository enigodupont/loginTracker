#!/usr/bin/python3
import requests
import getopt
import sys
from hashlib import sha256
from getpass import getpass

def get_password(password):
    pass_hash = sha256()
    if not password:
        password = getpass("password: ")
    """"

    pass_hash.update(str.encode(password))

    return pass_hash.hexdigest()
    """
    return password

def send_requests(username, target, pass_hash):
    if not pass_hash:
        pass_hash = get_password(pass_hash)

    try:
        r = requests.post(target, data = {'user': username, 'pass': pass_hash})
        if "pass" in r.text:
            print("[*] location logged")
        else:
            print("[**] failed to log location")
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)

def usage():
    print("%s (-u | --user=) <username> [-p | --pass=] <password> (-t | --target=) <target address> | [-h | --help]" % sys.argv[0])
    sys.exit(1)

def main():

    try:
        opts, args = getopt.getopt(sys.argv[1:], "u:p:t:h", ["help", "user=", "pass=", "target="])
    except getopt.GetoptError as err:
            print(err)
            usage()
            sys.exit(1)
    username  = ""
    target    = ""
    pass_hash = ""

    for o, a in opts:
        if o in ("-u", "--user="):
            username = a
        elif o in ("-t", "--target="):
            target = a
        elif o in ("-p", "--pass="):
            pass_hash = get_password(a)
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        else:
            assert False, "unhandled option"

    if not username or not target:
        usage()

    send_requests(username, target, pass_hash)

if __name__ == "__main__":
    main()
