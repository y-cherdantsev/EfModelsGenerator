types = {'integer': 'int?',
         'text': 'string',
         'timestamp': 'DateTime?',
         'boolean': 'bool?',
         'double precision': 'double?',
         'unknown': 'UnknownType'}


class ClassElement:
    name = ''
    type = 'unknown'


def main():
    template = 'namespace DataMigrationSystem.Models.Web.TradingFloor' \
               '{' \
               '[Table("$TABLE_NAME")]' \
               'public class $CLASS_NAME' \
               '{' \
               '$CONTAINER' \
               '}' \
               '}'

    import sys
    file = open(sys.argv[1], 'r', encoding='utf-8')
    text = file.read()

    # table_naming
    pre_table_name = text[0:text.index('(')] \
        .replace('\n', '') \
        .replace('create', '') \
        .replace('table', '') \
        .replace(' ', '') \
        .split('.')
    table_name = pre_table_name[len(pre_table_name) - 1]  # Ready
    template = template.replace('$TABLE_NAME', table_name)
    template = template.replace('$CLASS_NAME', modify_to_camel(table_name))

    # fields_creating
    inner_fields = text[text.index('(') + 1:text.index(')')].replace('\n', '').split(',')
    class_fields = []
    for inner_field in inner_fields:
        inner_field = inner_field.strip()
        class_field = ClassElement()
        class_field.name = inner_field.split(' ')[0]
        for t in types:
            if inner_field.__contains__(t):
                class_field.type = t
                break
        class_fields.append(class_field)
    return template


# for field in inner_fields:
#     print(field+"\n")

def modify_to_camel(text):
    text = text[0].upper() + text[1:]
    while text.__contains__('_'):
        text = text[:text.index('_')] + text[text.index('_') + 1:][0].upper() + text[text.index('_') + 2:]
        continue
    return text


print(main())
