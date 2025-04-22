from jinja2 import Template

data = '{%raw%}Модуль Jinja - {{name}}{%endraw%}'

template = Template(data)
print(template.render())