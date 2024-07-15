larg = float(input('largura da sua parede '))
alt = float(input('altura da sua parede '))
area = larg * alt
print('a area de sua parede é de {:.2f} m², ou seja, você precisara de {:.2} litros de tinta(supondo 1L = 2m²)'.format(area, area / 2))
