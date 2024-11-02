from jinja2 import Environment, FileSystemLoader
persons = [
    {'name': 'Bigdon', 'old': 12, 'weight': 122},
    {'name': 'Nazik', 'old': 42, 'weight': 1122},
    {'name': 'Kamazik', 'old': 2, 'weight': 52}
]
file_Loader = FileSystemLoader('templates')
env = Environment(loader=file_Loader)

tm = env.get_template('main.htm')
msg = tm.render(users=persons)

print(msg)