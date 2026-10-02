"""
Infrastructure Layer: Adaptadores secundarios que interactúan con el entorno,
sistema operativo, variables de entorno del contenedor y configuración.
"""
import os
from dataclasses import dataclass

@dataclass(frozen=True)
class AppConfig:
    app_env: str
    db_username: str
    db_password: str
    port: int
    debug: bool

    @classmethod
    def from_environment(cls) -> "AppConfig":
        return cls(
            app_env=os.environ.get("APP_ENV", "unknown"),
            db_username=os.environ.get("DB_USERNAME", "none"),
            db_password=os.environ.get("DB_PASSWORD", ""),
            port=int(os.environ.get("PORT", "5000")),
            debug=os.environ.get("DEBUG", "False").lower() in ("true", "1", "yes")
        )
