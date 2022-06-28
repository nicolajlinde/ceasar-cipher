import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

end_game = False

while end_game is not True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def ceasar(cipher_text, shift_amount, cipher_direction):
        i = 0
        cipher = str()

        for i in range(len(cipher_text)):
            letters = cipher_text[i]

            if letters not in alphabet:
                cipher += letters
            else:
                index_in_alphabet = alphabet.index(letters) + shift_amount

                if cipher_direction == "decode":
                    index_in_alphabet = alphabet.index(letters) + (26 - shift_amount)

                cipher += alphabet[index_in_alphabet]

        print(f"The {cipher_direction}d text is {cipher}")


    ceasar(cipher_text=text, shift_amount=shift % 26, cipher_direction=direction)
    x = input("Want to go again? Type 'yes' or 'no'").lower()

    if x == "no":
        end_game = True
