# 023 Ask the user to type in the first line of a nursery rhyme and display the length of the string. Ask for a starting number and an ending number and then display just that section of the text (remember Python starts counting from 0 and not 1).

rhyme = input("Enter the firstline of Rhyme: ")
print(len(rhyme))

startNum = int(input("Enter the Start Number: "))
endNum = int(input("Enter the End Number: "))
part = rhyme[startNum:endNum]
print(part)

