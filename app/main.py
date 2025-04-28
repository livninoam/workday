# app/main.py

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from uuid import UUID
import logging
from typing import List

from app import models, schemas
from app.database import SessionLocal, engine

# --- Setup Basic Logging ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- Create database tables at startup ---
# In production, you'd use Alembic migrations instead.
models.Base.metadata.create_all(bind=engine)

# --- Initialize FastAPI app ---
app = FastAPI(
    title="Dev Environment Management API",
    description="API for managing development and staging environments",
    version="1.0.0",
)

# --- Dependency to get DB session ---
# This ensures a new session is created per request and closed automatically after.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Root route just for health check ---
@app.get("/")
def read_root():
    return {"message": "Welcome to the Dev Environment Management API"}

# --- Create a new Dev Environment ---
@app.post("/envs", response_model=schemas.DevEnvResponse)
def create_env(env: schemas.DevEnvCreate, db: Session = Depends(get_db)):
    db_env = models.DevEnv(**env.dict())
    db.add(db_env)
    db.commit()
    db.refresh(db_env)
    logger.info(f"Created new DevEnv with ID: {db_env.id}")
    return db_env

# --- Retrieve a Dev Environment by ID ---
@app.get("/envs/{env_id}", response_model=schemas.DevEnvResponse)
def get_env(env_id: UUID, db: Session = Depends(get_db)):
    env = db.query(models.DevEnv).filter(models.DevEnv.id == env_id).first()
    if not env:
        logger.warning(f"DevEnv with ID {env_id} not found.")
        raise HTTPException(status_code=404, detail="Environment not found")
    logger.info(f"Retrieved DevEnv with ID: {env_id}")
    return env

# --- Update a Dev Environment ---
@app.put("/envs/{env_id}", response_model=schemas.DevEnvResponse)
def update_env(env_id: UUID, update: schemas.DevEnvUpdate, db: Session = Depends(get_db)):
    env = db.query(models.DevEnv).filter(models.DevEnv.id == env_id).first()
    if not env:
        logger.warning(f"DevEnv with ID {env_id} not found for update.")
        raise HTTPException(status_code=404, detail="Environment not found")
    
    update_data = update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(env, key, value)

    db.commit()
    db.refresh(env)
    logger.info(f"Updated DevEnv with ID: {env_id}")
    return env

# --- Delete a Dev Environment ---
@app.delete("/envs/{env_id}")
def delete_env(env_id: UUID, db: Session = Depends(get_db)):
    env = db.query(models.DevEnv).filter(models.DevEnv.id == env_id).first()
    if not env:
        logger.warning(f"DevEnv with ID {env_id} not found for deletion.")
        raise HTTPException(status_code=404, detail="Environment not found")
    
    db.delete(env)
    db.commit()
    logger.info(f"Deleted DevEnv with ID: {env_id}")
    return {"detail": "Environment deleted successfully"}

# --- Extend duration of a Dev Environment ---
@app.patch("/envs/{env_id}/extend", response_model=schemas.DevEnvResponse)
def extend_env(env_id: UUID, extra_duration: int, db: Session = Depends(get_db)):
    env = db.query(models.DevEnv).filter(models.DevEnv.id == env_id).first()
    if not env:
        logger.warning(f"DevEnv with ID {env_id} not found for extension.")
        raise HTTPException(status_code=404, detail="Environment not found")
    
    env.duration += extra_duration
    db.commit()
    db.refresh(env)
    logger.info(f"Extended duration for DevEnv with ID: {env_id} by {extra_duration} units.")
    return env

