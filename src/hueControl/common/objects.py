from dataclasses import dataclass
from enum import Enum
from typing import List


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
