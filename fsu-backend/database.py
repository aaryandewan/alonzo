from sqlalchemy import create_engine, Column, Integer, String, Date, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./fsu_stats.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

Base = declarative_base()

class PlayerStats(Base):
    __tablename__ = "player_stats"

    id = Column(Integer, primary_key=True, index=True)
    player_name = Column(String, index=True)
    position = Column(String)
    game = Column(String)
    date = Column(Date)
    opponent = Column(String)
    game_type = Column(String)
    season = Column(String)
    
    passing_yards = Column(Float, default=0)
    passing_TDs = Column(Integer, default=0)
    rushing_yards = Column(Float, default=0)
    rushing_TDs = Column(Integer, default=0)
    receptions = Column(Integer, default=0)
    receiving_yards = Column(Float, default=0)
    receiving_TDs = Column(Integer, default=0)
    tackles = Column(Integer, default=0)
    sacks = Column(Float, default=0)
    interceptions = Column(Integer, default=0)
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
