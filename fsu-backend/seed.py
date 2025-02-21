import json
from sqlalchemy.orm import Session
from database import SessionLocal, PlayerStats
from datetime import datetime

mock_data = [
    {
        "player_name": "Jordan Travis",
        "position": "QB",
        "game": "FSU vs Miami",
        "date": "2024-10-05",
        "opponent": "Miami",
        "game_type": "conference",
        "season": "2024",
        "passing_yards": 310,
        "passing_TDs": 3,
        "rushing_yards": 45,
        "rushing_TDs": 0,
        "receptions": 0,
        "receiving_yards": 0,
        "receiving_TDs": 0,
        "tackles": 0,
        "sacks": 0,
        "interceptions": 0
    },
    {
        "player_name": "Keon Coleman",
        "position": "WR",
        "game": "FSU vs Clemson",
        "date": "2024-09-21",
        "opponent": "Clemson",
        "game_type": "conference",
        "season": "2024",
        "passing_yards": 0,
        "passing_TDs": 0,
        "rushing_yards": 12,
        "rushing_TDs": 0,
        "receptions": 8,
        "receiving_yards": 134,
        "receiving_TDs": 2,
        "tackles": 0,
        "sacks": 0,
        "interceptions": 0
    },
    {
        "player_name": "Jared Verse",
        "position": "DL",
        "game": "FSU vs Miami",
        "date": "2024-10-05",
        "opponent": "Miami",
        "game_type": "conference",
        "season": "2024",
        "passing_yards": 0,
        "passing_TDs": 0,
        "rushing_yards": 0,
        "rushing_TDs": 0,
        "receptions": 0,
        "receiving_yards": 0,
        "receiving_TDs": 0,
        "tackles": 7,
        "sacks": 2.5,
        "interceptions": 0
    },
    {
        "player_name": "Johnny Wilson",
        "position": "WR",
        "game": "FSU vs Florida",
        "date": "2024-11-25",
        "opponent": "Florida",
        "game_type": "regular",
        "season": "2024",
        "passing_yards": 0,
        "passing_TDs": 0,
        "rushing_yards": 0,
        "rushing_TDs": 0,
        "receptions": 5,
        "receiving_yards": 76,
        "receiving_TDs": 1,
        "tackles": 0,
        "sacks": 0,
        "interceptions": 0
    },
    {
        "player_name": "Trey Benson",
        "position": "RB",
        "game": "FSU vs NC State",
        "date": "2024-10-15",
        "opponent": "NC State",
        "game_type": "conference",
        "season": "2024",
        "passing_yards": 0,
        "passing_TDs": 0,
        "rushing_yards": 128,
        "rushing_TDs": 2,
        "receptions": 3,
        "receiving_yards": 26,
        "receiving_TDs": 0,
        "tackles": 0,
        "sacks": 0,
        "interceptions": 0
    },
    {
        "player_name": "Jaheim Bell",
        "position": "TE",
        "game": "FSU vs Wake Forest",
        "date": "2024-10-28",
        "opponent": "Wake Forest",
        "game_type": "regular",
        "season": "2024",
        "passing_yards": 0,
        "passing_TDs": 0,
        "rushing_yards": 0,
        "rushing_TDs": 0,
        "receptions": 4,
        "receiving_yards": 58,
        "receiving_TDs": 1,
        "tackles": 0,
        "sacks": 0,
        "interceptions": 0
    },
    {
        "player_name": "Fabien Lovett",
        "position": "DL",
        "game": "FSU vs Pittsburgh",
        "date": "2024-10-21",
        "opponent": "Pittsburgh",
        "game_type": "regular",
        "season": "2024",
        "passing_yards": 0,
        "passing_TDs": 0,
        "rushing_yards": 0,
        "rushing_TDs": 0,
        "receptions": 0,
        "receiving_yards": 0,
        "receiving_TDs": 0,
        "tackles": 5,
        "sacks": 1.5,
        "interceptions": 0
    },
    {
        "player_name": "DJ Lundy",
        "position": "LB",
        "game": "FSU vs Boston College",
        "date": "2024-09-30",
        "opponent": "Boston College",
        "game_type": "regular",
        "season": "2024",
        "passing_yards": 0,
        "passing_TDs": 0,
        "rushing_yards": 0,
        "rushing_TDs": 0,
        "receptions": 0,
        "receiving_yards": 0,
        "receiving_TDs": 0,
        "tackles": 9,
        "sacks": 1,
        "interceptions": 1
    }
]


def seed_database():
    db: Session = SessionLocal()
    
    for item in mock_data:
        player_stat = PlayerStats(
            player_name=item["player_name"],
            position=item["position"],
            game=item["game"],
            date=datetime.strptime(item["date"], "%Y-%m-%d"),  # Convert string to Date format
            opponent=item["opponent"],
            game_type=item["game_type"],
            season=item["season"],
            passing_yards=item["passing_yards"],
            passing_TDs=item["passing_TDs"],
            rushing_yards=item["rushing_yards"],
            rushing_TDs=item["rushing_TDs"],
            receptions=item["receptions"],
            receiving_yards=item["receiving_yards"],
            receiving_TDs=item["receiving_TDs"],
            tackles=item["tackles"],
            sacks=item["sacks"],
            interceptions=item["interceptions"]
        )
        db.add(player_stat)
    
    db.commit()
    db.close()
    print("✅ Database seeded successfully!")

if __name__ == "__main__":
    seed_database()
