bit = 1
byte = bit * 256
k_byte = 1024 * byte

k_byte_in = int(input ('Введіть кількість Кбайт - '))
bit_out = k_byte_in * k_byte

print(f'Кількість бітів - {bit_out}')

