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
    
def decrypt(text,key):
    result = ''
    for letter in text:
        if letter in alphabet:
            position=alphabet.find(letter)
            new_position=position+key
            original_position= position-key
            result+=alphabet[original_position]
        else:
            result+=letter
    return(result)





if __name__ == "__main__":
   my_original_text = 'Hedgie'
   print(my_original_text)
   my_encrypted_text = encrypt(my_original_text, 1)
   print(my_encrypted_text)
   my_decrypted_text = decrypt(my_encrypted_text,1)
   print(my_decrypted_text)



