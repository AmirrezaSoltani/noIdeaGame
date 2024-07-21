from pydantic import BaseModel


class Player(BaseModel):
    name: str
    score: int

class Question(BaseModel):
    answer1: str
    answer2: str
    answer3: str
    answer4: str
    # 1 easy 2 medium 3 hard
    difficulty:int
    correct_answer: int
