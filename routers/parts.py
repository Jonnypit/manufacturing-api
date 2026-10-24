from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
from models import Part
from pydantic import BaseModel

class PartCreate(BaseModel):
    name: str
    material: str
    quantity: int
    price: float

router = APIRouter()

@router.get("/parts") #same as @app.get but uses router since this is a router file
def get_parts(db: Session = Depends(get_db)): #dependency injection, opens DB connection
    parts = db.query(Part).all() #SQL equivalent of SELECT * FROM parts
    return parts #returns all rows as JSON

@router.get("/parts/{part_id}")
def get_parts(part_id: int, db: Session = Depends(get_db)):
    part = db.query(Part).filter(Part.part_id == part_id).first() # SQL equivalent of WHERE part_id = 42 
    # .first() — returns the first match or None
    if part is None: # if nothing found in DB
        raise HTTPException(status_code=404, detail="Part not found") # returns "Part not found" error
    return part

@router.post("/parts")
def create_part(part: PartCreate, db: Session = Depends(get_db)):  # Pydantic validates incoming JSON first
    new_part = Part( # creates a new SQLAlchemy object from the validated data
        name=part.material,
        quantity=part.quantity,
        price=part.price)
    db.add(new_part)  # stages it for insertion
    db.commit() # writes it to the database
    db.refresh(new_part) # refreshes the object to get the auto-generated part_id
    return new_part # sends back the created part including its new ID

@router.put("/parts/{part_id}")
def update_part(part_id: int, part: PartCreate, db: Session = Depends(get_db)):
    existing_part = db.query(Part).filter.Part.part_id == part_id.first() # First finds the existing record — same as GET one part
    if existing_part is None: # 404 if part doesn't exist
        raise HTTPException(status_code=404, detail="Part not found")
    existing_part.name      = part.name # Updates each field with the new values
    existing_part.material  = part.material
    existing_part.quantity  = part.quantity
    existing_part.price     = part.price
    db.commit() # saves the changes
    db.refresh(existing_part) # gets the updated record
    return existing_part # sends back the updated part

@router.delete("/parts/{part_id}")
def delete_part(part_id: int, db: Session = Depends(get_db)):
    part = db.query(Part).filter(part.part_id == part_id).first() # Finds the part first — same pattern as GET and PUT
    if part is None: #404 if part doesn't exist 
        raise HTTPException(status_code=404, detail="Part not found")
    db.delete(part) #marks it for deletion
    db.commit() # removes it from the database
    return {"message": f"Part {part_id} deleted"} # confirms deletion to the caller

    
