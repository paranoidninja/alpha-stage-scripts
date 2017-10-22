#!/usr/bin/env python3


##Author : Paranoid Ninja
##Email  : paranoidninja@protonmail.com
##Descr  : Creates a Simple FTP Server in the tmp directory

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

FTP_PORT = 2121
FTP_USER = "ninja"
FTP_PASSWORD = "ninja"
FTP_DIRECTORY = "/media/paranoidninja/Files/my_git_repos/personal_projects/alpha-stage-scripts"


def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm='elradfmw')

    handler = FTPHandler
    handler.authorizer = authorizer
    handler.banner = "Python's Ninja FTP Server"

    address = ('', FTP_PORT)
    server = FTPServer(address, handler)

    server.max_cons = 256
    server.max_cons_per_ip = 5

    server.serve_forever()


if __name__ == '__main__':
    main()
