from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional, Dict
from urllib.parse import urljoin

from tomlkit.items import Bool

from hueControl.io.objects import Io


class Rtype(Enum):
    device = 1
    bridge_home = 2
    room = 3
    zone = 4
    light = 5
    button = 6
    relative_rotary = 7
    temperature = 8
    light_level = 9
    motion = 10
    entertainment = 11
    grouped_light = 12
    device_power = 13
    zigbee_bridge_connectivity = 14
    zigbee_connectivity = 15
    zgp_connectivity = 16
    bridge = 17
    zigbee_device_discovery = 18
    homekit = 19
    matter = 20
    matter_fabric = 21
    scene = 22
    entertainment_configuration = 23
    public_image = 24
    auth_v1 = 25
    behavior_script = 26
    behavior_instance = 27
    geofence = 28
    geofence_client = 29
    geolocation = 30
    smart_scene = 31


@dataclass
class Metadata:
    name: str
    image: Rtype
    rid: str
    rtype: Rtype

    def __post_init__(self):
        if self.image != 24:
            raise ValueError("Image must be a public_image rtype")
        if not 1 <= len(self.name) <= 32:
            raise ValueError("Name must be between 1 and 32 characters")


@dataclass
class Group:
    rid: str
    rtype: Rtype


@dataclass
class Dimming:
    brightness: float
    min_dim_level: float

    def __post_init__(self):
        if not 0 < self.brightness <= 100:
            raise ValueError("Dimming-Brightness must be between 0 and 100")
        if not 0 < self.min_dim_level <= 100:
            raise ValueError("Dimming-Min_dim_level must be between 0 and 100")


@dataclass
class ColorTemperature:
    mirek: int
    mirek_valid: bool
    mirek_min: int
    mirek_max: int

    def __post_init__(self):
        if not 152 < self.mirek < 501:
            raise ValueError("ColorTemperature-Mirek must be between 153 and 500")
        if not 152 < self.mirek_min < 501:
            raise ValueError("ColorTemperature-Mirek_Min must be between 153 and 500")
        if not 152 < self.mirek_max < 501:
            raise ValueError("ColorTemperature-Mirek_Max must be between 153 and 500")


@dataclass
class CieXy:
    x: float
    y: float

    def __post_init__(self):
        if not 0 <= self.x <= 1:
            raise ValueError("CieXy-X gamut position must be between 0 and 1")
        if not 0 <= self.y <= 1:
            raise ValueError("CieXy-Y gamut position must be between 0 and 1")


@dataclass
class Gamut:
    red: CieXy
    green: CieXy
    blue: CieXy


class GamutType(Enum):
    A = 1
    B = 2
    C = 3
    other = 4


@dataclass
class Color:
    xy: CieXy
    gamut: Gamut
    gamut_type: GamutType


class DynamicStatus(Enum):
    dynamic_palette = 1
    none = 2


@dataclass
class Dynamics:
    status: DynamicStatus
    status_values: List[DynamicStatus]
    speed: float
    speed_valid: bool


class SceneMode(Enum):
    interpolated_palette = 1
    interpolated_palette_mirrored = 2
    random_pixelated = 3


class GradientMode(Enum):
    interpolated_palette = 1
    interpolated_palette_mirrored = 2
    random_pixelated = 3


@dataclass
class LightGradient:
    points: List[CieXy]
    mode: GradientMode
    points_capable: int
    mode_values: List[GradientMode]
    pixel_count: int


class LightEffect(Enum):
    sparkle = 1
    fire = 2
    candle = 3
    no_effect = 4


@dataclass
class Effects:
    effect: LightEffect
    status_values: List[LightEffect]
    status: LightEffect
    effect_values: LightEffect


@dataclass
class Target:
    rid: str
    rtype: Rtype


@dataclass
class Scene:
    type: str
    id: str
    id_v1: str
    metadata: Metadata
    on: bool
    dimming: Dimming
    color_temperature: ColorTemperature
    color: Color
    dynamics: Dynamics
    alert_action_values: list[str]
    mode: SceneMode
    gradient: LightGradient


class SceneApi(Io):
    def __init__(self, bridge: str, user: str):
        super().__init__(bridge=bridge, user=user)

    def get_scene(self) -> List[Scene]:
        path = "resource/scene"
        url = urljoin(self.base_url, path)
        scene = self.get(url)
        return self.parse_scene(scene)

    def parse_scene(self, payload: Dict) -> List[Scene]:
        l = Scene(
            type="kdsjldkjf",
            id="kldsjflksj",
            id_v1="slkdjflksd",
            target=Target(
                rid="dskljflskdj",
                rtype="skdjfldsjfl",
            )
        )
        return [l]

    def put_scene(self, lights: List[Scene]) -> bool:
        raise NotImplementedError
