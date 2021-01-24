from codes import morse_code

converted_list = []

def convert_to_morse():
    plain_code = input('Input a word you wanna convert: ')

    for letter in plain_code:
        converted_list.append(morse_code[letter])

    encoded_word = ' '.join(converted_list)
    print(f"Result:\n{encoded_word}")

if __name__ == '__main__':
    convert_to_morse()
