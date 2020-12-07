import string
input = []


with open('day6-input') as file:
    lines = file.readlines()
    answers = []
    questions = 0
    persons = 0
    for line in lines:
        if line != "\n":
            persons += 1
            answers.append(set(line.strip('\n')))
        else:
            input.append({"persons": persons, "answers": answers})
            answers = []
            persons = 0

print(input)

count = 0

for question in input:
    # persons = question['persons']
    # answer_length = len(question['answers'])
    # if persons == 1:
    #     count += len(question['answers'][0])
    # else:
    count += len(question['answers'][0].intersection(*question['answers']))

print(count)

#########################################
# with open('test-input') as file:
#     lines = file.readlines()
#     answers = ""
#     for line in lines:
#         if line != "\n":
#             answers += line.strip("\n")
#         else:
#             input.append(answers)
#             answers = ""

# alphabet_string = set(string.ascii_lowercase)

# total = 0

# for i in input:
#     print(set(i).intersection(alphabet_string))
#     total += len(set(i).intersection(alphabet_string))

# print(input)
# print(total)
