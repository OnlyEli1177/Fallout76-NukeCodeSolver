from collections import OrderedDict
import os
def translate_from_dict(original_text,dictionary_of_translations):
    out = original_text
    for target in dictionary_of_translations:
        trans = str.maketrans(target,dictionary_of_translations[target])
        out = out.translate(trans)
    return out

with open("NukeCodeSolution.txt", "w") as file:
    code = input("Enter the Enclave bunker keyword: ")
    file.write(f'Bunker Keyword: {code.upper()}')
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    file.write(f'\nEnglish Alphabet: {alphabet.upper()}')
    alphabet_word_removed = alphabet.translate({ ord(c): None for c in f"{code.lower()}" })
    code_alphabet = f"{code.lower()}{alphabet_word_removed}"
    def removeDupWithOrder(str):
        return "".join(OrderedDict.fromkeys(str))
    file.write(f'\nCipher Alphabet: {removeDupWithOrder(code_alphabet).upper()}')
    alphabet_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_translation = [l for l in code_alphabet]
    translation_dict = dict(zip(alphabet_translation, alphabet_letters))
    reverse_translation_dict = dict(zip(alphabet_letters, alphabet_translation))
    print(f'English Alphabet: {alphabet.upper()}')
    print(f'Cipher Alphabet:  {removeDupWithOrder(code_alphabet).upper()}')
    code_piece1 = input("Enter the letter and number combination from your first code piece: ")
    file.write(f'\nCode Piece 1: {code_piece1.upper()}')
    code_piece2 = input("Enter the letter and number combination from your second code piece: ")
    file.write(f'\nCode Piece 2: {code_piece2.upper()}')
    code_piece3 = input("Enter the letter and number combination from your third code piece: ")
    file.write(f'\nCode Piece 3: {code_piece3.upper()}')
    code_piece4 = input("Enter the letter and number combination from your fourth code piece: ")
    file.write(f'\nCode Piece 4: {code_piece4.upper()}')
    code_piece5 = input("Enter the letter and number combination from your fifth code piece: ")
    file.write(f'\nCode Piece 5: {code_piece5.upper()}')
    code_piece6 = input("Enter the letter and number combination from your sixth code piece: ")
    file.write(f'\nCode Piece 6: {code_piece6.upper()}')
    code_piece7 = input("Enter the letter and number combination from your seventh code piece: ")
    file.write(f'\nCode Piece 7: {code_piece7.upper()}')
    code_piece8 = input("Enter the letter and number combination from your eighth code piece: ")
    file.write(f'\nCode Piece 8: {code_piece8.upper()}')
    code_piece_list = [f'{code_piece1}',
                       f'{code_piece2}',
                       f'{code_piece3}', 
                       f'{code_piece4}', 
                       f'{code_piece5}', 
                       f'{code_piece6}', 
                       f'{code_piece7}', 
                       f'{code_piece8}', 
                       ]
    code_piece_list_compiled = ' '.join(code_piece_list).replace(" ","")
    code_piece_numbers = []
    for i in code_piece_list_compiled:
        if i.isdigit():
            code_piece_numbers.append(i)
    code_piece_numbers_compiled = ''.join(code_piece_numbers)
    print(f'Code Piece Numbers: {code_piece_numbers_compiled}')
    code_piece_letters = []
    for i in code_piece_list_compiled:
        if not i.isdigit():
            code_piece_letters.append(i)
    code_piece_letters_compiled = ''.join(code_piece_letters)
    print(f'Code Piece Letters: {code_piece_letters_compiled.upper()}')
    code_piece_dict = dict(zip(code_piece_letters, code_piece_numbers))
    print("Decrypting Code Piece Lettering with Alphabetical Substitution Cipher...")
    decoded_code_pieces = ""
    for letter in code_piece_letters_compiled:
        if letter.lower() in code_alphabet:
            decoded_code_pieces += alphabet[code_alphabet.find(letter.lower())]
        else:
            decoded_code_pieces += letter
    print("Decrypted Code Piece Lettering SUCCESSFULLY!")
    print("********************CODE PIECE********************")
    print("You must make an English word out of these letters")
    print("**************************************************")
    print(f'Decrypted Code Piece Lettering: {decoded_code_pieces.upper()}')
    print("**************************************************")
    code_word = input("Enter the English code word: ")
    file.write(f'\nDecrypted Code Word: {code_word.upper()}')
    print("Re-Encrypting Code Piece Lettering with Alphabetical Substitution Cipher...")
    code_word_encoded = ""
    for letter in code_word:
        if letter.lower() in alphabet:
            code_word_encoded += code_alphabet[alphabet.find(letter.lower())]
        else:
            code_word_encoded += letter
    print("Re-Encrypted Code Piece Lettering SUCCESSFULLY!")
    print("Generating Nuclear Launch Codes...")
    file.write(f'\nRe-Encrypted Code Word: {code_word_encoded.upper()}')
    nuke_code = translate_from_dict(code_word_encoded, code_piece_dict)
    print("*********************")
    print(f"*NUKE CODE: {nuke_code}*")
    print("*********************")
    file.write("\n*********************")
    file.write(f'\n*NUKE CODE: {nuke_code}*')
    file.write("\n*********************")
    print("DONE")