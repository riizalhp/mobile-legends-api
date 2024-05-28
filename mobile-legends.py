from fastapi import FastAPI, HTTPException

# Membuat instance dari FastAPI
app = FastAPI()

# Endpoint root
@app.get('/')
async def root():
    return [
        {"id": 1, "nama": "Endpoint Hero", "endpoint": "/hero"},
        {"id": 2, "nama": "Endpoint Hero Detail", "endpoint": "/hero/hero_detail"},
        {"id": 3, "nama": "Endpoint Role", "endpoint": "/role"},
        {"id": 4, "nama": "Endpoint Type", "endpoint": "/type"},
        {"id": 5, "nama": "Endpoint Lane", "endpoint": "/lane"},
    ]

# Data dummy untuk hero
heros = [
    {
        "id": 1, 
        "hero": "Alucard", 
        "ras": "Manusia",
        "senjata": "Pedang",
        "umur": 28,
        "quotes": "Para iblis akan bersimbah darah, cahaya hanya milik orang yang benar."
    },
    {
        "id": 2, 
        "hero": "Natalia", 
        "ras": "Manusia",
        "senjata": "Cakar",
        "umur": 18,
        "quotes": "Orang bijak sejati tak akan memberitahumu keberanannya."
    },
    {
        "id": 3, 
        "hero": "Argus", 
        "ras": "Peri",
        "senjata": "Pedang",
        "umur": 40,
        "quotes": "Kekuatan adalah keabadian."
    },
]

# Endpoint untuk mendapatkan data hero
@app.get('/hero')
async def hero_data():
    # Menyederhanakan data hero agar hanya mengandung id, hero, dan ras
    simplified_heros = [
        {"id": hero["id"], "hero": hero["hero"], "ras": hero["ras"]}
        for hero in heros
    ]
    return {
        "Message": "Success fetch heros data",
        "Data": simplified_heros
    }

# Endpoint untuk mendapatkan detail hero berdasarkan id
@app.get('/hero/{hero_id}')
async def hero_detail(hero_id: int):
    # Mencari hero berdasarkan id
    for hero in heros:
        if hero["id"] == hero_id:
            return {
                "Message": "Success fetch hero detail",
                "Data": hero
            }
    # Jika hero tidak ditemukan, mengembalikan HTTP 404
    raise HTTPException(status_code=404, detail="Hero not found")

# Endpoint untuk mendapatkan data Role
@app.get('/role')
async def role_data():
    # Data dummy role
    return {
        "Message": "Success fetch role data",
        "Data": [
            {"id": 1, "Role": "Fighter"},
            {"id": 2, "Role": "Assasin"},
            {"id": 3, "Role": "Tank"},
        ]    
    }

# Endpoint untuk mendapatkan data type
@app.get('/type')
async def type_data():
    # Data dummy type
    return {
        "Message": "Success fetch type data",
        "Data": [
            {"id": 1, "Type": "Magic"},
            {"id": 2, "Type": "Deffend"},
            {"id": 3, "Type": "Phsycal"},
        ]    
    }

# Endpoint untuk mendapatkan data lane
@app.get('/lane')
async def lane_data():
    # Data dummy lane
    return {
        "Message": "Success fetch lane data",
        "Data": [
            {"id": 1, "Lane": "EXP Lane"},
            {"id": 2, "Lane": "Gold lane"},
            {"id": 3, "Lane": "Mid Lane"},
        ]
    }
