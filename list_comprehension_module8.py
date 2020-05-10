nums = [4, 8, 15, 16, 23, 42]
double_nums = [i*2 for i in nums]

nums = range(11)
squares = [i**2 for i in nums]

nums = [4, 8, 15, 16, 23, 42]
add_ten = [i+10 for i in nums]

nums = [4, 8, 15, 16, 23, 42]
divide_by_two = [i/2 for i in nums]

nums = [4, 8, 15, 16, 23, 42]
parity = [i%2 for i in nums]

names = ["Elaine", "George", "Jerry", "Cosmo"]
greetings = ['Hello, '+name for name in names]

names = ["Elaine", "George", "Jerry", "Cosmo"]
first_character = [name[0] for name in names]

names = ["Elaine", "George", "Jerry", "Cosmo"]
lengths = [len(name) for name in names]

booleans = [True, False, True]
opposite = [not b for b in booleans]

names = ["Elaine", "George", "Jerry", "Cosmo"]
is_Jerry = [name == 'Jerry' for name in names]

nums = [5, -10, 40, 20, 0]
greater_than_two = [i>2 for i in nums]

nested_lists = [[4, 8], [15, 16], [23, 42]]
product = [i*j for i,j in nested_lists]

nested_lists = [[4, 8], [16, 15], [23, 42]]
greater_than = [i>j for i,j in nested_lists]

nested_lists = [[4, 8], [16, 15], [23, 42]]
first_only = [i for i,j in nested_lists]

a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
sums = [i+j for i,j in list(zip(a,b))]

a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
quotients = [j/i for i,j in list(zip(a,b))]

capitals = ["Santiago", "Paris", "Copenhagen"]
countries = ["Chile", "France", "Denmark"]
locations = [cap+', '+coun for cap,coun in list(zip(capitals,countries))]

names = ["Jon", "Arya", "Ned"]
ages = [14, 9, 35]
users = ['Name: '+name+', Age: '+str(age) for name,age in list(zip(names,ages))]

a = [30, 42, 10]
b = [15, 16, 17]
greater_than = [i>j for i,j in list(zip(a,b))]
