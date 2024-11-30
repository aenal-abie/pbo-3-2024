from pydantic import BaseModel
from typing import List, Dict
from fastapi import APIRouter, HTTPException

class Barang(BaseModel):
    id: int
    nama: str
    jumlah: int
    harga_satuan: int

class Pembeli(BaseModel):
    id: int
    nama: str
    type: str = None

class Pembelian(BaseModel):
    pembeli_id: int
    barang: List[Dict[str, int]]

list_barang = [Barang(id=1, nama= "Baju Y", jumlah= 10,harga_satuan= 50000), 
                Barang(id = 2, nama = "Baju X", jumlah= 20, harga_satuan=53000)]
list_pembeli = [Pembeli(id=1, nama= "Budi", type = "member"),
                Pembeli(id = 2, nama = "Ali", type = ""),]

router =  APIRouter()

@router.post("/beli/")
def beli(pembelian: Pembelian):
    pembeli_id = pembelian.pembeli_id
    pembeli = next((p for p in list_pembeli if p.id == pembeli_id ), None)
    
    # pembeli = None
    # for p in list_pembeli:
    #     if(p.id == pembeli_id):
    #         pembeli = p

    if(pembeli == None):
        return HTTPException(detail="Pembeli tidak ditemukan", status_code=404)
    barang =  pembelian.barang
    total = 0
    for b in barang:
        item = next((c for c in list_barang if c.id == b["id"] ),None)
        harga = item.harga_satuan * b["jumlah"]
        total =  total + harga
        if item == None:
            return HTTPException(detail="Barang tidak ditemukan", status_code=404)
    diskon = 0
    if(pembeli.type == "member"):
        diskon = total * 0.1
    bayar = total - diskon
    return {"total" : total, "diskon": diskon, "bayar": bayar}
    

# buatkan sebuah router untuk pembelian barang POST (/beli/)
# barang tersedia dalam list barang 
# pembeli tersedia dalam list pembeli 
# barang yang di beli bisa lebih dari 1
# contoh body requestnya 
# {
#  pembeli_id: 1,barang: [{id:1, jumlah:2}, {id:2, jumlah:3}]
# }    
# jika pembeli type == "member" dapat diskon 10% dari total pemmbelian
# response:
# {total_akhir: xxxx,  diskon : xxxx, total_bayar: xxxx }