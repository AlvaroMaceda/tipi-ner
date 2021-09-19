from fastapi import FastAPI
from ner.tagger import Tagger

print("loading tagger")
tagger = Tagger()

app = FastAPI()

@app.get("/ping")
async def root():
    return "pong"

@app.get('/tag')
async def tag():
    res = tagger.foo("Bertín Osborne se fue a comer jamón Navidul a Santiago de Compostela")
    return 'this should return something with sense'
