"""
Application Layer: Casos de uso del sistema.
Orquesta el flujo de información entre la infraestructura y el dominio.
"""
from src.domain.models import Greeting, HealthStatus
from src.infrastructure.config import AppConfig

class GetGreetingUseCase:
    def __init__(self, config: AppConfig):
        self._config = config

    def execute(self) -> Greeting:
        return Greeting(
            message="¡Hola Mundo desde Kubernetes!",
            environment=self._config.app_env,
            database_user=self._config.db_username
        )

class GetHealthUseCase:
    def execute(self) -> HealthStatus:
        return HealthStatus(status="healthy")
