from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, PlayerStats
from typing import List
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Query
from sqlalchemy.sql import func

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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
def search_players(
    search: SearchRequest, 
    db: Session = Depends(get_db),
    skip: int = Query(0, alias="offset"),  
    limit: int = Query(3, alias="limit")   
):
    filtered_query = db.query(PlayerStats)
    
    if search.player_name:
        filtered_query = filtered_query.filter(PlayerStats.player_name.ilike(f"%{search.player_name}%"))
    if search.position:
        filtered_query = filtered_query.filter(PlayerStats.position == search.position)
    if search.season:
        filtered_query = filtered_query.filter(PlayerStats.season == search.season)
    if search.opponent:
        filtered_query = filtered_query.filter(PlayerStats.opponent == search.opponent)
    if search.game_type:
        filtered_query = filtered_query.filter(PlayerStats.game_type == search.game_type)

    total_count = filtered_query.count()

    paginated_query = (
        filtered_query
        .order_by(
            PlayerStats.date.desc(),  
            PlayerStats.id.asc()      
        )
        .offset(skip * limit)  
        .limit(limit)
    )

    results = paginated_query.all()

    return {
        "total": total_count, 
        "data": results
    }