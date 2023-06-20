print ("|===================================================================================|")
print ("|------------------------------   K A L K U L A T O R ------------------------------|")
print ("|===================================================================================|")
print('Metode')
print('  + Tambah \t [+]')
print('  - Kurang \t [-]')
print('  * Kali \t [*]')
print('  / Bagi \t [/]')
print('=' * 25)
operasi = input('Pilih metode (+/-/*/(/)): ')
bilangan_1 = eval(input('Masukkan bilangan pertama: '))
bilangan_2 = eval(input('Masukkan bilangan kedua: '))
print('=' * 25)

if operasi == '+':
      hasil = bilangan_1 + bilangan_2
      print (f"Hasil operasi dari {bilangan_1} + {bilangan_2} = {hasil}")
elif operasi == '-':
  hasil = bilangan_1 - bilangan_2
  print(f"Hasil operasi dari {bilangan_1} - {bilangan_2} = {hasil}")
elif operasi == '*':
  hasil = bilangan_1 * bilangan_2
  print(f"Hasil operasi dari {bilangan_1} * {bilangan_2} = {hasil}")
elif operasi == '/':
  hasil = bilangan_1 / bilangan_2
  print(f"Hasil operasi dari {bilangan_1} / {bilangan_2} = {hasil}")
else:
  print('Tidak valid')

print ("===============================")
