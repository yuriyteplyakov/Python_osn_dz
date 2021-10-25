result = {}
with open("text_6.txt") as file:
    content = file.readlines()
    for line in content:
        sum_lessons = 0
        data = line.split()
        for el in data[1:]:
            if el != '-':
                num = '0'
                for i in el:
                    if i.isdigit():
                        num += i
                    else:
                        break
                sum_lessons += int(num)
        result.update({data[0]: sum_lessons})
print(result)