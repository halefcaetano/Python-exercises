from datetime import date
today = date.today().year
name = str(input('Name: '))
year = int(input('Year of birth: '))
work = int(input('Work card number: '))
age = today - year
total = {'Name': name, 'Age': age, 'work': work}
if work == 0:
    for v, k in total.items():
        print(f'{v} has value {k}')
else:
    hire = int(input('Year of hire: '))
    salary = float(input('Salary: '))
    ap = today - hire
    law = 35 - ap
    apAge = law + age
    total['Hire'] = hire
    total['Salary'] = salary
    total['Age of retire'] = apAge
    for v, k in total.items():
        print(f'{v} has value {k}')

