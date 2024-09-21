# Class Barang
class Barang:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def kurangi_stok(self, jumlah):
        if jumlah <= self.stok:
            self.stok -= jumlah
        else:
            print(f"Stok {self.nama} tidak cukup! Tersisa {self.stok}.")

    def tambah_stok(self, jumlah):
        self.stok += jumlah
        

    def __str__(self):
        return f"{self.nama} - Harga: {self.harga}, Stok: {self.stok}"


# Class Penjualan
class Penjualan:
    def __init__(self):
        self.daftar_penjualan = []

    def jual_barang(self, barang, jumlah):
        if barang.stok >= jumlah:
            self.daftar_penjualan.append((barang, jumlah))
            barang.kurangi_stok(jumlah)
        else:
            print(f"Penjualan gagal! Stok {barang.nama} tidak mencukupi.")

    def total_harga(self):
        total = 0
        for barang, jumlah in self.daftar_penjualan:
            total += barang.harga * jumlah
        return total

    def tampilkan_penjualan(self):
        print("Daftar Penjualan:")
        for barang, jumlah in self.daftar_penjualan:
            print(f"{barang.nama} - Jumlah: {jumlah}, Harga Total: {barang.harga * jumlah}")
        print(f"Total Harga: {self.total_harga()}")


# Class Pembelian
class Pembelian:
    def __init__(self):
        self.daftar_pembelian = []

    def beli_barang(self, barang, jumlah):
        self.daftar_pembelian.append((barang, jumlah))
        barang.tambah_stok(jumlah)

    def total_harga(self):
        total = 0
        for barang, jumlah in self.daftar_pembelian:
            total += barang.harga * jumlah
        return total

    def tampilkan_pembelian(self):
        print("Daftar Pembelian:")
        for barang, jumlah in self.daftar_pembelian:
            print(f"{barang.nama} - Jumlah: {jumlah}, Harga Total: {barang.harga * jumlah}")
        print(f"Total Harga: {self.total_harga()}")




# Contoh penggunaan
if __name__ == "__main__":
    # Membuat objek barang
    barang1 = Barang("Laptop", 10000000, 5)
    barang2 = Barang("Mouse", 100000, 10)

    # Menampilkan stok awal
    print(barang1)
    print(barang2)

    # Membuat objek pembelian
    pembelian = Pembelian()

    # Menambah barang ke pembelian
    pembelian.beli_barang(barang1, 2)
    pembelian.beli_barang(barang2, 3)

    # Menampilkan hasil pembelian
    pembelian.tampilkan_pembelian()


    # Menampilkan stok barang setelah pembelian
    print("\nStok setelah penjualan:")
    print(barang1)
    print(barang2)

    # Membuat objek penjualan
    penjualan = Penjualan()

    # Menambah barang ke penjualan
    penjualan.jual_barang(barang1, 2)
    penjualan.jual_barang(barang2, 3)

    # Menampilkan hasil penjualan
    penjualan.tampilkan_penjualan()

    # Menampilkan stok barang setelah penjualan
    print("\nStok setelah penjualan:")
    print(barang1)
    print(barang2)
