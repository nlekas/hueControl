from hueControl.io.objects import Io
from urllib.parse import urljoin
from dataclasses import dataclass
from hueControl.common.objects import Owner, Metadata, Dimming, ColorTemperature, Color, Dynamics, SignalingStatus, LightMode, LightGradient


@dataclass
class Light:
    type: str
    id: str
    id_v1: str
    owner: Owner
    metadata: Metadata
    on: bool
    dimming: Dimming
    color_temperature: ColorTemperature
    color: Color
    dynamics: Dynamics
    alert_action_values: list[str]
    signaling_status: SignalingStatus
    mode: LightMode
    gradient: LightGradient


class LightApi(Io):
    def __init__(self, bridge: str, user: str):
        super().__init__(bridge=bridge, user=user)

    def get_lights(self):
        path = "resource/light"
        url = urljoin(self.base_url, path)
        lights = self.get(url)
        return lights

    def parse_lights(self):
        raise NotImplementedError
