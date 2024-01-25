# Caesar Cipher Encryptor/Decryptor using Python programming language

Welcome to the Caesar Cipher Encryptor/Decryptor! This Python program allows you to encrypt or decrypt messages using the Caesar Cipher algorithm.

## Overview
The Caesar Cipher is a simple substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet. In this implementation, only lowercase letters are considered, and special characters remain unchanged.

## Features
- **Encryption:** Secure your messages by shifting the letters in your text based on a chosen key.
- **Decryption:** Easily decrypt previously encrypted messages with the correct key.
- **Special Characters:** Preserve special characters in the text during encryption and decryption.
- **Interactive Interface:** User-friendly interface for input and output, making it accessible for everyone.
- **Flexible Shift Values:** Choose any positive integer as the shift value for greater customization.
- **Repeatable:** Encrypt or decrypt as many messages as you want in a single run.

## Usage
1. Run the program and choose whether to encrypt or decrypt.
2. Enter the lowercase text you want to process.
3. Provide the shift value for encryption or decryption.
4. The program will output the result.
   
## Example 
Here's an example of decrypting a message using the command line:

```
$ python caesar_cipher.py
Would You like to encrypt(e) or decrypt(d)?: d
Enter text (lowercase only): "udymts'x xnruqnhnyd fsi wjfifgnqnyd rfpj ny f kfatwnyj frtsl ijajqtujwx btwqibnij! ny'x qnpj f xsfpj bjfansl ymwtzlm htij, xywnpnsl bnym ymj utbjw tk {afwnfgqjx} fsi ymj jqjlfshj tk kzshyntsx."
Enter shift/key value: 5
The decrypted text is: "Python's simplicity and readability make it a favorite among developers worldwide! It's like a snake weaving through code, striking with the power of {variables} and the elegance of functions."
```

Feel free to experiment with different texts and shift values!

## License
This project is licensed under the [MIT License](LICENSE).
