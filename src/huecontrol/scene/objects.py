from dataclasses import dataclass
from enum import Enum
from typing import List, Dict
from urllib.parse import urljoin

from hueControl.io.objects import Io

from huecontrol.common.objects import Rtype


@dataclass
class MetadataScene:
    name: str
    image: Rtype
    rid: str
    rtype: Rtype

    def __post_init__(self):
        if self.image != Rtype.public_image:
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
