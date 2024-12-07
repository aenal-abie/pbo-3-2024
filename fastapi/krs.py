from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

# Definisi model
class Mk(BaseModel):
    kode_mk: str
    nama_mk: str
    sks: int
    semester_ke: int

class Mahasiswa(BaseModel):
    nim: str
    nama: str
    alamat: str
    kode_prodi: str

class Prodi(BaseModel):
    kode: str
    nama: str

class Krs(BaseModel):
    kode_mk: str
    nim: str

class Krsan(BaseModel):
    nim: str
    mk: List[str]

# Data in-memory untuk simulasi database
mks = [
    Mk(kode_mk="mk01", nama_mk="Algoritma", sks=3, semester_ke=1),
    Mk(kode_mk="mk02", nama_mk="Matematika", sks=2, semester_ke=1),
    Mk(kode_mk="mk03", nama_mk="Bahasa Inggris", sks=2, semester_ke=1),
]

mahasiswa = [
    Mahasiswa(nim="00001", nama="Budi", alamat="Jl. Mawar", kode_prodi="TI"),
    Mahasiswa(nim="00002", nama="Ani", alamat="Jl. Melati", kode_prodi="TI"),
]

prodi = [
    Prodi(kode="TI", nama="Teknik Informatika"),
    Prodi(kode="SI", nama="Sistem Informasi"),
]



# Endpoint untuk memproses KRSan
@app.post("/krsan/")
def process_krsan(data: Krsan):
    krs = []

    # Validasi mahasiswa
    if not any(m.nim == data.nim for m in mahasiswa):
        return {"error": "Mahasiswa tidak ditemukan"}
    mhs = next((m for m in mahasiswa if m.nim == data.nim ), None)

    # Validasi mata kuliah
    invalid_mk = [kode for kode in data.mk if not any(mk.kode_mk == kode for mk in mks)]
    if invalid_mk:
        return {"error": f"Mata kuliah tidak valid: {invalid_mk}"}

    # Tambahkan ke KRS
    for kode in data.mk:
        mk = next((p for p in mks if p.kode_mk == kode ), None)
        krs.append(mk)
        
    hasil =  { 
            "mahasiswa" : mhs,
            "mk" : krs
        }

    return hasil

