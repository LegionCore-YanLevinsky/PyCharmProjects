from tkinter import *
from passlib.hash import sha256_crypt
import json


def has_user(login):
    with open("passdb.json") as pf:
        data = json.load(pf)

    if login in data:
        logger.debug("{}: user in db".format(login))
        return True
    else:
        logger.debug("{}: no such user".format(login))
        return False


def get_hash_from_db(login):
    with open("passdb.json") as pf:
        data = json.load(pf)
    return data[login]


def create_user(login, password):
    with open("passdb.json") as pf:
        data = json.load(pf)

    with open("passdb.json", "w") as pf:
        # hash_login = sha256_crypt.hash(login)
        hash_pass = sha256_crypt.hash(password)

        data[login] = hash_pass
        json.dump(data, pf)


def login_process(login, password):
    if has_user(login):
        if sha256_crypt.verify(password, get_hash_from_db(login)):
            print("{}: verifying is true".format(login))
        else:
            print("{}: verifying is false".format(login))


root = Tk()

root.title("Login GUI")
root.minsize(250, 150)
root.resizable(False, False)

text_1 = Label(root, text="login")
text_2 = Label(root, text="password")
entry_1 = Entry(root)
entry_2 = Entry(root)
btn = Button(root, text="Enter", command=lambda: login_process(entry_1.get(), entry_2.get()))

text_1.pack()
entry_1.pack()
text_2.pack()
entry_2.pack()
btn.pack()

if __name__ == "__main__":
    if not has_user("test"):
        create_user("test", "123")

    root.mainloop()
