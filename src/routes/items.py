from fastapi import APIRouter, Depends, HTTPException
from asyncpg import exceptions
from ..database import get_db
from ..models.item import Item

router = APIRouter()

@router.post("/items/", response_model=Item)
async def create_item(item: Item, db = Depends(get_db)):
    query = "INSERT INTO items (name, description) VALUES ($1, $2) RETURNING id, name, description"
    try:
        result = await db.fetchrow(query, item.name, item.description)
        if not result:
            raise HTTPException(status_code=500, detail="Failed to create item")
        return result
    except exceptions.UniqueViolationError:
        raise HTTPException(status_code=400, detail="Item with the given name already exists")
    except exceptions.ForeignKeyViolationError:
        raise HTTPException(status_code=400, detail="Foreign key constraint failed")
    except exceptions.PostgresError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@router.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int, db = Depends(get_db)):
    query = "SELECT id, name, description FROM items WHERE id = $1"
    try:
        result = await db.fetchrow(query, item_id)
        if not result:
            raise HTTPException(status_code=404, detail="Item not found")
        return result
    except exceptions.PostgresError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
