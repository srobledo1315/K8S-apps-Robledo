"""
Domain Layer: Contiene las entidades puras y reglas de negocio del sistema.
No depende de frameworks web, bases de datos ni bibliotecas externas.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Greeting:
    message: str
    environment: str
    database_user: str

    def format_output(self) -> str:
        return f"{self.message} [Entorno: {self.environment} | DB User: {self.database_user}]\n"

@dataclass(frozen=True)
class HealthStatus:
    status: str = "healthy"

    def to_dict(self) -> dict:
        return {"status": self.status}
