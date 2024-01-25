welcome = '''
██████   █████  ███████ ███████  █████  ██████       ██████ ██ ██████  ██   ██ ███████ ██████
██      ██   ██ ██      ██      ██   ██ ██   ██     ██      ██ ██   ██ ██   ██ ██      ██   ██
██      ███████ █████   ███████ ███████ ██████      ██      ██ ██████  ███████ █████   ██████
██      ██   ██ ██           ██ ██   ██ ██   ██     ██      ██ ██      ██   ██ ██      ██   ██
██████  ██   ██ ███████ ███████ ██   ██ ██   ██      ██████ ██ ██      ██   ██ ███████ ██   ██
'''
print(welcome, "\n")

print("Welcome to Caesar Cipher encryptr/Decoder\n")

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', ';', ':', "'", '"', '<', '>', ',', '.', '/', '?', ' ']

def encrypt(text, shift):
    cipler = ""
    for i in text:
        if i in special_characters:
            cipler += i
            continue
        position = alphabet_list.index(i)
        new_position = position + shift
        if new_position>= len(alphabet_list):
            new_position -= len(alphabet_list)
        cipler += alphabet_list[new_position]
    return cipler

def decrypt(text, shift):
    cipler = ""
    for i in text:
        if i in special_characters:
            cipler += i
            continue
        position = alphabet_list.index(i)
        new_position = position - shift
        if new_position< 0:
            new_position += len(alphabet_list)
        cipler += alphabet_list[new_position]
    return cipler

while True:
    type = input("Would You like to encrypt(e) or decrypt(d)?: ")
    text = input("Enter text (lowercase only): ").lower()
    shift = int(input("Enter shift/key value: "))
    if type == 'e':
        print(f"The encrypted text is: {encrypt(text, shift)}")
    elif type == 'd':
        print(f"The decrypted text is: {decrypt(text, shift)}")
    else:
        print("Invalid input try again.")
        continue

    status = input("\nEnter 'y' to continue or 'n' to exit: ")
    if status == 'y':
        continue
    else:
        break

