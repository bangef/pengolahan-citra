from modules.grayscale import grayscale
from modules.rgb import rgb, eq

def main():
    condition = True
    while condition :
        question = int(input('Pilih menu berikut :\n1. Grafik Histogram RGB\n2. Grafik Histogram & Normalisasi Grayscale\n3. Quantization Histogram RGB\nPilih Salah satu :\n'))
        if question == 1 :
            rgb()
        elif question == 2 :
            grayscale()
        elif question == 3 :
            eq()
        else :
            condition = False
            print('Pilihan anda salah! Keluar Program')

main()