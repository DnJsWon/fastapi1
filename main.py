from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # すべてのoriginを許可するように設定（実際の展開では必要に応じて変更）
    allow_origins=["*"],
    # Cookie使用設定
    allow_credentials=False,
    # 
    allow_methods=["*"],
    # 
    allow_headers=["*"],
)

@app.get('/')
async def read_root():
    return{"Hello": "World"}

@app.get("/order/{fruits}/red")
async def read_user(fruits: str):
    if fruits == "apple":
        ee = "🍎🍎"
    elif fruits == "banana":
        ee = "🍌🍌"
    else:
        ee = "回答なし😒"
    return ee + "が注文されました。"

@app.get("/order/{fruits}/blue")
async def read_user(fruits: str):
    if fruits == "apple":
        ee = "🍏🍏"
    elif fruits == "banana":
        ee = "🍌🍌"
    else:
        ee = "回答なし😒"
    return ee + "が注文されました。"

#http://127.0.0.1:8000/order/apple?color=red
@app.get("/order/apple")
async def read_apple(color: str = Query(max_length=5)):
    if color == "red":
        ee = "🍎"
    else:
        ee = "🍏"
    return("msg", ee+"が注文されました。")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
