
 # In cryptography, a Caesar cipher, also known as Caesars cipher, the shift cipher, Caesars
 # code or Caesar shift, is one of the simplest and most widely known encryption techniques.
 #  It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number
 #of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.
 #The method is named after Julius Caesar, who used it in his private correspondence. - Wikipedia


# The function str2lst accepts a string  and returns its arithmetic coding to ASCI

def str2lst(string):

    return [ord(x) - 65 for x in string]


# The function lst2str receives a list of numbers and returns an alphanumeric

def lst2str(list):

    return ''.join([chr(x+65) for x in list])

# The 'encryption' function encrypts the string 'string' using the key 'key'

def encryption(string, key):

    pln = str2lst(string)
    plnsf = [(x + key ) % 26 for x in pln]
    return lst2str(plnsf)

# The 'decryption' function performs the decryption of the string 'string using the key 'key'

def decryption(string, key):
    ctx = str2lst(string)
    ctxsf = [(x - key) % 26 for x in ctx]
    return lst2str(ctxsf)


if __name__ == '__main__':

      # Τhe message we want to encrypt

      stringForEncryption ="STRINGFORENCRYPTION"

      print("The message for encryption is : ", stringForEncryption)

      # the key with which we will encrypt

      key = 10

      enMessage = encryption(stringForEncryption, key)

      print("The encrypted messages is : ", enMessage)

      decMessage = decryption(enMessage, key)

      print("The decrypted messages is : ", decMessage)










