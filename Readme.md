![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
## Skyentodo

Это веб-приложение — планировщик задач, который позволит работать с целями и
отслеживать прогресс по ним.

### Функционал:

1. Вход/регистрация/аутентификация через вк.
2. Создание целей.
- Выбор временного интервала цели с отображением кол-ва дней до завершения цели.
- Выбор категории цели (личные, работа, развитие, спорт и т. п.) с возможностью добавлять/удалять/обновлять категории.
- Выбор приоритета цели (статичный список minor, major, critical и т. п.).
- Выбор статуса выполнения цели (в работе, выполнен, просрочен, в архиве).
3. Изменение целей.
- Изменение описания цели.
- Изменение статуса.
- Дать возможность менять приоритет и категорию у цели.
4. Удаление цели.
- При удалении цель меняет статус на «в архиве».
5. Поиск по названию цели.
6. Фильтрация по статусу, категории, приоритету, году.
7. Выгрузка целей в CSV/JSON.
8. Заметки к целям.
9. Все перечисленный функции реализованы в телеграм-боте.

### Стек:
python3.11, Django, DRF, Postgres

### Запуск:
Локально - в дирректории проекта выполнить команду:
docker-compose up --build

На сервере сборка и деплой осуществляются автоматически с помощью github actions
