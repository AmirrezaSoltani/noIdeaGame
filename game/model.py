from pydantic import BaseModel

class Player(BaseModel):
    number: int
    score: int


class GameSession(BaseModel):
    mode: str
    high_score: int


class Question(BaseModel):
    answer1: str
    answer2: str
    answer3: str
    answer4: str
    # 1 easy 2 medium 3 hard
    difficulty: int
    correct_answer: int
