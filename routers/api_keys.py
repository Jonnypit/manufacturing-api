from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
from dependencies import get_db
from models import APIKey
from pydantic import BaseModel
import os

router = APIRouter()

def get_fernet():
    key = os.getenv("FERNET_KEY")
    return Fernet(key.encode())

class ApiKeyCreate(BaseModel):
    name: str
    raw_key: str

@router.post("/api-keys")
def store_api_key(data: ApiKeyCreate, db: Session = Depends(get_db)):
    f = get_fernet()
    encrypted =f.encrypt(data.raw_key.encode())
    new_key = APIKey(name=data.name, encrypted_key=encrypted.decode())
    db.add(new_key)
    db.commit()
    db.refresh(new_key)
    return {
            "id": new_key.id, 
            "name": new_key.name, 
            "message": "API key stored securely"
            }

@router.get("/api-keys/{key_id}")
def retrieve_api_key(key_id: int, db: Session =Depends(get_db)):
    api_key = db.query(APIKey).filter(APIKey.id == key_id).first()
    if api_key is None:
        raise HTTPException(status_code=404, detail="API key not found")
    f = get_fernet()
    decrypted = f.decrypt(api_key.encrypted_key.encode())
    return {
            "id": api_key.id,
            "name": api_key.name,
            "key": decrypted.decode()
            }
    

