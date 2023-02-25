from shopbridge import create_app
from config import ProductionConfig,DevelopmentConfig

app = create_app(config_class=DevelopmentConfig)