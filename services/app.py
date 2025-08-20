from data_loader.soldier import Soldier, SoldierModelPatch, SoldierModelPost
from fastapi import FastAPI
from data_loader.data_loader import DataLoader
import os
import logging
import uvicorn


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()
dataLoader = DataLoader()


@app.post("/soldier/")
async def create(soldier_post:SoldierModelPost):
    """Create a new soldier."""
    soldier:Soldier = Soldier(
        id=soldier_post.id, 
        first_name=soldier_post.first_name, 
        last_name=soldier_post.last_name, 
        phone_number=soldier_post.phone_number, 
        rank=soldier_post.rank
        )
    return dataLoader.insert(soldier=soldier)


@app.get("/soldier/all")
async def read_all():
    """Get all soldiers."""
    return list(dataLoader.get())


@app.get("/soldier/{soldier_id}")
async def read(soldier_id:int):
    """Get a soldier by ID."""
    return list(dataLoader.get(soldier_id))


@app.patch("/soldier/{soldier_id}")
async def update_soldier(soldier_id: int, soldier_update: SoldierModelPatch):
    """Update a soldier by ID."""
    update_dict = {field: value for field, value in soldier_update.model_dump(exclude_unset=True).items()}
    return dataLoader.update(soldier_id=soldier_id,update_dict=update_dict)


@app.delete("/soldier/{soldier_id}")
async def delete_item(soldier_id: int):
    """Delete  a soldier by ID."""
    return dataLoader.delete(soldier_id=soldier_id)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("APP_PORT","27017")))  
