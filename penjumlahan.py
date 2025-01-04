class Penjumlahan():

    def __init__(self, nilai_awal, nilai_akhir):
        self.nilai_awal = nilai_awal
        self.nilai_akhir = nilai_akhir

    def hitung(self):
        jumlah = 0
        for i in range(self.nilai_awal, self.nilai_akhir):
            jumlah += i
        return jumlah

hitung1 = Penjumlahan(1, 10000)
print(hitung1.hitung())


hitung2 = Penjumlahan(10, 100000000)
print(hitung2.hitung())
