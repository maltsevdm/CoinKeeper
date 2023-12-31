from fastapi import APIRouter

from db import schemas
from db import core

router = APIRouter()


@router.get('/add')
async def add_operation(operation: schemas.TransactionCreate):
    return await core.add_operation(operation)
