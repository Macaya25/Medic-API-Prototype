from fastapi import APIRouter, Request, HTTPException, Depends
from ..database.conf import db

healthRouter = APIRouter()


@healthRouter.get("/health", response_description="Health endpoint", summary="health")
async def health_check(DB=Depends(db)):
    try:
        DB.execute("SELECT 1")
    except:
        raise HTTPException(status_code=500, detail="errorDetail")
    else:
        return {"status": 200, "message": "Server Alive!"}
