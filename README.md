# DataAnalysis

Генерирует случайные данные связанные с поездками на такси и сохраняет эти данные в PostgreSQL. Далее с ними можно работать, например, в Redash.
## Как работает генерация:
Использует osmnx для загрузки и интерпретации небольшой части Владивостока(см. внизу), выбирая случайные две точки - начало поездки и конец соответственно. На основе этих данных рассчитывает расстояние, стоимость. Рейтинг поездки выставляется случайно.
![[misc/city_map.png]] 

## Инструкция
1. Склонируйте репозиторий
2. Создайте файл .env в котором укажите следующие переменные:
	PG_PASS = пароль к БД Такси
	PG_USER = юзер к БД Такси
	PG_URL = "postgresql+psycopg2://\${PG_USER}:${PG_PASS}@db:5432/Taxi"
	
	\#Redash переменные, взял из оф. репозитория
	COOKIE_SECRET= случайное число
	SECRET_KEY= случайное число
	DATABASE_URL="postgresql://postgres:${PG_PASS}@postgres/postgres"
	PYTHONUNBUFFERED=0
	REDASH_COOKIE_SECRET=${COOKIE_SECRET}
	REDASH_SECRET_KEY=${SECRET_KEY}
	POSTGRES_PASSWORD=${PG_PASS}
	REDASH_DATABASE_URL=${DATABASE_URL}
	REDASH_REDIS_URL="redis://redis:6379/0"
3. Запустите launch.sh
Если какие-то проблемы с launch.sh, можно самостоятельно ввести две команды (он очень маленький, просто для удобства) - первая команда задает служебную БД для Redash, вторая запускает контейнер. Для входа в Redash перейдите по localhost:5050.

## Redash
Возможности Redash:
![[misc/redash.png]]