count = varial = 1
varial_count = 0
fixed = 5

while fixed != varial_count or fixed > varial_count:
    varial_count += 1
    varial *= count
    count += 1
    print(varial, count)

print('o fatorial de {}, é {}'.format(fixed, varial))

