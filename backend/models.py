from pydantic import BaseModel

class Item(BaseModel):
<<<<<<< HEAD
    name: str
=======
    name: str  # int 
>>>>>>> 6525eb1a6b70624867ebdb5e206a3f840a1f6f63
    description: str

class User(BaseModel):
    username: str
    bio: str
    
    # You can raise your hands and give the answer to the chocolate question
