import requests
import pymorphy2

# Task 1
print(requests.get('http://pochta.ru'))


# Task 2

print("Чтобы закончить, напишите: стоп")
city_name = input("Введите город, в котором хотите получить прогноз:\n")
token = 'token'  # вставьте свой токен
while city_name != "стоп":
    try:
        request = requests.get("http://api.openweathermap.org/data/2.5/weather?" + "appid=" + token + "&q=" + city_name
                               + '&units=metric&lang=ru')
        data = request.json()
        morph = pymorphy2.MorphAnalyzer()
        word = morph.parse(data['name'])[0]
        result_city = word.inflect({'loct'}).word.capitalize()
        print(f"Погода в {result_city} сейчас: {data['weather'][0]['description'].capitalize()}")
        print(f"Температура: {data['main']['temp']}°C")
        print(f"Ощущается как: {data['main']['feels_like']}°C")
        print(f"Влажность: {data['main']['humidity']}%")
        print(f"Давление: {data['main']['pressure']} мм рт.ст.")
    except Exception as e:
        print("К сожалению,ничего не нашёл по вашему запросу. Попробуйте ещё раз.")
    city_name = input("\n")




