alphabet= 'abcdefghijklmnopqrstuvwxyz'
def encrypt(text,key):
    result=''
    for letter in text:
        if letter in alphabet:
            position=alphabet.find(letter)
            new_position=position+key
            result+=alphabet[new_position]
        else:
            result+=letter
    return(result)
    
if __name__ == "__main__":
   my_text = 'Hedgie'
   print(my_text)
   my_encrypted_text = encrypt(my_text, 1)
   print(my_encrypted_text)
