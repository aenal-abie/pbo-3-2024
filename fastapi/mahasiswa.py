from pydantic import BaseModel
from typing import List
class Mk(BaseModel):
    kode_mk: str
    nama_mk: str
    sks: int
    semester_ke : int

class Mahasiswa(BaseModel):
    nim:str
    nama: str
    alamat: str
    kode_prodi: str

class Prodi(BaseModel):
    kode: str
    nama: str

class Krs(BaseModel):
    kode_mk:str
    nim:str

class Krsan(BaseModel):
    nim: str
    mk:List[str]
