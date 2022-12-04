from typing import Union
from fastapi import FastAPI, Depends, Path, HTTPException
from sqlalchemy.orm import Session
import database
import models
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get('/')
def read_root():
    return {'Hello': 'World'}


@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    return {'item_id': item_id, 'q': q}


@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {'item_name': item.name, 'item_id': item_id}


@app.get('/product')
def read_product_list(db: Session = Depends(database.get_db)):
    result = db.query(models.Product).all()
    return {
        'status_code': 200,
        'data': result
    }


@app.get('/product/{product_no}')
def read_product(product_no: str,
                 db: Session = Depends(database.get_db)):
    result = db.query(models.Product).filter(
        models.Product.product_no == product_no).first()

    if result is None:
        raise HTTPException(status_code=404, detail='Product No에 맞는 상품이 없습니다.')

    return {
        'status_code': 200,
        'data': result
    }
