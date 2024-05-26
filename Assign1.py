import re
import string
import math

# Function to get the message/plaintext from the user
def getmsg(prompt="Provide the msg for encryption in the format (word1 word2) or (word): "):
    msg = input(prompt)
    print("\n")
    while not msg or not is_valid_input(msg):
        msg = input("Provide valid msg for encryption in the format (word1 word2) or (word): ")
        print("\n")
    return msg

# Check if the input string contains only lowercase alphabets and spaces.
def is_valid_input(input_string):
    pattern = r'^[a-z]+( [a-z]+)?$'
    return bool(re.match(pattern, input_string))

# Convert a character to its 8-bit binary string representation.
def char_to_bitstring(character):
    if character == ' ':
        return '00100000'
    return bin(ord(character))[2:].zfill(8)

# Convert a list of bitstrings to their corresponding characters.
def bitstring_to_char(bitstring):
    integer_value = int(bitstring, 2)
    character = chr(integer_value)
    return character

# Convert a list of bitstrings to their corresponding characters.
def bitstrings_to_chars(bitstring_list):
    characters = [bitstring_to_char(bitstring) for bitstring in bitstring_list]
    result_string = ''.join(characters)
    return result_string

# Apply XOR to two bitstrings and return the result as a bitstring.
def xor_bitstrings(bitstring1, bitstring2):
    int1 = int(bitstring1, 2)
    int2 = int(bitstring2, 2)
    xor_result = int1 ^ int2
    result_bitstring = bin(xor_result)[2:].zfill(len(bitstring1))
    return result_bitstring

# Apply XOR to two lists of bitstrings and return the result as a list of bitstrings.
def xor_bitstring_lists(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")
    result_list = [xor_bitstrings(b1, b2) for b1, b2 in zip(list1, list2)]
    return result_list

# Function to get the key from the user
def getkey(bit_list_size):
    main_keys = []
    print("Following commands require you to insert an 8-bit key.\n")
    print("Any key less than 8 bits will have 0-bit added from the left but more than 8 bits will be invalid.\n")
    print(f"The number of keys is the same as the total number of characters in the message ({bit_list_size} characters).\n")
    j = 0
    while j < bit_list_size:
        key = input("Provide key for encryption: ")
        print("\n")
        if not key:
            print("No key entered")
        elif len(key) > 8:
            print("Digits don't match the recommended length")
            print("\n")
            continue
        elif len(key) < 8:
            if is_valid_binary_input(key):
                while len(key) != 8:
                    key = "0" + key
                main_keys.append(key)
                j += 1
            else:
                print("Less than 8 bits")
                print("\n")
                print("Invalid key entered")
                print("\n")
                continue
        else:
            if is_valid_binary_input_main(key):
                main_keys.append(key)
                j += 1
            else:
                print("Invalid key entered")
                print("\n")
                continue
    return main_keys

# Check if the input string is a valid 8-bit binary number.
def is_valid_binary_input_main(input_string):
    pattern = r'^[01]{8}$'
    return bool(re.match(pattern, input_string))

def is_valid_binary_input(input_string):
    pattern = r'^[01]+$'
    return bool(re.match(pattern, input_string))

# Function to encrypt the message
def encrypt():
    plaintext = getmsg("Provide the plaintext for encryption in the format (word1 word2) or (word): ")
    bitstrings = [char_to_bitstring(char) for char in plaintext]
    key = getkey(len(bitstrings))
    encrypted_bitstrings = xor_bitstring_lists(bitstrings, key)
    ciphertext = bitstrings_to_chars(encrypted_bitstrings)
    return ciphertext

# Function to decrypt the message
def decrypt():
    ciphertext = getmsg("Provide the ciphertext for decryption in the format (word1 word2) or (word): ")
    bitstrings = [char_to_bitstring(char) for char in ciphertext]
    key = getkey(len(bitstrings))
    decrypted_bitstrings = xor_bitstring_lists(bitstrings, key)
    plaintext = bitstrings_to_chars(decrypted_bitstrings)
    return plaintext

def brute_getmsg(prompt="Provide the msg for decryption in the format (word1 word2) or (word): "):
    msg = input(prompt)
    print("\n")
    while not msg or not is_brute_valid_input(msg):
        msg = input("Provide valid msg for encryption in the format (word1 word2) or (word): ")
        print("\n")
    return msg


# Check if the input string contains only alphabets and spaces.
def is_brute_valid_input(input_string):
    pattern = r'^[a-zA-Z ]+$'
    return bool(re.match(pattern, input_string))

#Applying Brute Force method to Caeser cipher 
def brute_force():
    cipher_text = brute_getmsg()
    possible_plaintext = {}

    for i in range(26):
        new_text = []
        for char in cipher_text:
            if char.islower():
                index = ord(char) - ord('a')
                new_pos = (index + i) % 26
                new_text.append(string.ascii_lowercase[new_pos])
            elif char.isupper():
                index = ord(char) - ord('A')
                new_pos = (index + i) % 26
                new_text.append(string.ascii_uppercase[new_pos])
            else:
                new_text.append(char)
        shift = str(i) + " shift"
        possible_plaintext[shift] = ''.join(new_text)

    return possible_plaintext




if __name__ == "__main__":
    print("Welcome to cryptography 101\n")
    print("This is a Vernam cipher program \n")
    print("Choose an option: \n")
    print("1. Encryption \n")
    print("2. Decryption \n")
    print("3. Brute Force Attack \n")
    print("4. End program \n\n")



    while True:

        x = input("Enter your choice (1,2,3,4): ")
        print("\n")

        if (x == '1'):
            cipher_text = encrypt()
            print("Ciphertext: ",cipher_text)

        elif (x =='2'):
            new_plain_text = decrypt()
            print("Plaintext: ",new_plain_text)

        elif( x == '3'):
            brute_f= brute_force()
            print("Possible plaintext combinations: ", brute_f)
        
        elif( x == '4'):
            print("Have a nice day. Best reagrds, Rudra More")
            break

        else:
            print("Invalid Input")
            x = input("Enter only either these choices (1,2,3,4): ")
            print("\n")



    

    