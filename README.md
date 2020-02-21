# Entity Framework Models Generator

## Details
Скрипт использует файл с sql кодом создания таблицы и преобразует его в модель для .NET Entity Framework
##### Python v3.8.1
## Usage

Для начала нужно запустить скрипт указав в качестве аргумента файл для преобразования:
```
user@DESKTOP-JEJGU1J~: python generate_model.py table_create.sql
```
После этого в папке со скриптом появится файл с расширением ***.cs*** и названием сгенерированным из названия таблицы. Этот файл и есть сгенерированная модель для фреймворка

## Authors
* **Евгений Черданцев** - *Initial work* - [ZhekaCher](https://github.com/ZhekaCher)