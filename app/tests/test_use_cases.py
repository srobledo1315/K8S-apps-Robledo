"""
Unit Tests: Validación de casos de uso y lógica de dominio sin framework web.
"""
import sys
import os

# Incluir carpeta app en PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.domain.models import Greeting, HealthStatus
from src.infrastructure.config import AppConfig
from src.application.use_cases import GetGreetingUseCase, GetHealthUseCase

def test_greeting_use_case():
    config = AppConfig(
        app_env="production",
        db_username="admin",
        db_password="password",
        port=5000,
        debug=False
    )
    use_case = GetGreetingUseCase(config)
    greeting = use_case.execute()

    assert greeting.environment == "production"
    assert greeting.database_user == "admin"
    assert "¡Hola Mundo desde Kubernetes!" in greeting.format_output()
    assert "[Entorno: production | DB User: admin]" in greeting.format_output()

def test_health_use_case():
    use_case = GetHealthUseCase()
    health = use_case.execute()

    assert health.status == "healthy"
    assert health.to_dict() == {"status": "healthy"}

if __name__ == "__main__":
    test_greeting_use_case()
    test_health_use_case()
    print("✓ Todos los tests unitarios de Clean Architecture pasaron exitosamente.")
