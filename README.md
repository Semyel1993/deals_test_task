Deals test-task
=====================

Этот README описывает весь процесс установки, запуска и работы с сервисом.

---------------------

### Создание окружения для локальной разработки

##### Копирование файлов репозитория на локальную машину

```
$ git clone https://github.com/Semyel1993/deals_test_task.git
$ cd deals_test_task
```

##### Создание и запуск контейнеров

```
$ docker-compose up 
```
Данная команда так же выполнит скрипт *entrypoint.sh*, который в свою очередь применит миграции и создаст суперпользователя, поэтому вам останется только использовать сервис

_**Примечание:** Созданный суперпользователь имеет следующие данные:_
```
username: admin
email: admin@mail.com
password: 123
```


##### Проверка доступности панели администратора

Открыть в браузере страницу [http://0.0.0.0:8000/admin/](http://0.0.0.0:8000/admin/) и выполнить вход в систему

---------------------

### Использование сервиса

Сервис имеет всего 2 эндпоинта: 
```
POST http://0.0.0.0:8000/api/deals-upload/
GET http://0.0.0.0:8000/api/deals-get/
```

**POST** запрос принимает один аргумент *deals*, который является файлом в формате .csv и возвращает ответ *OK* или *Error*

**GET** запрос возвращает “response” со списком из 5 клиентов, потративших наибольшую сумму за весь период.

Каждый клиент описывается следующими полями:

- *username* - логин клиента;
- *spent_money* - сумма потраченных средств за весь период;
- *gems* - список из названий камней, которые купили как минимум двое из списка "5 клиентов, потративших наибольшую сумму за весь период", и данный клиент является одним из этих покупателей.
