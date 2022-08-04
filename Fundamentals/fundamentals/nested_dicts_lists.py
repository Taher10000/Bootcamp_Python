x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0]['last_name']='Bryant'
print(students)

sports_directory['soccer'][0]='Andres'

print(sports_directory)

z[0]['y'] ='30'
print(z)

def iterateDictionary(list1):
    for i in list1:
        for key,val in i.items():
            print(key,"-", val)

iterateDictionary(students)

def iterateDictVal(key_name,some_list):
    for i in some_list:
        print(i[key_name])


iterateDictVal('first_name',students)


def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]),key.upper())
        for val in some_dict[key]:
            print(val)

        print("\n")


printInfo(sports_directory)





