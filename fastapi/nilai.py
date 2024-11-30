from fastapi import APIRouter
from pydantic import BaseModel, Field

# Router untuk endpoint nilai
nilai_router = APIRouter()

# Model input untuk nilai
class NilaiMahasiswa(BaseModel):
    nilai_harian: float = Field(..., ge=0, le=100, description="Nilai harian (0-100)")
    nilai_uts: float = Field(..., ge=0, le=100, description="Nilai UTS (0-100)")
    nilai_uas: float = Field(..., ge=0, le=100, description="Nilai UAS (0-100)")

# Endpoint untuk menghitung nilai akhir
@nilai_router.post("/hitung-nilai-akhir/")
async def hitung_nilai_akhir(nilai: NilaiMahasiswa):
    nilai_akhir = (
        (nilai.nilai_harian * 0.2) +
        (nilai.nilai_uts * 0.3) +
        (nilai.nilai_uas * 0.5)
    )

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

    return {
        "nilai_harian": nilai.nilai_harian,
        "nilai_uts": nilai.nilai_uts,
        "nilai_uas": nilai.nilai_uas,
        "nilai_akhir": round(nilai_akhir, 2),
        "grade": grade
    }
