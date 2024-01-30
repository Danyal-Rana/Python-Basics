thisdict = {
    "saib":"apple",
    "plang":"bed",
    "kambal":"blanket",
    "basta":"bag"
}

print ("Options are: ", thisdict.keys())

a = input("Enter the Urdu word: ")

print ("The meaning of entered word is: ", thisdict.get(a))