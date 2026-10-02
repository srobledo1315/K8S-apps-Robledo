"""
Main Entrypoint / Composition Root: Inicializa las dependencias, ensambla las capas
y arranca el servidor web.
"""
from flask import Flask
from src.infrastructure.config import AppConfig
from src.presentation.routes import create_web_blueprint

def create_app(config: AppConfig = None) -> Flask:
    if config is None:
        config = AppConfig.from_environment()

    app = Flask(__name__)
    app.config["DEBUG"] = config.debug

    # Registro de controladores (Presentation Layer)
    blueprint = create_web_blueprint(config)
    app.register_blueprint(blueprint)

    return app

if __name__ == "__main__":
    cfg = AppConfig.from_environment()
    flask_app = create_app(cfg)
    flask_app.run(debug=cfg.debug, host="0.0.0.0", port=cfg.port)
