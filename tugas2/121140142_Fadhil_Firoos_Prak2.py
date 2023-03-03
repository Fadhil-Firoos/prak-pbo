class data:
    def __init__(self, nama, nim, kelas, sks):
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        self.sks = sks

    def printOut(self):
        print("nama  : ", self.nama)
        print("nim   : ", self.nim)
        print("kelas : ", self.kelas)
        print("sks   : ", self.sks)
    
    def ubahKelas(self, ubah):
        self.kelas = ubah

        

aku = data("fadhil Firoos", "121140142", "PBO RB", 3);

print("Data Awal")
aku.printOut()

berhenti = False
while(not berhenti):
    print("\n1. ubah kelas \n2. print\n0. exit")
    menu = int(input("\nmasukan menu : "))
    if menu == 1:
        ubah = str(input("ubah kelas : "))
        aku.ubahKelas(ubah)
    elif menu == 0:
        berhenti = True
    elif menu == 2 :
        aku.printOut()