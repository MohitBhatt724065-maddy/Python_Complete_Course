#Using variables in strings.
name = "Eric"
surname = "Matthes"
full_name = f"{name} {surname}"
print(f"Hello, {full_name.title()}!")

# Note: f-string is a new feature in Python 3.6 if you are using below version you should use format() method. like full_name = "{} {}".format(name, surname)