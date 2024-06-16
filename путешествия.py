import pandas as pd
import csv

data = {
    'Name': ['Ivan', 'Sergey', 'Alexey', 'Victor', 'Natalia', 'Tatiana'],
    'Cities Visited': [
        ['Moscow', 'St.Petersburg', 'Luxembourg'],
        ['St.Petersburg', 'Nizhny Novgorod', 'Pinsk'],
        ['Moscow', 'Lyubertsy', 'Dubai'],
        ['Rostov', 'Nizhny Novgorod', 'Yekaterinburg'],
        ['Stavropol', 'Saratov', 'Tomsk'],
        ['Kiev', 'Minsk', 'Vladivostok']
    ],
    'Wants to Visit': [
        ['Cairo', 'Levan', 'Minsk'],
        ['Rostov', 'Odintsovo', 'Minsk'],
        ['Krasnodar', 'Naberezhnye Chelny', 'Kazan'],
        ['Tokyo', 'Beijing', 'Murmansk'],
        ['Paris', 'Kazan', 'Volgograd'],
        ['Moscow', 'Paris', 'Arkhangelsk']
    ]
}

df = pd.DataFrame(data)

df.to_csv('travel_notes.csv', index=False)


def read_travel_notes(file_path):
    cities = {}
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            name, visited_cities, want_to_visit = row[0], row[1].split(';'), row[2].split(';')
            cities[name] = {'visited': set(visited_cities), 'want_to_visit': set(want_to_visit)}
    return cities


def write_holiday_cities(cities, first_letter):
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
    write_holiday_cities(cities_data, 'S')


if __name__ == '__main__':
    main()
