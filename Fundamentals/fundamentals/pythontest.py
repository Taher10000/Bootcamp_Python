print(type(24))
print(type(3.9))
print(type(3j))
print("Hello World")
first_name = "taher"
last_name = "mac"
age=23
print("Hi i am %s %s and i am %d old" %(first_name, last_name, age))
print(f"my name is {first_name} {last_name} and i am {age} years old")
print(first_name.upper())
print(first_name.capitalize())
people = ['mark', 'john', 'cam']
print(people[2])
people.append("jerry")
print(people)

person = [
    {
    'first_name': 'Taher',
    'last_name' : 'Mac',
    'age':'23'
},
{
    'first_name': ['Jay','zee'],
    'last_name' : 'Mac',
    'age':'27'
}

]
print(person[1]['first_name'][1])


brothers=['tyle','joe','curts']
for brother in brothers:
    print(brother)


for index in range(3):
    print(brothers[index])

import random

def randomize_list(new_list):
    return_list = []
    for items in new_list:
        random_num = random.randint(0,len(new_list)-1)
        item = new_list[random_num]
        return_list.append(item)
    return return_list

print(randomize_list(brothers))


def add(num1, num2=10,num3=2):
    x= num1+ num2 +num3
    return x

print(add(1))