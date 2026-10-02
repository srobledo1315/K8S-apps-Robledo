import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from src.main import create_app
from src.infrastructure.config import AppConfig

config = AppConfig.from_environment()
app = create_app(config)

if __name__ == '__main__':
    app.run(debug=config.debug, host='0.0.0.0', port=config.port)
