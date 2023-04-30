### Обновления

## v0.1 
- Базовая струтура
- Модели бд

## v0.1.1
- Регистрация через мыло и выдача ссылки на авторизацию
- Сериализаторы
- Представления

## v0.2
- API (v1)

- CARD

| URL      | Ответ |
| --------- | -----|
| api/v1/card/ | Получить все карточки пользователя (GET) или добавить новую (POST) |
| api/v1/card/<int:pk> | Получить карточку по ID (GET) |
| api/v1/cardUpdate/<int:pk> | Обновить карточку по ID (PATCH) |
| api/v1/cardLink/<int:pk> | Обновить карточку по LINK (GET) (v0.3) |
| api/v1/cardDelete/<int:pk> | Удалить карточку (DELETE) (v0.6) |


- PORTFOLIO

| URL      | Ответ |
| --------- | -----|
| api/v1/portfolio/| Добавит элемент портфолио (POST) |
| api/v1/portfolio/<int:id> | Получить элемент портфолио по ID (GET) |
| api/v1/portfolioByCard/<int:id_card> | Получить все елементы по ID карточки (GET) |
| api/v1/portfolioUpdate/<int:id> | Обновить порфолио по ID (PATCH) |
| api/v1/portfolioDelete/<int:id> | Удалить порфолио по ID (DELETE) |
| api/v1/portfolioCard/ | Получить элемент портфолио по id_card (GET) (v0.3) |


- IMAGE

| URL      | Ответ |
| --------- | -----|
| api/v1/image/ | Добавить новое изображение (POST) |

- SOCIAL

| URL      | Ответ |
| --------- | -----|
| api/v1/social/ | Добавить новою инфо о социалках (POST) |
| api/v1/social/<int:id> | Получить ифно о социалках по ID (GET) |
| api/v1/socialUpdate/<int:id> | Обновить инфо по ID (PATCH) |

- COMPANY

| URL      | Ответ |
| --------- | -----|
| api/v1/company/ | Добавить инфо о компании (POST) |
| api/v1/company/<int:id> | Получить ифно по ID (GET) |
| api/v1/companyUpdate/<int:id> | Обновить инфо по ID (PATCH) |

# v0.2.1
- Небольшие изменения представлений
- небольшие изменения моделей
- небольшие изменения сериализаторов 

# v0.3 
- новые роуты для card.domain (для домена просмота карт)
- Изменеия можно посмотреть в v0.2 (API)

# v0.4 
- Добавлена станица с ифнормацие о провале авторизации
- Изменен путь ссылки редиректа 
- Добавлен мидлваре для редиректа с 404c

# v0.5
- Лендос

# v0.6
- Фикс социалок (изменения в модели Social)
- Новый api (смотреть в v0.2) путь для удлаеия карточек
- Фикс путей в апи
- Фикс middlware 404, адрес API больше не обрабатываются