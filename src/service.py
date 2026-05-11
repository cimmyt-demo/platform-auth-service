class PlatformAuthService:
    def __init__(self, config):
        self.config = config

    def authenticate(self, user_id: str) -> bool:
        """Basic authentication placeholder."""
        return bool(user_id)


def create_service(config):
    return PlatformAuthService(config)
