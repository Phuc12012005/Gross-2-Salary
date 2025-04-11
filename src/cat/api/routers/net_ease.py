from fastapi import APIRouter, Depends, UploadFile, File
from src.cat.api.dependencies import get_service
from src.cat.core.net_ease.services import NetEaseService
from src.cat.core.net_ease.dto import SalaryInput, SalaryOutput
import pandas as pd
import io

router = APIRouter()

@router.get("/calculate", response_model=SalaryOutput)
async def calculate_salary(data: SalaryInput, service: NetEaseService = Depends(get_service)):
    return service.calculate_salary(data)

@router.post("/bulk-calculate")
async def bulk_calculate(file: UploadFile = File(...), service: NetEaseService = Depends(get_service)):
    contents = await file.read()
    df = pd.read_excel(io.BytesIO(contents))
    results = []
    for _, row in df.iterrows():
        data = SalaryInput(gross_salary=row["gross_salary"], number_of_dependents=row["number_of_dependents"])
        result = service.calculate_salary(data)
        results.append(result.dict())
    return results
