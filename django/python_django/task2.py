
str = input("Введите строку: ")
print(f"Длина строки: {len(str)}\n")
if len(str) >= 3: print(f"\nСтрока с пропущенным 3 символом: {str[:2]+str[3:]}")
if str.find('c') != -1: print("Это строка содержит 'c'\n")
print(f"Строка без последнего символа {str[:-1]}\n")


