# ordered, changeable, but don't allow duplicates

# key-value pairs

thisdict = {
    "name":"danyal",
    "year":[2022, 2023, 2024, 2025, 2026],
    "fruit":"mango",
    "city":"rohillan wali"
}

print (len(thisdict))

print(thisdict)

print (thisdict["year"])

print (thisdict["fruit"])

print (type(thisdict))

# Accessing item from a dict 

fruit = thisdict.get("fruit")

print (fruit)

# accessing keys

keys = thisdict.keys()

print(keys)

# accessing values

values = thisdict.values()

print (values)

# accessing items

items = thisdict.items()

print (items)

# changing values 

thisdict ["fruit"] = "apple"

print (thisdict)

# updating values 

thisdict.update ({"year":2020})

print (thisdict)

# dict constructor 

dict_constructor = dict( name="danyal", age=20)

print (dict_constructor)