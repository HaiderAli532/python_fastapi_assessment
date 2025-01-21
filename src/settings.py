from pydantic import BaseSettings, Field

#for all your env variables
class Settings(BaseSettings):
    database_url: str = Field(env="DATABASE_URL", default="postgresql://postgres:Netsolpk1@localhost:5432/freelance_community")  

settings = Settings()
