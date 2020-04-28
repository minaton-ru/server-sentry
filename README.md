# Сервер на bottle с логгированием в Sentry

В коде есть проверка на запуск локально или на Heroku.

Сервер делает только две вещи:  
по адресу /fail заканчивает работу с ошибкой 500  
по адресу /success возвращает 200 ОК и текст success

Проект на Heroku:  
https://fathomless-bastion-95774.herokuapp.com/success  
https://fathomless-bastion-95774.herokuapp.com/fail
