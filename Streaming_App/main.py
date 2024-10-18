from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import asyncio
import uvicorn

app = FastAPI()

async def event_generator():
    count = 0
    while True:
        count += 1
        yield f"data: Event {count}\n\n"
        await asyncio.sleep(1)

@app.get("/")
async def root():
    return {"message": "Server-Sent Events Example"}

@app.get("/events")
async def events(request: Request):
    return StreamingResponse(event_generator(), media_type="text/event-stream")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)