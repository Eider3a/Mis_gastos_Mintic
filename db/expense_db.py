from typing import Dict
from pydantic import BaseModel


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
    match = []
    print(database_expenses)
    print('**********antes de buscar')
    for x in database_expenses:
        print(x.username)
        if x.username == username:
            match.append(x)
    
    return match


def register_new_expense(expense_in_db: ExpenseInDB):
   
    database_expenses.append(expense_in_db)

    print(database_expenses)
    return expense_in_db

def get_all_expenses():
   
    # database_expenses.append(expense_in_db)

    # print(database_expenses)
    return database_expenses

