from string import Template

name = "Alice"
age = 25
template = Template("My name is $name and I'm $age years old.")
formatted_string = template.substitute(name=name, age=age)
print(formatted_string)
