from fastapi import APIRouter, HTTPException
from classes.requests_handler import requests_handler

router = APIRouter()


@router.get('/data/migrationion')
def data_migration():
    try:
        return requests_handler.data_migration()
    except Exception:
        raise HTTPException(500, detail="Server error")