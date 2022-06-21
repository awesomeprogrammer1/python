alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_size = 26

scramble_amount = int(input('By how many spaces will each letter move? '))

def encrypt(text,key):
    result=''
    for letter in text:
        if letter in alphabet:
            position=alphabet.find(letter)
            new_position=position+key
            if new_position >= alphabet_size:
                new_position=new_position-alphabet_size
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
            if original_position >= alphabet_size:
                original_position=original_position+alphabet_size
            result+=alphabet[original_position]
        else:
            result+=letter
    return(result)


if __name__ == "__main__":
   my_original_text = 'abcdefghijklmnopqrstuvwxyz'
   print(my_original_text)
   my_encrypted_text = encrypt(my_original_text, scramble_amount-alphabet_size)
   print(my_encrypted_text)
   my_decrypted_text = decrypt(my_encrypted_text, scramble_amount-alphabet_size)
   print(my_decrypted_text)



