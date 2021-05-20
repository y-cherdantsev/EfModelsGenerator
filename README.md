# Entity Framework Models Generator

## Details
Script uses sql file with table creation code and transforms it into .NET Entity Framework model
##### Python v3.8.1
## Usage

First of all you need to start script with sql file path as an argument:
```
user@DESKTOP-JEJGU1J~: python generate_model.py sql_example.sql
```
After that in a script folder file with ***.cs*** extension will appear with file name as a table title. This file will be a model for the framework.

## Authors
* **Евгений Черданцев** - *Initial work* - [ZhekaCher](https://github.com/ZhekaCher)
