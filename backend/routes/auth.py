"""
Auth routes - API xác thực PIN
"""

from fastapi import APIRouter, HTTPException
from ..schemas import PinRequest, PinResponse
from core.config import PIN_CODE

router = APIRouter()

@router.post("/verify-pin", response_model=PinResponse)
def verify_pin(request: PinRequest):
    if request.pin == PIN_CODE:
        return PinResponse(success=True, message="Xác thực thành công")
    else:
        raise HTTPException(status_code=401, detail="Mã PIN không đúng")
