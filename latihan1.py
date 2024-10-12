class Pasien:
    def __init__(self, id, nama, nik):
        # Pastikan id, nama, dan nik wajib diisi
        if not id or not nama or not nik:
            raise ValueError("id, nama, dan nik wajib diisi.")
        
        self.id = id
        self.nama = nama
        self.nik = nik
        self.jk = None

class Pendaftaran:
    def __init__(self, pasien, tgl_daftar):
        self.pasien = pasien
        self.tgl_daftar = tgl_daftar
        self.no_antrian = None

class ListPendaftaran:
    def __init__(self):
        self.list_pendaftaran = []
    
    def pendaftaran_baru(self, pasien, tgl_daftar):
        pendaftaran = Pendaftaran(pasien, tgl_daftar)
        pendaftaran.no_antrian = len(self.list_pendaftaran) + 1 
        self.list_pendaftaran.append(pendaftaran)
        return pendaftaran.no_antrian

    def tampilkan_pendaftaran(self):
        if not self.list_pendaftaran:
            print("Belum ada pendaftaran.")
        else:
            for pendaftaran in self.list_pendaftaran:
                print(f"No Antrian: {pendaftaran.no_antrian}, Nama Pasien: {pendaftaran.pasien.nama}, JK: {pendaftaran.pasien.jk}, Tanggal Daftar: {pendaftaran.tgl_daftar}")

# Contoh penggunaan
pasien1 = Pasien(1, "Budi",  "123456789")
pasien2 = Pasien(2, "Siti",  "987654321")
pasien1.jk = "L";

daftar = ListPendaftaran()

# Daftarkan pasien baru
no_antrian1 = daftar.pendaftaran_baru(pasien1, "2024-10-12")
no_antrian2 = daftar.pendaftaran_baru(pasien2, "2024-10-12")

# Tampilkan daftar pendaftaran
daftar.tampilkan_pendaftaran()
