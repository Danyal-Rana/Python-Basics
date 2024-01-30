m1 = int (input ("Enter the age of first person: "))
m2 = int (input ("Enter the age of second person: "))
m3 = int (input ("Enter the age of third person: "))

if (m1>m2 and m2>m3):
    print ("First person is oldest and third person is youngest.")
elif (m1>m3 and m3>m2):
    print ("First person is oldest and second person is youngest.")
elif (m2>m1 and m1>m3):
    print ("Second person is oldest and third person is youngest.")
elif (m2>m3 and m3>m1):
    print ("Second person is oldest and first person is youngest.")
elif (m3>m2 and m2>m1):
    print ("Third person is oldesd and first person is youngest.")
elif (m3>m1 and m1>m2):
    print ("Third person is oldesd and second person is youngest.")
elif (m1==m2 and m3>m1):
    print ("Third person is oldest and other two persons are of equal age.")
elif (m1==m2 and m3<m1):
    print ("Third person is youngest and other two persons are of equal age.")
elif (m1==m3 and m2>m1):
    print ("Second person is oldest and other two persons are of equal age.")
elif (m1==m3 and m2<m1):
    print ("Second person is youngest and other two persons are of equal age.")
elif (m2==m3 and m1<m2):
    print ("First person is youngest and other two persons are of equal age.")
elif (m2==m3 and m1>m2):
    print ("First person is oldest and other two persons are of equal age.")