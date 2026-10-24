from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
from models import Order
from pydantic import BaseModel

class OrderCreate(BaseModel):
    part_id: int
    quantity: int
    status: str
    date: str

router = APIRouter()

@router.get("/orders")
def get_orders(db: Session = Depends(get_db)):
    orders = db.query(Order).all()
    return orders

@router.get("/orders/{order_id}")
def get_orders(order_id: int, db:Session = Depends(get_db)):
    order = db.query(Order).filter(order.order_id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.post("/orders")
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    new_order = Order(
        part_id     =order.part_id,
        quantity    =order.quantity,
        status      =order.status,
        date        =order.date
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

@router.put("/orders/{order_id}")
def update_order(order_id: int, order: OrderCreate, db: Session = Depends(get_db)):
    existing_order = db.query(Order).filter.Order.order_id == order_id.first()
    if existing_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    existing_order.part_id     = order.part_id
    existing_order.quatity      = order.quantity
    existing_order.status       = order.status
    existing_order.date         = order.date
    db.commit()
    db.refresh(existing_order)
    return existing_order

@router.delete("/orders/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(order.order_id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(order)
    db.commit()
    return{"message": f"Order {order_id} deleted"}

