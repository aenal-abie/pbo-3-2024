class User:
    def __init__(self, nama, jk) -> None:
        self.nama = nama
        self.jk = jk
    
    def login(self,password): 
        if(password==123):
            print("Password anda benar")
        else:
            print("Password anda salah")

class Pasien(User):
    def __init__(self, nik, nama, jk):
        self.nik = nik
        super().__init__(nama, jk)
        
        
class Dokter(User):
    def __init__(self, id, nama, jk, spesialisasi,):
        self.spesialisasi = spesialisasi
        self.id = 10
        super().__init__(nama, jk)

    def login(self,id, password):
        if(id == self.id and password == 123):
            print("Anda berhasil login")
        else: 
            print("Anda gagal login")
    
    

pasien1 = Pasien(12211,  "Budi", "L")
dokter1 = Dokter(10,"dr. Budi", "L", "Anak")

print(pasien1.jk)
pasien1.login(124)
print(dokter1.nama)
dokter1.login(10, 123)