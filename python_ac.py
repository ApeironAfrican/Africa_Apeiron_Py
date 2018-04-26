import Cars_Class

#lists
courses = ["Maths","Biology","Physics","Chemistry"]
courses.insert(2,"Geography")
reversed_list = courses.sort()
print(courses)
print(reversed_list)

for x in courses:
    print(x)

#sets
courses = {"Maths","Biology","Physics","Physics","Chemistry"}
life = courses.pop()
print(life)
print(len(courses))

#tuple
tuples = ("Maths","Biology","Physics","Chemistry")
print(tuples)
print(len(tuples))
print(tuples[:3])


#dictionary
dictionary = {1:"Maths",2:"Biology",3:"Physics",4:"Physics",5:["Chemistry","Power","Money"]}
print(dictionary)
print(len(dictionary))
print(dictionary.get(5)[2])
what = dictionary.values()
print(what)

#iterations
nums = [1,2,3,4,5,6,7,8,9]

for num in nums:
    print(num)

x = 0

while True:
    x += 10
    print(x)
    if(x > 100):
        break