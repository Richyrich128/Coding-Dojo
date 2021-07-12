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
#1
x[1][0] = 15
#2
students[0]["last_name"] = "Bryant"
#3
sports_directory["soccer"][0] = "Andres"
#4
z[0]["y"] = 30


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary(names):
    for i in students:
        f = i["first_name"]
        l = i["last_name"]
        print(f"first_name - {f}, last_name - {l}")

iterate_dictionary(students) 
print()
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)

def iterate_dictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])
iterate_dictionary2("first_name", students)
print()
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(some_dict):
    for i in some_dict.keys():
        print(str(len(some_dict[i])) + " " + i.upper())
        for j in some_dict[i]:
            print(j)
        print()



print_info(dojo)