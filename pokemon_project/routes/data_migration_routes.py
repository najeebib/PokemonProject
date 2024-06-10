from fastapi import APIRouter
from classes.requests_handler import requests_handler

router = APIRouter()


@router.get('/data/migrationion')
def data_migration():
    return requests_handler.data_migration()