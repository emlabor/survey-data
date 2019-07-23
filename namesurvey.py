import json

surveys_by_name = {}
add_survey = 'yes'

while add_survey == 'yes':
    survey = {}
    survey["name"] = input("What's your name? ")
    survey["age"] = input("What's your age? ")
    survey["hometown"] = input("What's your hometown? ")
    survey["twitter"] = input("What's your twitter handle? ")
    #print(survey)
    surveys_by_name[survey["name"]] = survey
    add_survey = input("Would you like to add a survey response? (yes/no) ").lower()

print("Thanks for your responses!")
# print(surveys_by_name)

fp = open("survey_responses.json", "r")
old_surveys = json.load(fp)
# print(old_surveys)
for key in surveys_by_name.keys():
    old_surveys[key] = surveys_by_name[key]
# print(old_surveys)
fp.close()

fp = open("survey_responses.json", "w")
json.dump(old_surveys, fp)
fp.close()
