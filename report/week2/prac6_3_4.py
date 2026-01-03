from dataclasses import dataclass

@dataclass
class DatabaseConfig:
    host: str
    port: int
    username: str
    password: str
    database: str
    timeout: int = 30    # 기본
    pool_size: int = 5   # 기본

config = DatabaseConfig(
    host="[localhost](http://localhost)",
    port=3306,
    username="admin",
    password="secret123",
    database="myapp"
)
print(config)