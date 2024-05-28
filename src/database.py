import asyncpg
import os
from fastapi import FastAPI

from .config import get_config

config = get_config()

DATABASE_URL = config.database_url

async def get_db():
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        yield conn
    finally:
        await conn.close()
