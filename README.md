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

- PORTFOLIO

| URL      | Ответ |
| --------- | -----|
| api/v1/portfolio/| Добавит элемент портфолио (POST) |
| api/v1/portfolio/<int:id> | Получить элемент портфолио по ID (GET) |
| api/v1/portfolioByCard/<int:id_card> | Получить все елементы по ID карточки (GET) |
| api/v1/portfolioUpdate/<int:id> | Обновить порфолио по ID (PATCH) |
| api/v1/portfolioDelete/<int:id> | Удалить порфолио по ID (DELETE) |

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