from typing import Dict
from pydantic import BaseModel 

class UserInDB(BaseModel): 
    username: str 
    password: str 
    expenses: int

database_users = Dict[str, UserInDB]
database_users = {
    "camilo24" : UserInDB(**{"username":"camilo24",
    "password": "root",
    "expenses":120000}),

    "andres18" : UserInDB(**{"username":"andres18",
    "password": "root",
    "expenses":15000})
}


def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def register_user(user_in_db: UserInDB):
    # setattr(user_in_db, 'expenses', 0)
    # user_in_db['expenses'] = 0
    print(user_in_db)
    # Si es != None significa que el usuario existe entonces no lo puedo registrar
    if get_user(user_in_db.username) != None:
      return None
    
    # Agrego al diccionario y lo retorno
    # database_users[user_in_db.username] = user_in_db
    database_users[user_in_db.username] = UserInDB(**{"username":user_in_db.username,
    "password": user_in_db.password,
    "expenses": 0})

    # database_users[user_in_db.username] = {
    #   "username": user_in_db.username, 
    #   "password": user_in_db.password, 
    #   "expenses": 0, 
    # }
    print(database_users)
    return user_in_db

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db


