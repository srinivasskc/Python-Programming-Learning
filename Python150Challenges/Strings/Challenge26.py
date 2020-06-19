# 026 Pig Latin takes the first consonant of a word, moves it to the end of the word and adds on an “ay”. If a word begins with a vowel you just add “way” to the end. For example, pig becomes igpay, banana becomes ananabay, and aadvark becomes aadvarkway. Create a program that will ask the user to enter a word and change it into Pig Latin. Make sure the new word is displayed in lower case.

word = input("Enter a word: ")
length = len(word)
print(length)
first = word[0]
print(first)
rest = word[1:length]
print(rest)

if first!="a" and first!="e" and first!="i" and first!="o" and first!="u":
    new_word = rest + first + "ay"
    print(new_word.lower())
else:
    new_word = word + "way"
    print(new_word.lower())