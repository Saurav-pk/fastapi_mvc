from fastapi import FastAPI
from controllers import note_controller, user_controller

app = FastAPI()

app.include_router(note_controller.router, prefix="/notes", tags=["notes"])
app.include_router(user_controller.router, prefix="/users", tags=["users"])

