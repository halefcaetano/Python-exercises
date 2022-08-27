ages = 0
average = 0
oldest = 0
oldestName = ''
girl = 0
for c in range(1, 5):
    name = str(input('Write a name: ')) .strip()
    age = int(input('Age: '))
    sex = str(input('Male or female: ')) .strip()
    ages += age
    if c == 1 and sex in "Mm":
        oldest = age
        oldestName = name
    if sex in 'Mm' and age > oldest:
        oldest = age
        oldestName = name
    if sex in 'Ff' and age < 20:
        girl += 1
average = ages / 4
print('The mean age of the group is {}.' .format(average))
print('The oldest man is {} years old and is called {}.' .format(oldest, oldestName))
print('There are {} girls under the age of 20.' .format(girl))
