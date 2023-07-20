import datetime

print(f"{'abdo':+<10}")
print(f"{'abdo':+>10}")
print(f"{'abdo':+^10}")

# IMPORTANT
number = 3.14159
print(f"{number:.2f}")
big_number = 1000002234
print(f"{big_number:,}")

current_date = datetime.datetime.now()
print(f"{current_date:%d-%m-%Y}")
