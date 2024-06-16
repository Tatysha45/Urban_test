import csv


def read_travel_notes(file_path):
    """Чтение данных из файла travel_notes.csv."""
    cities = {}
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Пропускаем заголовок
        for row in reader:
            name, visited_cities, want_to_visit = row[0], row[1].split(';'), row[2].split(';')
            cities[name] = {'visited': set(visited_cities), 'want_to_visit': set(want_to_visit)}
    return cities


def write_holiday_cities(cities, first_letter):
    """Запись данных в файл holiday.csv."""
    with open('holiday.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Посетили:', 'Хотят посетить:', 'Никогда не были в:', 'Следующим городом будет:'])
        for name, city_data in sorted(cities.items()):
            if name.startswith(first_letter):
                visited_cities = sorted(list(city_data['visited']))
                want_to_visit_cities = sorted(list(city_data['want_to_visit']))
                never_visited_cities = sorted(set(city_data['want_to_visit']) - city_data['visited'])
                next_city = min(never_visited_cities)
                writer.writerow(
                    [', '.join(visited_cities), ', '.join(want_to_visit_cities), ', '.join(never_visited_cities),
                     next_city])


def main():
    cities_data = read_travel_notes('travel_notes.csv')
    write_holiday_cities(cities_data, 'L')


if __name__ == '__main__':
    main()
