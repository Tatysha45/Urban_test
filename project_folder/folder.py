import json


def employees_rewrite(sort_type):
    with open('employees.json', 'r') as file:
        data = json.load(file)

    if sort_type not in ["firstName", "lastName", "department", "salary"]:
        raise ValueError('Bad key for sorting')

    sorted_employees = sorted(data['employees'], key=lambda x: x[sort_type])

    output_file_name = f'employees_{sort_type}_sorted.json'
    with open(output_file_name, 'w') as outfile:
        json.dump(sorted_employees, outfile, indent=4)


try:
    employees_rewrite('lastName')
except ValueError as e:
    print(e)
