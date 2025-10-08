def createUsername(username):
    if len(username) < 3:
        print("The username must be at least 3 characters long")
    elif len(username) > 20:
        print("The username must be no more than 20 characters long")
    else:
        print("Valid choice of username")

createUsername("john")
createUsername("jo")
createUsername("adsadwdasdwadsdawdsadwad")