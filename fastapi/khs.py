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

class Nilai(BaseModel):
    kode_mk: str
    nim : str
    harian: int
    uts: int
    uas: int
    na: float  = None
    grade: str =  None


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

hasil_nilai = [
    Nilai(kode_mk = "mk01", nim="00001", harian=90, uts=90, uas=100),
    Nilai(kode_mk = "mk02", nim="00001", harian=60, uts=20, uas=10),
    Nilai(kode_mk = "mk03", nim="00001", harian=70, uts=50, uas=90),
    Nilai(kode_mk = "mk01", nim="00002", harian=30, uts=20, uas=80),
    Nilai(kode_mk = "mk02", nim="00002", harian=40, uts=60, uas=50),
    Nilai(kode_mk = "mk03", nim="00002", harian=50, uts=20, uas=100)
]

def hitung_bobot(grade):
    bobot = 0
    if(grade == "A"):
        bobot = 4
    pass

def hitungGrade(nilai_akhir):
    grade = "E"
    if(nilai_akhir >= 80):
        grade = "A"
    elif (nilai_akhir>=75):
        grade = "B+"
    elif (nilai_akhir>=70):
        grade = "B"
    elif (nilai_akhir>=60):
        grade = "C+"
    elif (nilai_akhir>=50):
        grade = "C"
    elif (nilai_akhir>=30):
        grade = "D"
    return grade

# Endpoint untuk memproses KRSan
@app.get("/khs/{nim}")
def process_krsan(nim):
    nilai_mhs = []
    for nilai in hasil_nilai:
        if(nim == nilai.nim):
            nilai_akhir = (
                (nilai.harian * 0.2) +
                (nilai.uts * 0.3) +
                (nilai.uas * 0.5)
            )
            nilai.na = nilai_akhir
            nilai.grade =  hitungGrade(nilai_akhir)
            nilai_mhs.append(nilai)
    #hitung total sks
    
    return nilai_mhs
