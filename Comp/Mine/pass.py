def get():
    with open("passwords") as f:
        passwords = [l.strip() for l in f.readlines()]
        return passwords