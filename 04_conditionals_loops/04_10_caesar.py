''' Replicate one of the oldest known encryption in code.

Apply a Cesar cipher of 7 to the 'secret' variable.

P.S.: http: // www.montypython.net / scripts / dentist.php;)

You can start with the following code:
'''

secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7
alphabet = ["a", "b", "c", "d", "e", "f","g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

secret_lower = secret.lower()
new_secret = list(secret_lower)
cipher_message = []

a = 0
my_dict = {}
for i in alphabet:
    a += 1
    my_dict[i] = a

for w in new_secret:
    if w in alphabet:
        x = my_dict.get(w)
        if x > (len(alphabet) - cipher -1):
            w = alphabet[(x + cipher)-len(alphabet) -1]
            cipher_message.append(w)
        if x <= (len(alphabet) - cipher -1):
            w = alphabet[x + cipher - 1]
            cipher_message.append(w)
    else:
        cipher_message.append(w)

cipher_string = ""
for c in cipher_message:
    cipher_string += c

print(cipher_string.capitalize())