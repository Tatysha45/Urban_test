import csv


def write_holiday_cities(first_letter):
    visited_cities = set()
    wish_list_cities = set()

    with open('travel_notes.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            name, visited, wish_list = row[0].split(',')

            if name.startswith(first_letter):
                visited_cities.update(visited.split(';'))
                wish_list_cities.update(wish_list.split(';'))

    all_cities = visited_cities | wish_list_cities
    not_visited_cities = wish_list_cities - visited_cities
    next_city = sorted(not_visited_cities)[0] if not_visited_cities else None

    with open('holiday.csv', 'w') as file:
        file.write(f"Посетили: {', '.join(sorted(visited_cities))}\n")
        file.write(f"Хотят посетить: {', '.join(sorted(wish_list_cities))}\n")
        file.write(f"Никогда не были в: {', '.join(sorted(not_visited_cities))}\n")
        file.write(f"Следующим городом будет: {next_city}\n")


# Пример работы функции
write_holiday_cities('L')
