stuff = {"food": 15, "energy": 20, "drinks": 2}

# Access Elements from Dictionary using Get Method.
# If Key Matches with the Dictionary, It will return the Value.
print(stuff.get("food"))
print(stuff.get("energy"))
print(stuff.get("drinks"))

# If the Key is Not Matched, It will return - None
print(stuff.get("drink"))


# The items method takes the name of the dictionary and outputs a view of the key/value pairs.
print(stuff.items())

#The keys method returns a view of all of the keys in the dictionary.
print(stuff.keys())

#The Values method returns a view of all the values in the dictionary
print(stuff.values())

#The setdefault method allows us to see what the value is of a key that is in the dictionary,
# but more importantly, allows us to set a default value when a key is not in the dictionary and to add that value to the dictionary.
print(stuff.setdefault("food"))
print(stuff)
print(stuff.setdefault("sweets",20))
print(stuff)

#update method is to update the first dictionary with another dictionary.
mar_items = {"Rice": 2, "Besan": 2, "Noodles": 2, "Sugar": 1}
print(mar_items)
apr_items = {"salt":1, "Ketchup": 1}
mar_items.update(apr_items)
print(mar_items)

apr_items = {"salt":2, "Ketchup": 2}
mar_items.update(apr_items)
print(mar_items)

#Directly Updating the Value to the Key using UPDATE Method
#dict.update(key=value)
apr_items.update(salt = 5)
print(apr_items)

#Adding New Items to the Dictionary using UPDATE Method
apr_items.update(Juice = 6, Onions = 10)
print(apr_items)


#The popitem method allows us to remove the last item in a dictionary.
print(stuff)
print(stuff.popitem())
print(stuff)

#The Pop Method allows us to remove the item from the dictionary
stuff.pop("food")
print(stuff)
