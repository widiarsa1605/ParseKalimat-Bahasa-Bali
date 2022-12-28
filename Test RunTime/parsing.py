import rule as dictionary
import os
from memory_profiler import profile
import time

@profile
def tabelCYK(kalimat, cnf, start): #membuat tabel cyk
    tabel = [] # list untuk menyimpan tabel cyk
    for index, kata in enumerate(kalimat): #perulangan sepanjang kata pada kalimat
        d1Tabel = [] #list untuk menyimpan sementara value dari dimensi pertama pada tabel
        d2Tabel = [] #list untuk menyimpan sementara value dari dimensi kedua pada tabel
        for iterasi in range(index): #perulangan sepanjang index, tidak akan berjalan apabila index bernilai 0
            d1Tabel.append([]) #memasukkan tabel kosong sebagai salah satu value dari list dimensi pertama, sesuai dengan bentuk tabel CYK
        for lhs, rhs in cnf.items(): #perulangan sepanjang index pada dictionary cnf
            if kata in rhs: #percabangan untuk kata pada list rhs
                d2Tabel.append(lhs) #memasukkan nilai lhs
        d1Tabel.append(d2Tabel) #memasukkan nilai d2Tabel pada list d1Tabel
        tabel.append(d1Tabel) #memasukkan nilai d1Tabel kedalam tabel
    for index in range(len(kalimat)-1): #perulangan sepanjang len(kalimat) dikurang 1 karena baris pertama pada tabel cyk sudah terinisiasi pada for loop sebelumnya
        for kolom in range(len(kalimat)-index-1): #perulangan untuk menambah value sesuai dengan tabel cyk yang dibutuhkan, ex: baris1 = 5, baris2 = 4, baris3 = 3, dst
            baris = index + kolom + 1 #variabel yang akan digunakan sebagai baris pada proses concentenasi pada CYK, ex: X1,2 -> 2 menunjukan value dari baris
            d2Tabel = rumusCYK(tabel, kolom, baris, cnf) #masuk ke proses konkentenasi CYK
            tabel[kolom].append(d2Tabel) #memasukkan hasil konkentenasi pada dimensi ke2 tabel cyk
    if start in tabel[0][len(kalimat)-1]:
        return True
    else:
        return False
def rumusCYK(tabel, kolom, baris, cnf): #menghitung konkentenasi cell
    iterasi = 0 #list untuk setiap iterasi
    d2Tabel = [] #list yang menyimpan value hasil perhitungan dan akan di return
    temp = [] #list sementara untuk menyimpan hasil semua cross product
    while (kolom+iterasi+1 <= baris): #perulangan sepanjang baris pada rumus cyk
        crossProduct = [] #menyimpan sementara cross product
        for index in range(len(tabel[kolom][iterasi+kolom])): #rumus cyk
            for index2 in range(len(tabel[kolom+iterasi+1][baris])): #rumus cyk
                crossProduct.append(tabel[kolom][kolom+iterasi][index] + ' ' + tabel[kolom+iterasi+1][baris][index2]) #konkentenasi 2 lhs
        temp.append(crossProduct)
        iterasi += 1
    temp = unionCrossProduct(temp, len(temp)) #melakukan union terhadap temp
    for lhs, rhs in cnf.items(): #melakukan pengecekan pada cnf
        for product in temp:
            if product in rhs:
                d2Tabel.append(lhs) #masukan value ke list d2Tabel
                break #linear search
    d2Tabel = list(dict.fromkeys(d2Tabel)) #menghilangkan duplicate
    return d2Tabel
def unionCrossProduct(temp, panjang): #melakukan union pada cross product yang bernilai lebih dari 1 sesuai rumus cyk
    if panjang == 1:
        return temp[panjang-1] #langsung mengembalikan nilai temp karena tidak perlu di unionkan
    else:
        gabung = list(set(temp[panjang-1]).union(set(unionCrossProduct(temp, panjang-1)))) #melakukan union cross product secara rekursif
        return gabung

cnf = dictionary.rule()
menuIndex = 0
ulang = True
while menuIndex != 3 and ulang:
    os.system('cls')
    print("Menu\n1. Cek Kalimat\n2. DataBase\n3. Exit\n")
    menuIndex = int(input("Masukkan Pilihan : "))
    if menuIndex == 1:
        kalimat = input("Masukkan Kalimat : ")
        startTime = time.time()
        if tabelCYK(kalimat.lower().split(' '), cnf, 'K'): 
            print("\nKalimat ini valid!")
        else: 
            print("\nKalimat ini tidak Valid!")
        print("%s execution time"%(time.time() - startTime))
        user = input("ulang? y/n\n-> ")
        if user == 'n':
            ulang = False
    elif menuIndex == 2:
        dictionary.kamusCNF()
        user = input("ulang? y/n\n-> ")
        if user == 'n':
            ulang = False
    elif menuIndex == 3:
        print("Terima Kasih!!!!")
    else:
        print("SALAH MENU!!!")
        kalimat = input("Masukkan Kalimat : ")
