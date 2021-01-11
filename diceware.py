from store_dict import get_dict
import secrets
def get_word():
    dictionary =  get_dict("diceware.wordlist.asc.webarchive")
    while True:
        try:
            res = ""
            word = ""
            for i in range(5):
                word += str(secrets.randbelow(7))
            res = dictionary[word]
            break
        except KeyError:
            pass
    return res

def create_password(num_words):
    password = ""
    for i in range(num_words):
        password += get_word() + " "
    return password

print(create_password(6)) #change this number in order to increase or decrease security. 
                          #The minimum recommended number of words is 6 for a secure password.
