import argparse
from manager import PasswordManager
from auth import verify_master_password
import getpass


def authenticate():
    password = getpass.getpass("Enter master password: ")
    if not verify_master_password(password):
        print("Authentication failed.")
        exit()


def main():
    parser = argparse.ArgumentParser(description="CLI Password Manager")

    parser.add_argument("command", choices=["add", "get", "delete", "list"])
    parser.add_argument("--site", help="Site name")
    parser.add_argument("--password", help="Password")

    args = parser.parse_args()

    authenticate()

    manager = PasswordManager()

    if args.command == "add":
        manager.add_password(args.site, args.password)

    elif args.command == "get":
        manager.get_password(args.site)

    elif args.command == "delete":
        manager.delete_password(args.site)

    elif args.command == "list":
        manager.list_sites()


if __name__ == "__main__":
    main()