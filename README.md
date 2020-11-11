# Учебный проект от AivanF, IQ-Beat
В данном мини-проекте находится скрипт **jq.py**, который принимает на вход название файла в формате **JSON** и строку, задающую составной ключ, для доступа к значению данного ключа. Скрипт выводит значение ключа в формате **JSON** с форматированием, читабельным для человека. Строки должны быть заданы в следующем формате:

```
.key1.key2.[index].key3
```

В данном случае перед каждым элементом составного ключа должна ставиться точка, после которой используется либо название ключа **key**, либо элемент в массиве под номером **index**, индекс должен быть окружен квадратными скобками **[index]**. Стоит отметить, что весь файл выведется при запросе **"."**.

Также данный скрипт записывает лог событий, произошедших во время выполнения, в файл **jq.log**. Уровень детализации лога берется из переменной среды под названием **LOG_LEVEL**, если такой переменной нет, то используется уровень **"INFO"**. В текущей реализации доступны уровни детализации из библиотеки **logging** ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL").

# Пример использования
Тут будут описаны запросы и значение, которое вывелось на экран, а также какой вывод был в файл **jq.log**. Изначально переменная **LOG_LEVEL** не задана, поэтому используется уровень детализации **"INFO"**.

Во всех запросах используется файл **test_json.json**:
```
{
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
```

Запрос 1:
```
python jq.py test_json.json .children.[0]
```
Вывод 1 в консоль:
```
{
    "firstName": "Alice",
    "age": 6
}
```
Вывод 1 в **jq.log**:
```
2020-11-11 18:03:08,282 - jq - [INFO] - Find key: .children.[0]
2020-11-11 18:03:08,282 - jq - [INFO] - Start
2020-11-11 18:03:08,284 - jq - [INFO] - Successful finish!
```

Запрос 2:
```
python jq.py test_json.json .children.[10]
```
Вывод 2 в консоль:
```
```
Вывод 2 в **jq.log**:
```
2020-11-11 18:03:32,133 - jq - [INFO] - Find key: .children.[10]
2020-11-11 18:03:32,133 - jq - [INFO] - Start
2020-11-11 18:03:32,133 - jq - [ERROR] - list index out of range
Traceback (most recent call last):
  File "jq.py", line 41, in <module>
    json_dict = json_dict[to_real_key(i)]
IndexError: list index out of range
```

Запрос 3:
```
python jq.py test_json.json .firstName
```
Вывод 3 в консоль:
```
"Jane"
```
Вывод 3 в **jq.log**:
```
2020-11-11 18:03:55,811 - jq - [INFO] - Find key: .firstName
2020-11-11 18:03:55,812 - jq - [INFO] - Start
2020-11-11 18:03:55,812 - jq - [INFO] - Successful finish!
```

Запрос 4:
```
python jq.py test_json.json .name
```
Вывод 4 в консоль:
```
```
Вывод 4 в **jq.log**:
```
2020-11-11 18:04:16,579 - jq - [INFO] - Find key: .name
2020-11-11 18:04:16,579 - jq - [INFO] - Start
2020-11-11 18:04:16,579 - jq - [ERROR] - 'name'
Traceback (most recent call last):
  File "jq.py", line 41, in <module>
    json_dict = json_dict[to_real_key(i)]
KeyError: 'name'
```
Теперь установим переменную окружения **LOG_LEVEL** равную **"DEBUG"**.

Запрос 5:
```
python jq.py test_json.json .name
```
Вывод 5 в консоль:
```
```
Вывод 5 в **jq.log**:
```
2020-11-11 18:12:34,543 - jq - [INFO] - Find key: .name
2020-11-11 18:12:34,543 - jq - [INFO] - Start
2020-11-11 18:12:34,543 - jq - [DEBUG] - There is no key 'name'
2020-11-11 18:12:34,543 - jq - [ERROR] - 'name'
Traceback (most recent call last):
  File "jq.py", line 41, in <module>
    json_dict = json_dict[to_real_key(i)]
KeyError: 'name'
```
