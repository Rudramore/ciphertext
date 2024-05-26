# Vernam Cipher 

The project is designed to implement a Vernam cipher for secure encryption and decryption of messages. The primary objective is to take user-provided plaintext or ciphertext, validate the input, and either encrypt or decrypt it using a specified key. The input message is processed to ensure it consists of valid characters, then each character is converted to its binary representation. For encryption, the plaintext's binary data is XORed with a user-provided binary key to produce the ciphertext, which is then converted back to a readable format. For decryption, the ciphertext undergoes a similar process where it is XORed with the key to recover the original plaintext. The project also includes functionality to prompt the user for input, validate binary keys, and ensure proper format adherence. Additionally, there is a placeholder for a brute force attack function aimed at decrypting messages by trying all possible keys. The user interacts with the program through a simple interface that allows them to choose between encrypting, decrypting, or exiting the program.

## Function Documentation

'getmsg(prompt)'

- *Purpose*: Prompts the user to input a message for encryption or decryption, ensuring the input format is valid.

- **Parameters:**
-   'prompt' (str): The prompt message displayed to the user.

- **Return:**
-   'new_msg' (list of str): The message split into individual characters.

- **Details:**
- Continuously prompts the user until a valid message is provided.
- Validates the input to contain only lowercase and uppercase alphabets and spaces.

'is_valid_input(input_string)'

- *Purpose*: Validates that the input string contains only lowercase and uppercase alphabets and spaces.

- **Parameters:**
-   'input_string' (str): The string to validate.

- **Return:**
-   'bool' : True if the string is valid, False otherwise.

- **Details:**
- Uses a regular expression to check the format.

'char_to_bitstring(character)'

- *Purpose*:  Converts a character to its 8-bit binary string representation.

- **Parameters:**
-   'character' (str): The character to convert.

- **Return:**
-   'str' : The 8-bit binary representation of the character.

- **Details:**
- Specially handles spaces (' ') to ensure correct binary representation.

'bitstring_to_char(bitstring)'

- *Purpose*: Converts an 8-bit binary string back to its corresponding character.

- **Parameters:**
-   'bitstring' (str): The 8-bit binary string to convert.

- **Return:**
-   'str' : The corresponding character.

- **Details:**
- Converts from binary to integer and then to the character.

'bitstrings_to_chars(bitstring_list)'

- *Purpose*: Converts a list of bitstrings to their corresponding characters.

- **Parameters:**
-   'bitstring_list' (list of str): The list of bitstrings to convert.

- **Return:**
-   'str' : The resulting string of characters.

- **Details:**
- Uses 'bitstring_to_char' to convert each bitstring and joins the characters into a single string.

'xor_bitstrings(bitstring1, bitstring2)'

- *Purpose*: Applies XOR to two lists of bitstrings and returns the result as a list of bitstrings.

- **Parameters:**
-   list1 (list of str): The first list of bitstrings.
-   list2 (list of str): The second list of bitstrings.

- **Return:**
-   result_list (list of str) : The resulting list of bitstrings after applying XOR.

- **Details:**
- Both lists must have the same length.

'getkey(bit_list_size)'

- *Purpose*: Prompts the user to input a key for encryption or decryption.

- **Parameters:**
-   bit_list_size (int):  The required size of the key in bits.

- **Return:**
-   main_keys (list of str): The list of bitstrings representing the key.

- **Details:**
- Ensures the key is of the correct size and format.

'vernam_cipher_encrypt_decrypt(message, key)'

- *Purpose*: Encrypts or decrypts a message using the Vernam cipher.

- **Parameters:**
-  message (str): The message to encrypt or decrypt.
-  key (list of str): The key used for encryption or decryption.

- **Return:**
-  result (str): The resulting encrypted or decrypted message.

- **Details:**
- Uses XOR operation on the message and key bitstrings.

'brute_getmsg()'

- *Purpose*: Prompts the user to input a message for a brute force attack, ensuring the input format is valid.

- **Parameters:**
-  None

- **Return:**
- new_msg (list of str): The message split into individual characters.

- **Details:**
- Continuously prompts the user until a valid message is provided.
- Validates the input to contain only alphabets and spaces.

'is_brute_valid_input(input_string)'

- *Purpose*: Checks if the input string contains only alphabets and spaces.

- **Parameters:**
-  input_string (str): The input string to validate.

- **Return:**
- bool: True if the input string is valid, otherwise False.

- **Details:**
- Uses a regular expression pattern to validate the input string.

'brute_force()'

- *Purpose*: Applies a brute force attack on a Caesar cipher.

- **Parameters:**
- None
  
- **Return:**
- possible_plaintext (dict): A dictionary with keys as shift values and values as the possible plaintexts

- **Details:**
- Tries all possible shifts and records the resulting plaintexts.

'encrypt()'

- Encrypts a message using the Vernam cipher.

- **Parameters:**
- None
  
- **Return:**
- cipher_text (str): The encrypted message.

- **Details:**
- Prompts the user for a message and key, then applies the Vernam cipher.

'decrypt()'

- Decrypts a message using the Vernam cipher.

- **Parameters:**
- None
  
- **Return:**
- plain_text (str): The decrypted message.

- **Details:**
- Prompts the user for a message and key, then applies the Vernam cipher.



