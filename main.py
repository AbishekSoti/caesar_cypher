import string
#create a list with all the letters of the alphabet
alphabet = list(string.ascii_lowercase)
alphabet += alphabet
print(alphabet)
word = input("Enter a word: ").lower()
#convert the word to a list
word = list(word)
for i in range(0,len(word)):
    #find the index of the letter in the alphabet
    shift_number = input("Enter a number u wish to shift by:")
    index = alphabet.index(word[i])
    #replace the letter with the the letter of the shifted index
    word[i] = alphabet[index+ shift_number]
    print(word)
