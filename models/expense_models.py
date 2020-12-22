from pydantic import BaseModel

class ExpenseIn(BaseModel):
    username: str
    title: str
    value: str
    description: str
    payment_type: str
    
    
class UserOut(BaseModel):
    username: str
    expenses: int