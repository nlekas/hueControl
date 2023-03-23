from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional
from urllib.parse import urljoin

from tomlkit.items import Bool

from hueControl.io.objects import Io


@dataclass
class Owner:
    rid: str
    rtype: str


class Archetype(Enum):
    unknown_archetype = 1
    classic_bulb = 2
    sultan_bulb = 3
    flood_bulb = 4
    spot_bulb = 5
    candle_bulb = 6
    luster_bulb = 7
    pendant_round = 8
    pendant_long = 9
    ceiling_round = 10
    ceiling_square = 11
    floor_shade = 12
    floor_lantern = 13
    table_shade = 14
    recessed_ceiling = 15
    recessed_floor = 16
    single_spot = 17
    double_spot = 18
    table_wash = 19
    wall_lantern = 20
    wall_shade = 21
    flexible_lamp = 22
    ground_spot = 23
    wall_spot = 24
    plug = 25
    hue_go = 26
    hue_lightstrip = 27
    hue_iris = 28
    hue_bloom = 29
    bollard = 30
    wall_washer = 31
    hue_play = 32
    vintage_bulb = 33
    vintage_candle_bulb = 34
    ellipse_bulb = 35
    triangle_bulb = 36
    small_globe_bulb = 37
    large_globe_bulb = 38
    edison_bulb = 39
    christmas_tree = 40
    string_light = 41
    hue_centris = 42
    hue_lightstrip_tv = 43
    hue_lightstrip_pc = 44
    hue_tube = 45
    hue_signe = 46
    pendant_spot = 47
    ceiling_horizontal = 48
    ceiling_tube = 49


@dataclass
class Metadata:
    name: str
    archetype: Archetype
    fixed_mired: int


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


class Signal(Enum):
    no_signal = 1
    on_off = 2


@dataclass
class SignalingStatus:
    signal: Signal
    estimated_end: datetime


class LightMode(Enum):
    normal = 1
    streaming = 2


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
    no_effect = 1
    sparkle = 2
    fire = 3
    candle = 4


@dataclass
class Effects:
    effect: LightEffect
    status_values: List[LightEffect]
    status: LightEffect
    effect_values: LightEffect


class LightTimedEffect(Enum):
    no_effect = 1
    sunrise = 2


@dataclass
class TimedEffects:
    effect: LightTimedEffect
    duration: int
    status_values: [str]
    status: LightTimedEffect
    effect_values: [str]


class Preset(Enum):
    safety = 1
    powerfail = 2
    last_state = 3
    custom = 4


class PowerUpMode(Enum):
    toggle = 1
    previous = 2


@dataclass
class On:
    mode: PowerUpMode
    on: bool


@dataclass
class DimmingDimming:
    brightness: float

    def __post_init__(self):
        if 0 > self.brightness > 100:
            raise ValueError(f"Dimming must be 0 to 100.")

    def __str__(self):
        return f"{{brightness: {self.brightness}}}"


class DimmingMode(Enum):
    dimming = 1
    previous = 2


class PowerUpDimming:
    mode: DimmingMode
    dimming: DimmingDimming


@dataclass
class PowerUp:
    preset: Preset
    configured: bool
    on: On
    dimming: Dimming


class ColorMode(Enum):
    color_temperature = 1
    color = 2
    previous = 3


@dataclass
class ColorColorTemperature:
    mirek: int

    def __post_init__(self):
        if self.mirek < 153 or self.mirek > 500:
            raise ValueError("ColorColorMirek has to be 153 to 500")

    def __str__(self):
        # TODO: Finish this to json method in strng
        return {""}


@dataclass
class Color:
    mode: ColorMode
    color_temperature: ColorColorTemperature
    color: CieXy


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
    effects: Effects


class LightApi(Io):
    def __init__(self, bridge: str, user: str):
        super().__init__(bridge=bridge, user=user)

    def get_lights(self) -> List[Light]:
        path = "resource/light"
        url = urljoin(self.base_url, path)
        lights = self.get(url)
        return self.parse_lights(lights)

    def parse_lights(self, payload: Dict) -> List[Light]:
        l = Light(
            type="kdsjldkjf",
            id="kldsjflksj",
            id_v1="slkdjflksd",
            owner=Owner(
                rid="dskljflskdj",
                rtype="skdjfldsjfl",
            ),
        )
        return [l]

    def put_lights(self, lights: List[Light]) -> bool:
        raise NotImplementedError
