import json


# my_dict = (1, [2, 3, {8: 9}], 4)
#
# json_string = json.dumps(my_dict, indent=4)
#
# print(json_string)

# new_dict = json.loads(json_string)

# class MyException(BaseException):
#     pass
#
#
# a = 1
# b = 2
#
# try:
#     raise MyException
# except MyException as me:
#     print('Exception raised!')

with open('output.txt', 'r') as inp:
    json_string = json.load(inp)

print(json_string)
