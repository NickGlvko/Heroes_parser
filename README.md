## Как запускать тесты


### 1. Создание и активация виртуального окружения
- На `MacOS/Linux`:
``` bash
python3 -m venv venv
source venv/bin/activate
```

- На `Windows`:
``` bash
python -m venv venv
venv\Scripts\Activate.ps1
```


### 2. Установка зависимостей
Напишите в терминале следующую команду:
```
pip install -r requirements.txt
```


### 3. Запуск тестов
Все тесты находятся в папке `test/`. Для запуска, в терминале напишите:
``` bash
python -m pytest
```
Для более подробного вывода напишите:
``` bash
python -m pytest -v
```
## Как проверить работу функции


### 1. Запустите интерпритатор
``` bash
python
``` 

### 2. Поочередно выполните команды
``` python
from src.index import get_tallest_hero_by_gender_and_employment
```
``` python
hero = get_tallest_hero_by_gender_and_employment("Male", True) #Замените Male и True на необходимое
```
``` python
print(hero["name"], "-",  hero['appearance']['height'][1])
```
### 3. Для выхода из интерпритатора нажмите
- `MacOS/Linux`:
`Ctrl + D`
- `Windows`:
`Ctrl + Z + Enter`
## Структура проекта

```
├── src/

│   └── index.py          функция поиска самого высокого персонажа

├── test/

│   └── test_index.py     тесты функции

├── requirements.txt      файл для установки пакетов(зависимостей)

└── README.md
```
