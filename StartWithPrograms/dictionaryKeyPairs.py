studentsAgeDictionary =  {"Srini":30, "Teju" : 28, "Arjun" : 1 }
print(studentsAgeDictionary)

studentsAgeDictionaryIn =  {"Srini":30, "Teju" : 28, "Arjun" : 1, "Teju" : 10}
print(studentsAgeDictionaryIn)
#In the results, it will replace first value of Teju with next Value.

studentsAgeDictionaryIn =  {"Srini":30, "Teju" : 28, "Arjun" : 1, "Teju" : 10, "Teju" : 25}
print(studentsAgeDictionaryIn)
print(studentsAgeDictionaryIn["Teju"])


#DictionaryKeys must be unique 


empNameAndAge = dict(Mithun=30,Sharadha=22,Sneha=27)
print(empNameAndAge)
print(empNameAndAge["Mithun"])
empNameAndAge["Mithun"]=29
print(empNameAndAge["Mithun"])
print(empNameAndAge)



"""
empNameAndAgeN = dict(Mithun=30,Sharadha=22,Sneha=27,Sharadha=24)
print(empNameAndAgeN)
"""
# we cannot have same dictionary key. Error - Key Argument Repeated.


#Adding data to empty dictionary.
emptyDictionary = {}
emptyDictionary["Subject1"] = "Maths"
print(emptyDictionary)
emptyDictionary["Subject2"] = "Physics"
emptyDictionary["Subject3"] = "Chemistry"
emptyDictionary["Subject4"] = "Labs"
print(emptyDictionary)

#Deleting data from dictionary.
del emptyDictionary["Subject4"]
print(emptyDictionary)

#Its just key value pair.
dictDataTypes = {"int": 1, "float" : 1.25, 2.5 : "Two Point Five", 3 : "+", 5.5 : 5 }
print(dictDataTypes)

#Its just key value pair.
dictDiffDataTypes = {"One": 1.25, "float" : 5.25, 2.5 : "Two Point Five", 3 : "+", 7.9 : 2 }
print(dictDiffDataTypes)

print(dictDiffDataTypes["One"])
print(dictDiffDataTypes[7.9])

dictDiffDataTypes[2.5] = "Two and Half"
print(dictDiffDataTypes)


dictDiffDataTypes["New One"] = 1
print(dictDiffDataTypes)

del dictDiffDataTypes["One"]
print(dictDiffDataTypes)


