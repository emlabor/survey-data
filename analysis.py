import json

ages = []
fp = open("survey_responses.json")
data = json.load(fp)
for key in data.keys():
    ages.append(int(data[key]["age"]))
print(ages)
sum_ages = sum(ages)
sum_ages //= len(data)
print("The average age is", sum_ages)
