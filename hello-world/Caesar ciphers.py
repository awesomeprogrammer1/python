

alphabet = 'abcdefghijklmnopqrstuvwxyz' # variable for alphabet
alphabet_size = len(alphabet) # outputting the value of the string

scramble_amount = int(input('By how many spaces will each letter move? ')) # Requesting the # the letters will shift by

def encrypt(text,key): # function to encrypt
    result='' #placeholder
    for letter in text: # for statement, runs until every letter has been adjusted, one at a time
        if letter in alphabet: # determines if the character in the string is a part of the variable "alphabet"
            position=alphabet.find(letter) # determining the position of the current letter
            new_position=position+key # determining what the current letter should be replaced with
            if new_position >= alphabet_size: # determining if the variable new_position_ has a higher value, or is equal to the variable "alphabet_size"
                new_position=new_position-alphabet_size # finding the new letter
            result+=alphabet[new_position] # outputting the result
        else:
            result+=letter # gives the # of letters the original letter needs to be moved by
    return(result) # outputs the result
    
def decrypt(text,key): # function to decrypt
    result = '' #placeholder
    for letter in text:  # see note at bottom
        if letter in alphabet:  # see note at bottom
            position=alphabet.find(letter)   # see note at bottom
            new_position=position+key   # see note at bottom
            original_position= position-key  # see note at bottom
            if original_position >= alphabet_size:   # see note at bottom
                original_position=original_position-alphabet_size   # see note at bottom 
            result+=alphabet[original_position]  # see note at bottom
        else:  # see note at bottom
            result+=letter  # see note at bottom
    return(result) # see note at bottom


if __name__ == "__main__": #condition
   my_original_text = 'abcdefghijklmnopqrstuvwxyz' # variable to express the original text
   print(my_original_text) # output
   my_encrypted_text = encrypt(my_original_text, scramble_amount-alphabet_size) # variable to express the new text, and the process to get to it.
   print(my_encrypted_text) # output
   my_decrypted_text = decrypt(my_encrypted_text, scramble_amount-alphabet_size) #variable to change the encrypted text back to normal
   print(my_decrypted_text) # output



# Note: Lines 21-33 are essentially the same process as lines 8-19, but reversed.