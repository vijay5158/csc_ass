from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from views.user_views import router as UserRouter
from views.org_views import router as OrgRouter

app = FastAPI()

# Allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(UserRouter,prefix='/user')
app.include_router(OrgRouter,prefix='/organization')



@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}