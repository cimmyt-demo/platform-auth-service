class PlatformAuthService:
    def __init__(self, config, environment="development"):
        self.config = config
        self.environment = environment

def create_service(config, environment="development"):
    return PlatformAuthService(config, environment)
