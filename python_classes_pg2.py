import re

name = input("Name: ")
courses = input("input all the course you offer seperated by a comma :")
# duplicate_commas = list(set(courses))
# print(courses)
# removing_space = list(filter(lambda x: x != " ",courses))
cleaned_text = re.sub(r'[^a-zA-Z0-9,]', '', courses)
remmoved_commas = re.sub(r',+', ',', cleaned_text)
remmoved_numbers = re.sub(r'\d+', '', remmoved_commas)
