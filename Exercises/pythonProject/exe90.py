name = str(input('Enter the name: '))
media = int(input('Enter the score: '))
if media >= 7:
    status = 'approved'
else:
    status = 'disapproved'
situation = {'name': name, 'media': media, 'status': status}
print(f"Student's name: {situation['name']}")
print(f"The final average: {situation['media']}")
print(f"The student is: {situation['status']}")
