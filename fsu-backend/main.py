from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, PlayerStats
from typing import List
from pydantic import BaseModel

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Request model for search filters
class SearchRequest(BaseModel):
    player_name: str = None
    position: str = None
    season: str = None
    opponent: str = None
    game_type: str = None

@app.get("/")
def home():
    return {"message": "FastAPI server is running!"}

@app.get("/players")
def get_players(db: Session = Depends(get_db)):
    players = db.query(PlayerStats).all()
    return {"data": players}

@app.post("/search")
def search_players(search: SearchRequest, db: Session = Depends(get_db)):
    query = db.query(PlayerStats)

    if search.player_name:
        query = query.filter(PlayerStats.player_name.ilike(f"%{search.player_name}%"))
    if search.position:
        query = query.filter(PlayerStats.position == search.position)
    if search.season:
        query = query.filter(PlayerStats.season == search.season)
    if search.opponent:
        query = query.filter(PlayerStats.opponent == search.opponent)
    if search.game_type:
        query = query.filter(PlayerStats.game_type == search.game_type)

    results = query.all()
    return {"data": results}
