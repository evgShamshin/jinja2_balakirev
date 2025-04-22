from jinja2 import Template


name = 'user_name'
surname = 'user_surname'

tm = Template('Hello {{name.upper()}} {{surname.lower()}}!')
msg = tm.render(name=name, surname=surname)
print(msg)