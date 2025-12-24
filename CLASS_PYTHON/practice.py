# from collections import Counter


# student_profile = {
#     "id": 101,
#     "name": "Himal",
#     "age": 20,
#     "is_active": True,
#     "contact": {
#         "email": "himal@example.com",
#         "phone": "9800000000",
#         "address": {
#             "city": "Kathmandu",
#             "country": "Nepal"
#         }
#     },
#     "skills": ["Python", "Django", "JavaScript"],
#     "projects": {
#         "chat_app": {
#             "status": "in_progress",
#             "tech_stack": ["Django", "DRF", "React"],
#             "stars": 5
#         },
#         "portfolio": {
#             "status": "completed",
#             "tech_stack": ["HTML", "CSS", "JavaScript"],
#             "stars": 4
#         }
#     },
#     "scores": {
#         "DSA": 78,
#         "OS": 72,
#         "DBMS": 81
#     }
# }

# names = [1 , 2 , 4 , 4 , 4 , 4 , 5, 1 , 2, "Ram" , "Shyam" , "Hari"]
# count = Counter(names)
# print(count)
# print(type(count))


# value = Counter(student_profile)
# print(value)


# for items in value.items():
#     print(items)
    


#Default Dictionary 

# Dict = {}
# Dict['a'] = Dict['a'] + 12

# print(Dict)


# to solve this problem we introduce the default dictionary

# from collections import defaultdict


# Dict = defaultdict(str)
# Dict['a'] = Dict['a'] + "Himal"

# print(Dict['a'])
# double ended queue => deque  both side bata enter ra both side bata remove garna milxa yesma

# from collections import deque

# queue = deque("himal")
# queue.append(234from collections import deque

# queue = deque("himal")
# queue.append(234)
# print(queue)
# queue.append(34)
# print(queue)


# while queue:
#     val = queue.pop()
#     print(val)

# print(queue)
# queue.append(34)
# print(queue)


# while queue:
#     val = queue.pop()
#     print(val)



# from collections import namedtuple

# Point = namedtuple('himal', 'Fi b c')
# p1 = Point(1,4,5)
# print(p1)

# a , b , c = p1.Fi , p1.b , p1.c
# print(a,b,c)


from collections import Counter

aDict = {
    'a': 10,
    'b': 20,
    'c': 30
}

count = Counter(aDict.keys()) # this will count the occurrence of each key
print(count['a'])  # repr object le Counter vanera print garxa tara yo chai int ho

print(type(count))