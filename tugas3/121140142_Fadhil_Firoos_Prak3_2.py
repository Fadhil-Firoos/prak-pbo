class Manusia:
    # atribut global
    spesies = 'Homo sapiens'
    
    def __init__(self, nama, umur, jurusan):
        # atribut publik
        self.nama = nama
        self.jurusan = jurusan
        # atribut protected
        self._umur = umur
        # atribut private
        self.__alamat = '-'
    
    # fungsi publik
    def getUmur(self):
        return self._umur
    
    # fungsi protected
    def _ubahUmur(self, umur_baru):
        self._umur = umur_baru   
    def _ubahAlamat(self, alamat_baru):   
        # mengubah atribut private (tidak dapat diakses langsung pada main program)
        # misal orang1.__alamat = 'Jakarta'
        # akan menyebabkan AttributeError: 'Manusia' object has no attribute '__alamat'
        self.__alamat = alamat_baru
    
    # fungsi instance private
    # fungsi ini hanya dapat di akses di dalam class tidak dapat di akses di luar class atau di main program
    def __printAlamat(self):
        print(f"Alamat {self.__alamat}")
    
    def info(self):
        print('Nama:', self.nama)
        print('Umur:', self._umur)
        self.__printAlamat()
        print('Spesies:', self.spesies)
        print("")
        
        
        
# membuat objek dari class 
mhs1 = Manusia('Andi', 25, "Teknik Informatika")
mhs1.info()

# mengakses atribut kelas
print('Spesies:', Manusia.spesies)
print("")

# mengakses atribut instance publik
print('Nama:', mhs1.nama)
print("")

# mengubah atribut instance protected
mhs1._ubahUmur(26)
print('Umur:', mhs1.getUmur())
print("")

mhs1._ubahAlamat("bandung")
mhs1.info()
