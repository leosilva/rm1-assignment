import sys
import os

perc_rate = [
    'normal',
    '001',
    '002',
    '005'
]
d_size = ['100', '1000', '10000']

def create_csv_data(rate, size):
    fileIn = open('_data-' + rate + '-' + size + '.in', 'r')
    fileOut = open('_data-' + rate + '-' + size + '.csv', 'a+')
    line = fileIn.readline().split(' ')
    del line[:2]
    last_number = line[-1].replace('\n', '')
    line.pop()
    line.append(last_number)
    fileOut.write('number')
    fileOut.write('\n')
    for n in line:
        fileOut.write(n)
        fileOut.write('\n')
    fileIn.close()
    fileOut.close()

print('Iniciando execucao...')
for p in perc_rate:
    print('% Rate: ' + p)
    for y in d_size:
        print('Data Size: ' + y)
        create_csv_data(p, y)
print('Finalizando execucao...')
