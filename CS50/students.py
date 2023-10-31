import csv


def main():
    write_csv()
    read_csv()


def write_csv():
    name = input('What\'s your name? ')
    home = input('What\'s your home? ')
    with open('students.csv', 'a') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'home'])
        writer.writerow({'name': name, 'home': home})


def read_csv():
    students = []
    with open('students.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)

    for student in sorted(students, key=lambda student: student['name']):
        print(f'{student["name"]} is from {student["home"]}')


if __name__ == '__main__':
    main()
