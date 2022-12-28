iterasi = 0 #variabel untuk iterasi variabel baru yang terbentuk pada konversi CNF
NonTerminal = {} # list untuk Nonterminal pada rule
HasilProduksi = [] # List untuk ruas kanan pada rule
cnfRule = []
    
def cnf(cfg): #fungsi untuk mengkonversi CNF
    global iterasi
    global HasilProduksi
    global NonTerminal

    for index, rule in enumerate(cfg): # perulangan sebanyak rule pada cfg, ini digunakan untuk memecah rule menjadi 2 bagian yaitu ruas kiri(non terminal) dan ruas kanan
        RuleSplit = rule.split(" -> ") # metode split untuk memecah setiap item pada list variabel cfg dengan separator " -> "
        NonTerminal[RuleSplit[0]] = index # memasukkan nilai RuleSplit item pertama kedalam list NonTerminal
        HasilProduksi.append(RuleSplit[1].split(" | "))
    for index, rule in enumerate(HasilProduksi):
        for step in range(1, len(HasilProduksi[index])):
            # print(cnf[index][1][i])
            key = HasilProduksi[index][step]
            j = step - 1 
            while j >= 0 and key < HasilProduksi[index][j]:
                HasilProduksi[index][j + 1] = HasilProduksi[index][j]
                j = j - 1
            HasilProduksi[index][j + 1] = key
    for index, part in enumerate(HasilProduksi):# Perulangan sebanyak item pada list HasilProduksi, ini digunakan untuk memecah lagi HasilProduksi kedalam beberapa subHasilProduksi dari rule
        temp = [] #list untuk menyimpan hasil konversi tiap rule
        temp = unitProduction(part) #memanggil fungsi unitProduction
        HasilProduksi[index] = temp #mengubah value list HasilProduksi suatu index dengan nilai variabel temp yang sudah berisikan hasil konversi cnf suatu rule
    
    for key, val in NonTerminal.items():
        NonTerminal[key] = HasilProduksi[val]
    return NonTerminal




def reduceProduction(unit): #fungsi untuk menyederhanakan rule yang memiliki banyak non terminal
    global HasilProduksi
    global NonTerminal
    global iterasi

    temp = [] #list untuk menyimpan sementara hasil konversi rule kedalam bentuk cnf
    newName = ["X"] #X didefinisikan sebagai variabel baru yang akan dibentuk
    if len(unit) > 2: #mengecek apakah panjang unit lebih besar dari 2, salah apabila panjang unit telah bernilai 1
        temp.append(unit[0] +" "+ unit[1]) #menggabungkan unit[0] dengan unit[1] dibarengi dengan spasi sebagai calon hasil produksi baru
        newName[0] = newName[0] + str(iterasi) #menggabungkan newName[0] dengan nilai iterasi(ex.X1, untuk iterasi = 1) sebagai calon nonTerminal baru
        if temp not in HasilProduksi: #jika nilai temp yang telah dibentuk belum ada di Hasil Produksi
            NonTerminal[newName[0]] = len(NonTerminal) #masukkan nilai newName sebagai nonterminal baru
            HasilProduksi.append(temp) #masukkan nilai temp sebagai HasilProduksi baru
            iterasi += 1 #increament nilai iterasi
            temp = reduceProduction(newName + unit[2:]) #rekursif
        else:
            temp = reduceProduction([list(NonTerminal.keys())[HasilProduksi.index(temp)]] + unit[2:]) #rekursif apabila nilai temp sudah ada pada HasilProduksi
        return temp #return nilai Temp
    else:
        return [" ".join(unit)] #melakukan return apabila len(unit) bernilai 2


def unitProduction(part): #fungsi untuk menghilangkan unit production dan memanggil fungsi reduceProduction
    temp = [] #list untuk menyimpan sementara hasil konversi
    for unit in part: #perulangan sebanyak rule hasil produksi suatu non terminal
        if len(unit.split()) == 1: #untuk rule dengan 1 bagian/ tanpa spase
            if unit in NonTerminal.keys(): #untuk rule pada hasil produksi yang merupakan bagian dari non terminal(salah apabila itu adalah terminal)
                temp = temp + unitProduction(HasilProduksi[NonTerminal[unit]]) #rekursif
            else:
                return part #melakukan return apabila unit adalah terminal
        elif len(unit.split()) > 2: #untuk rule yang memiliki lebih dari 2 bagian
            temp = temp + reduceProduction(unit.split()) #memanggil fungsi reduceProduction
        else:
            temp.append(unit) #untuk rule yang telah sesuai aturan
    return temp #return nilai temp



