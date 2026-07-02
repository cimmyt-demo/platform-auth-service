class PlatformAuthService:
    def __init__(self, config):
        self.config=config
        self.max_tries=3

def create_service(config):
    return PlatformAuthService(config)
