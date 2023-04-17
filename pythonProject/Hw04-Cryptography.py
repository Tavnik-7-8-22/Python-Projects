""" Project Name: Hw04-Cryptography.py

    Description: This program allows you to encipher and decipher things using the Caesar cipher.

    Name:Samuel Rabinor

    Date: Nov 8 2022
"""


def letter_probability(c):
    """ if c is the space character or an alphabetic character,
        we return its monogram probability (for english),
        otherwise we return 1.0 We ignore capitalization.
        Adapted from
        http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
    """
    if c == ' ': return 0.1904
    if c == 'e' or c == 'E': return 0.1017
    if c == 't' or c == 'T': return 0.0737
    if c == 'a' or c == 'A': return 0.0661
    if c == 'o' or c == 'O': return 0.0610
    if c == 'i' or c == 'I': return 0.0562
    if c == 'n' or c == 'N': return 0.0557
    if c == 'h' or c == 'H': return 0.0542
    if c == 's' or c == 'S': return 0.0508
    if c == 'r' or c == 'R': return 0.0458
    if c == 'd' or c == 'D': return 0.0369
    if c == 'l' or c == 'L': return 0.0325
    if c == 'u' or c == 'U': return 0.0228
    if c == 'm' or c == 'M': return 0.0205
    if c == 'c' or c == 'C': return 0.0192
    if c == 'w' or c == 'W': return 0.0190
    if c == 'f' or c == 'F': return 0.0175
    if c == 'y' or c == 'Y': return 0.0165
    if c == 'g' or c == 'G': return 0.0161
    if c == 'p' or c == 'P': return 0.0131
    if c == 'b' or c == 'B': return 0.0115
    if c == 'v' or c == 'V': return 0.0088
    if c == 'k' or c == 'K': return 0.0066
    if c == 'x' or c == 'X': return 0.0014
    if c == 'j' or c == 'J': return 0.0008
    if c == 'q' or c == 'Q': return 0.0008
    if c == 'z' or c == 'Z': return 0.0005
    return 1.0


def encipher(text, num):
    """
    Will encipher a string
    :param text: the string you are enciphering
    :param num: the amount of numbers you are moving each letter
    :return: the enciphered string
    """
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #lists all upercase letters.
    shifted_upper = upper[-num:] + upper[:-num] #the code used to shift uppercase letters in the text
    lower = "abcdefghijklmnopqrstuvwxyz" #lists all lowercase letters
    shifted_lower = lower[-num:] + lower[:-num] #the code used to shift lowercase letters in the text
    encipher_str = "" #the enciphered text

    print(shifted_upper)

    for ch in text:
        if ch in upper:
            ch_pos = upper.index(ch)
            encipher_str += shifted_upper[ch_pos] #the code telling the computer to keep text shifted in uppercase
        elif ch in lower:
            ch_pos = lower.index(ch)
            encipher_str += shifted_lower[ch_pos] #the code telling the computer to keep text shifted in lowercase
        else:
            encipher_str += ch #the code telling the computer to leave text as is if not upper or lowercase
    return encipher_str


print(encipher('My dog has fleas', 7))
print(encipher('Meet at the dock at noon tomorrow.', 20))


def decipher(text, num):
    """
    Will encipher a string
    :param text: the string you are deciphering
    :param num: the amount of numbers you are moving each letter
    :return: the deciphered string
    """
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_upper = upper[num:] + upper[:num]
    lower = "abcdefghijklmnopqrstuvwxyz"
    shifted_lower = lower[num:] + lower[:num]
    encipher_str = ""

    for ch in text:
        if ch in upper:
            ch_pos = upper.index(ch)
            encipher_str += shifted_upper[ch_pos]
        elif ch in lower:
            ch_pos = lower.index(ch)
            encipher_str += shifted_lower[ch_pos]
        else:
            encipher_str += ch
    return encipher_str


print(decipher('Fr whz atl yextl.', 7))
print(decipher('Skkz gz znk juiq gz tuut zusuxxuc.', 20))


def try_all_shifts(text):
    """
    Will attempt to decipher a message where we do not know the number of characters it has been shifted.
    :param text: The enciphered text (string)
    :return: The most likely shift that was used to encrypt that text string.
    """
    highest = 0  # initialize highest here
    index = 0

    for i in range(26):  # the length of data is 3
        total = 0  # reset total to 0
        test_text = decipher(text, i)
        for ch in test_text:
            total += letter_probability(ch)  # add the number in the list

        if total > highest:
            highest = total
            index = i
    return index


print(try_all_shifts('Fr whz atl yextl.'))
print(try_all_shifts('Skkz gz znk juiq gz tuut zusuxxuc.'))

while True:
    enciphered_choice = input("Enter 1 to encipher or 2 to decipher: ")
    try:
        enciphered_choice = int(enciphered_choice)  # input results in a string--int() to convert
        break
    except ValueError:
        print("Error: You must enter a valid number. Try again...")

if enciphered_choice == 1:
    encipher_text = input("Enter text you wish to encipher: ")
    num_shift = input("Enter the number of characters to shift: ")
    num_shift = int(num_shift)
    print("The encrypted text is: " + encipher(encipher_text, num_shift))

if enciphered_choice == 2:
    deciphered_text = input("Enter text you wish to decipher:")
    print("The most likely string is" + str(try_all_shifts(deciphered_text)))
    print(decipher(deciphered_text, int(try_all_shifts(deciphered_text))))

