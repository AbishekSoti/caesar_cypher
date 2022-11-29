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
    index = alphabet.index(word[i])
    #replace the letter with the letter 13 places after it
    word[i] = alphabet[index+13]
