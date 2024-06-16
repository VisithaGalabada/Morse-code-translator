morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                'Y': '-.--', 'Z': '--..',
                '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
                '7': '--...', '8': '---..', '9': '----.',
                ' ': '.-..-.', '.': '.-.-.-', '#': '.-..-.', '?': '..--..', '!': '..--.'}

def text_to_morse(text):
    morse_code = ''
    for char in text:
        char_upper = char.upper()
        if char_upper in morse_code_dict:
            morse_code += morse_code_dict[char_upper] + ' '
        else:
            morse_code += char + ' '

    return morse_code.strip()

def morse_to_text(morse_code):
    morse_code_dict_reverse = {value: key for key, value in morse_code_dict.items()}
    morse_words = morse_code.split(' ')
    english_text = ''
    for morse_word in morse_words:
        if morse_word in morse_code_dict_reverse:
            english_text += morse_code_dict_reverse[morse_word]
        else:
            english_text += morse_word

    return english_text

def main():
    while True:
        user_choice = input("Enter '1' to translate from English to Morse code or '2' to translate from Morse code to English: ")
        
        if user_choice == '1':
            user_input = input("Enter a number, letter, or sentence: ")
            translated_text = text_to_morse(user_input)
            print(f"Morse Code: {translated_text}")
        elif user_choice == '2':
            user_input = input("Enter Morse code: ")
            translated_text = morse_to_text(user_input)
            print(f"English Text: {translated_text}")
        else:
            print("Invalid choice. Please enter '1' or '2'.")
        
        try_again = input("Do you want to try again? (yes/no): ")
        if try_again.lower() not in ['yes', 'y']:
            break

if __name__ == "__main__":
    main()