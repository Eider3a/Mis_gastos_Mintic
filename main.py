from db.user_db import UserInDB
from db.user_db import update_user, get_user, register_user
from db.transaction_db import TransactionInDB
from db.transaction_db import save_transaction
from models.user_models import UserIn, UserOut
from models.transaction_models import TransactionIn,TransactionOut

# Comando para correr el programa.
# uvicorn main:api --reload


import datetime
from fastapi import FastAPI
from fastapi import HTTPException

# Rest API
api = FastAPI()


#########################################################
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080", "http://localhost:8081", "http://127.0.0.1:6060",
    "https://cajero-app-1987.herokuapp.com", "https://eider-arango-cajero-ui.herokuapp.com:6060",
    "https://eider-arango-cajero-ui.herokuapp.com", "https://mis-gastos-frontend.herokuapp.com"
]
api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)
#########################################################



@api.post("/user/register/")
async def register_new_user(user_in: UserIn):
    user_in_db = register_user(user_in)
    if user_in_db == None:
        raise HTTPException(status_code=404,
            detail="Ya existe un usuario registrado con ese username en la db")
    return {"Registrado": True}

@api.post("/user/auth/")
async def auth_user(user_in: UserIn):
    user_in_db = get_user(user_in.username)
    if user_in_db == None:
        raise HTTPException(status_code=404,
            detail="El usuario no existe")
    if user_in_db.password != user_in.password:
        return {"Autenticado": False}
    return {"Autenticado": True}

@api.get("/user/expenses/{username}")
async def get_total_expenses(username: str):
    user_in_db = get_user(username)
    if user_in_db == None:
        raise HTTPException(status_code=404,
            detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())
    print(user_in_db)
    return user_out

# @api.get("/user/balance/{username}")
# async def get_balance(username: str):
#     user_in_db = get_user(username)
#     if user_in_db == None:
#         raise HTTPException(status_code=404, detail="El usuario no existe")
#     user_out = UserOut(**user_in_db.dict())
#     return  user_out

# @api.put("/user/transaction/")
# async def make_transaction(transaction_in: TransactionIn):
#     user_in_db = get_user(transaction_in.username)
#     if user_in_db == None:
#         raise HTTPException(status_code=404,
#             detail="El usuario no existe")
#     if user_in_db.balance < transaction_in.value:
#         raise HTTPException(status_code=400,
#             detail="Sin fondos suficientes")
#     user_in_db.balance = user_in_db.balance - transaction_in.value
#     update_user(user_in_db)
#     transaction_in_db = TransactionInDB(**transaction_in.dict(),
#                             actual_balance = user_in_db.balance)
#     transaction_in_db = save_transaction(transaction_in_db)
#     transaction_out = TransactionOut(**transaction_in_db.dict())
#     return transaction_out