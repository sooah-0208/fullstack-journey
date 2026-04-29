from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
  # 연결방식1
  maria_db_url: str
  # 연결방식2
  maria_db_user: str
  maria_db_password: str
  maria_db_host: str
  maria_db_database: str
  maria_db_port: int

  model_config = SettingsConfigDict(
    env_file=".env",
    env_file_encoding="utf-8",
  )

settings = Settings()
