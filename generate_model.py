types = {'integer': 'int?',
         'bigint': 'long?',
         'smallint': 'int?',
         'text': 'string',
         'timestamp': 'DateTime?',
         'date': 'DateTime?',
         'boolean': 'bool?',
         'numeric': 'double?',
         'double precision': 'double?',
         'real': 'double?',
         'decimal': 'double?',
         'bigserial': 'long?',
         'serial': 'int?',
         'smallserial': 'int?',
         'unknown': 'UnknownType'}


class ClassElement:
    key = False
    name = ''
    type = 'unknown'


def main():
    template = 'using System;\n' \
               'using System.ComponentModel.DataAnnotations;\n' \
               'using System.ComponentModel.DataAnnotations.Schema;\n\n' \
               'namespace SomeNamespace\n' \
               '{\n' \
               '\t[Table("$TABLE_NAME")]\n' \
               '\tpublic class $CLASS_NAME\n' \
               '\t{\n' \
               '$CONTAINER\n' \
               '\t}\n' \
               '}\n'

    import sys
    file = open(sys.argv[1], 'r', encoding='utf-8')
    text = file.read()

    # table_naming
    pre_table_name = text[0:text.index('(')] \
        .replace('\n', '') \
        .replace('create', '') \
        .replace('table', '') \
        .replace('-- auto-generated definition', '') \
        .replace(' ', '') \
        .split('.')
    table_name = pre_table_name[len(pre_table_name) - 1]  # Ready

    # fields_parsing
    inner_fields = text[text.index('(') + 1:text.index(')')].replace('\n', '').split(',')
    class_fields = []
    for inner_field in inner_fields:
        inner_field = inner_field.strip()
        class_field = ClassElement()
        class_field.name = inner_field.split(' ')[0]
        if inner_field.__contains__('primary key'):
            class_field.key = True
        for t in types:
            if inner_field.__contains__(t):
                class_field.type = t
                break
        class_fields.append(class_field)

    # generating result
    template = template.replace('$TABLE_NAME', table_name)
    template = template.replace('$CLASS_NAME', modify_to_camel(table_name))
    container = '\t\t'
    for class_field in class_fields:
        if class_field.key:
            container += '[Key] '
        container += '[Column(\"' + class_field.name + '\")] public ' \
                     + types[class_field.type] \
                     + ' ' \
                     + modify_to_camel(class_field.name) \
                     + '{get; set;}\n\t\t'
    template = template.replace('$CONTAINER', container)
    file = open(modify_to_camel(table_name) + ".cs", 'w', encoding='utf-8')
    file.write(template)
    print("Model successfully created and wrote to the file \'" + modify_to_camel(table_name) + ".cs\'")


def modify_to_camel(text):
    text = text[0].upper() + text[1:]
    while text.__contains__('_'):
        text = text[:text.index('_')] + text[text.index('_') + 1:][0].upper() + text[text.index('_') + 2:]
        continue
    return text


main()