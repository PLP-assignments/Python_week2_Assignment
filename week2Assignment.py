#create an empty list named myList
myList=[]

#Append the following elements to my_list: 10, 20, 30, 40.
myList.append(10)
myList.append(20)
myList.append(30)
myList.append(40)

#Insert the value 15 at the second position in the list (index 1)
myList.insert(1,15)

#Extend myList with another list: [50, 60, 70].
myList.extend([50,60,70])

#Remove the last element from myList.
#del myList[-1]
myList=myList [:-1]

#Sort myList in ascending order
myList.sort()

#Find and print the index of the value 30 in myList.
index30=myList.index(30)


print("Index of 30 in my list: ",index30)