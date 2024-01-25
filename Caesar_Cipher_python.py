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
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', ';', ':', "'", '"', '<', '>', ',', '.', '/', '?', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def caesar(text, shift, type):
    cipler = ""
    for i in text:
        if i in special_characters:
            cipler += i
            continue
        position = alphabet_list.index(i)
        if type == "e":
            new_position = position + shift
            if new_position>= len(alphabet_list):
                new_position -= len(alphabet_list)
        elif type == "d":
            new_position = position - shift
            if new_position< 0:
                new_position += len(alphabet_list)
        cipler += alphabet_list[new_position]
    return cipler

while True:
    user_req = input("Would You like to encrypt(e) or decrypt(d)?: ")
    text = input("Enter text (lowercase only): ").lower()
    shift = int(input("Enter shift/key value: "))
    if user_req == 'e':
        print(f"The encrypted text is: {caesar(text, shift, user_req)}")
    elif user_req == 'd':
        print(f"The decrypted text is: {caesar(text, shift, user_req)}")
    else:
        print("Invalid input try again.")
        continue

    status = input("\nEnter 'y' to continue or 'n' to exit: ")
    if status == 'y':
        continue
    else:
        break
