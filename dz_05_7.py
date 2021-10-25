import json

companies ={}
pos_count = 0
pos_sum = 0
with open('text_7.txt') as file:
    file_lines = file.readlines()
    for line in file_lines:
        data = line.split()
        profit = float(data[2]) - float(data[3])
        companies.update({data[0]: profit})
        if profit > 0:
            pos_count += 1
            pos_sum += profit
average_profit = pos_sum / pos_count
result = [companies, {'average_profit': average_profit}]
with open('result.json', 'w') as file:
    json.dump(result, file)