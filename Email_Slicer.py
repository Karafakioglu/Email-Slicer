email = input("Enter an email: ")

def Test(email):
    return email.split("@")

print("Your username is: {} and your domain name is: {}".format(Test(email)[0], Test(email)[1]))

