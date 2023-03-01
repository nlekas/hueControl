from hueControl.io.objects import Io


class Light(Io):
    def __init__(self, bridge: str, user: str):
        super().__init__(bridge=bridge, user=user)
