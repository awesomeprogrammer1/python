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
    
