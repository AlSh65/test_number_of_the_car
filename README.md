
# test_number_of_the_car

тестовое задание Intern Backend Developer REST-API (Python) 
1. Развернуть локальную базу данных PostgreSQL с созданием архитектуры под следующие пункты задания
2. Реализовать следующий метод: GET | /PLATE/GENERATE (Генерация государственных номеров автомобилей)
	1. Метод должен принимать следующие параметры: token, amount
	2. Где: token – Bearer-токен авторизации, amount – количество государственных 	номеров автомобилей в ответе
	3. Примечание: token – любой формат, amount – int or null, если не указано, вернуть 	один номер. Если не указан токен, вернуть соответствующий ответ клиенту.
3. Реализовать следующий метод: GET | /PLATE/GET (Получение государственных номеров автомобилей)
	1. Метод должен принимать следующие параметры: token, id
	2. Вернуть в JSON формате все данные по записи
	3. Где: token – Bearer-токен авторизации, id – идентификатор записи о государственном 	номере авто
	4. Примечание: token – любой формат, id – любой (Предпочтительно uuid4 ). Если 	не указан токен, вернуть соответствующий ответ клиенту.
4. Реализовать следующий метод: POST | /PLATE/ADD (Добавление государственных номеров автомобилей в базу данных)
	1. Метод должен принимать следующие параметры: token, plate
	2. Перед добавлением должна проводиться проверка на корректность 	государственного номера автомобиля
	3. Где: token – Bearer-токен авторизации, plate – государственный номер
	4. Примечание: token – любой формат, plate – str. Оба значения обязательны к передаче, если не указаны, вернуть соответствующие ответы клиенту.

**Стек:**
- Python 
- Django 
- Postgresql
- djangorestframework 

## Запуск проекта 

##### 1) Клонировать репозиторий

    git clone https://github.com/AlSh65/test_number_of_the_car.git

##### 2) Создать виртуальное окружение

    python -m venv venv
    
##### 3) Активировать виртуальное окружение
    source venv/bin/activate

##### 4) Устанавливить зависимости:

    pip install -r requirements.txt

##### 5) build docker

    docker-compose build
    
##### 6) Сделать миграции

    docker-compose run --rm django-app sh -c "python3 manage.py migrate"

##### 7) Создать суперпользователя 
    docker-compose run --rm django-app sh -c "python3 manage.py createsuperuser"

##### 8) Поднять сервер
	docker-compose up

Для проверки работоспособности, помимо тестов, был использован Postman
##### POST PLATE/ADD
   ![plate_add](https://user-images.githubusercontent.com/94260936/212915147-d0ca36c9-6a8c-465d-a08e-bf5732682fbd.png)
##### GET PLATE/GENERATE
   ![plate_generate](https://user-images.githubusercontent.com/94260936/212915349-44097dc9-26ec-4eef-bc3e-3b4eedb64c1b.png)
##### GET PLATE/GET
   ![plate_get](https://user-images.githubusercontent.com/94260936/212915539-503c432a-e18b-471b-9f28-9df71ecb287f.png)


