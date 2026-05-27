
"""
numbers = [1, 2, 3, 4, 5]
squares = {str(n): n ** 2 for n in numbers}
print(squares)
"""
"""
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = {k: v for k, v in zip(keys, values)}
print(my_dict)


student1 = {
    "name": "Alex",
    "age": 42,
    "course": "Data Analytics",
    "city": "Auckland",
    "status": "Lecturer" 
}

student2 = {
    "name": "Sophia",
    "age": 29,
    "course": "Software Engineering",
    "city": "Wellington",
    "status": "Student"
}   

student3 = {
    "name": "Michael",
    "age": 35,
    "course": "Cyber Security",
    "city": "Christchurch",
    "status": "Researcher"
}   


meged_students = {
    **{k: v for k, v in student1.items() if k == "name" and "ex" in v},
    **{k: v for k, v in student2.items() if k == "name" and "ex" in v},
    **{k: v for k, v in student3.items() if k == "name" and "ex" in v}
}

print(meged_students)


x, _, z = (1, "ignore", 3)
print(_)  # Output: 1

"""


for _ in range(3):
    print("Hello", _)


#fomat large number
large_num = 1_000_000 
print(large_num)

