firm = {}
n = int(input("Введіть кількість фірм про які бажаєте внести дані: ")) 
all_assets = 0
min = 0
max = 0

for i in range(n):
    name = str(input("Введіть назву фірми: "))
    assets = int(input(f'Введіть оборотні активи для {name}: '))
    firm[name] = assets
    all_assets += firm[name]
    if i == 0:
        min = firm[name]
        max = firm[name]
        min_name = name
        max_name = name
    if firm[name] < min:
        min = firm[name]
        min_name = name
    if firm[name] > max:
        max = firm[name]
        max_name = name
        
print("\nСумарні активи",all_assets)
print("Фірма з найменшими обороними активами: ", min_name)
print("Фірма з найбільшими обороними активами: ", max_name)
