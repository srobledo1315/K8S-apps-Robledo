"""
Presentation Layer: Adaptadores primarios (Controladores HTTP / Flask Blueprint).
Maneja las solicitudes HTTP entrantes y las traduce a ejecuciones de casos de uso.
"""
from flask import Blueprint, jsonify
from src.application.use_cases import GetGreetingUseCase, GetHealthUseCase
from src.infrastructure.config import AppConfig

def create_web_blueprint(config: AppConfig) -> Blueprint:
    bp = Blueprint("web", __name__)
    greeting_use_case = GetGreetingUseCase(config)
    health_use_case = GetHealthUseCase()

    @bp.route("/")
    def index():
        greeting = greeting_use_case.execute()
        return greeting.format_output(), 200

    @bp.route("/healthz")
    def healthz():
        health = health_use_case.execute()
        return jsonify(health.to_dict()), 200

    return bp
