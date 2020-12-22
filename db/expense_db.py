from typing import Dict
from pydantic import BaseModel
from pymongo import MongoClient
from bson.json_util import dumps
from bson.json_util import loads

MONGO_URI = 'mongodb+srv://root:root@cluster0.3idi6.mongodb.net/expenses?retryWrites=true&w=majority'

client = MongoClient(MONGO_URI)

db = client['mintic_db']
collection = db['expenses']

# collection.insert_one({"username":"andres18", "title": "Nuevo TV", "value":15000, "description": "Hoy compre nuevo tv", "payment_type": "efectivo"})
# collection.insert_one({"username":"camilo24", "title": "Arriendo", "value":250000, "description": "Pago del arriendo", "payment_type": "efectivo"})
# collection.insert_one({"username":"camilo24", "title": "Play station plus", "value":35000, "description": "Pago de mensualidad de play plus", "payment_type": "tarjeta de credito"})
# collection.insert_one({"username":"andres18", "title": "Horno", "value":450000, "description": "Horno LG estaba en promoción", "payment_type": "tarjeta de credito"})

class ExpenseInDB(BaseModel):
    username: str
    title: str
    value: str
    description: str
    payment_type: str


# {"username":"andres18", "title": "compre nuevo tv", "value":15000,
#  "description": "Hoy compre nuevo tv", "payment_type": "efectivo"}
database_expenses = [
 ExpenseInDB(**{"username":"andres18", "title": "Nuevo TV", "value":15000, "description": "Hoy compre nuevo tv", "payment_type": "efectivo"}),
 ExpenseInDB(**{"username":"camilo24", "title": "Arriendo", "value":250000, "description": "Pago del arriendo", "payment_type": "efectivo"}),
 ExpenseInDB(**{"username":"camilo24", "title": "Play station plus", "value":35000, "description": "Pago de mensualidad de play plus", "payment_type": "tarjeta de credito"}),
 ExpenseInDB(**{"username":"andres18", "title": "Horno", "value":450000, "description": "Horno LG estaba en promoción", "payment_type": "tarjeta de credito"}),
]

def get_expenses_by_username(username: str):
    # match = []
    # print(database_expenses)
    # print('**********antes de buscar')
    # for x in database_expenses:
    #     print(x.username)
    #     if x.username == username:
    #         match.append(x)
    
    # return match


    results = collection.find({"username": username}, {'_id': 0})
    
    return list(results)


def register_new_expense(expense_in_db: ExpenseInDB):
   
    # database_expenses.append(expense_in_db)

    # print(database_expenses)
    # return expense_in_db


    data = {
      "username":      expense_in_db.username,
      "title":      expense_in_db.title,
      "value":      expense_in_db.value,
      "description":      expense_in_db.description,
      "payment_type":      expense_in_db.payment_type,
    }

    collection.insert_one(data)
    return expense_in_db


def get_all_expenses():
   
    # database_expenses.append(expense_in_db)

    # print(database_expenses)
    return database_expenses

