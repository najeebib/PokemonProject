from fastapi import APIRouter, HTTPException
from classes.requests_handler import requests_handler

router = APIRouter()


@router.get('/data/migration')
def data_migration():
    return requests_handler.data_migration()
