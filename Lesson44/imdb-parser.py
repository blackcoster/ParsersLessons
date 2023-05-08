from colorama import Fore, Style
import requests

api_key = 'k_5k2zono2'
base_url = 'https://imdb-api.com/ru/API/'


def get_comming_soon():
    r = requests.get(f'{base_url}ComingSoon/{api_key}')
    films = r.json()['items']
    for i in range(len(films)):
        title = films[i]['title']
        date_release = films[i]['releaseState']
        genre = films[i]['genres']

        print(Fore.YELLOW + f'Название: {title}\nДата выхода: {date_release}\nЖанр: {genre}')
        print('______________________________')





def search_film(film):
    r = requests.get(f'{base_url}SearchMovie/{api_key}/{film}')

    if r.status_code == 200:
        films = r.json()['results']
        for i in range(len(films)):
            title = films[i]['title']
            desciption = films[i]['description']
            print(Fore.BLUE + f'{i + 1}. {title}')
            print(Fore.YELLOW + desciption)
            print('____________________________')
        number = input(Fore.YELLOW + 'Введите номер фильма чтобы узнать его рейтинг - ')
        if number.isdigit():
            number = int(number)
            try:
                id = films[number - 1]['id']
                r = requests.get(f'{base_url}Ratings/{api_key}/{id}')
                print(Fore.BLUE+f'Рейтинг: {r.json()["imDb"]}')
                r = requests.get(f'{base_url}Wikipedia/{api_key}/{id}')
                print(Fore.BLUE + f'Рейтинг: {r.json()["url"]}')
            except IndexError:
                print(Fore.RED+'Введен неверный номер')
        else:
            print(Fore.RED+'Вы ввели не число!')


def get_top250():
    r = requests.get(f'{base_url}Top250Movies/{api_key}')
    films = r.json()['items']
    for i in films:
        title = i['title']
        rating = i['imDbRating']
        year = i['year']
        print(Fore.BLUE + f'Название: {title}\nРейтинг: {rating}\nГод: {year}')
        print(Fore.GREEN+'___________________________________________')


def main():
    print(Fore.GREEN + Style.BRIGHT + 'IMDB бот')
    while True:
        print(Fore.BLUE + Style.NORMAL + '1. Найти фильм\n2. Список ожидаемых фильмов\n3. Топ-250')
        action = input(Fore.CYAN+'Выберите необходимое действие: ')
        match action:
            case '1':
                film = input('Название фильма: ')
                search_film(film)
            case '2':
                get_comming_soon()
            case '3':
                get_top250()
        answer = input(Fore.YELLOW + 'Выйти? ')
        if answer.title() == 'Да':
            break


main()
