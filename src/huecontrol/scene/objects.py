from dataclasses import dataclass
from enum import Enum
from typing import Dict, List
from urllib.parse import urljoin

from huecontrol.common.objects import (Color, ColorTemperature, Dimming,
                                       Dynamics, LightGradient, Rtype)
from hueControl.io.objects import Io


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


class SceneMode(Enum):
    interpolated_palette = 1
    interpolated_palette_mirrored = 2
    random_pixelated = 3


@dataclass
class Target:
    rid: str
    rtype: Rtype


@dataclass
class Scene:
    type: str
    id: str
    id_v1: str
    metadata: MetadataScene
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
        scenes = Scene(
            type="kdsjldkjf",
            id="kldsjflksj",
            id_v1="slkdjflksd",
            target=Target(
                rid="dskljflskdj",
                rtype="skdjfldsjfl",
            ),
        )
        return [scenes]

    def put_scene(self, lights: List[Scene]) -> bool:
        raise NotImplementedError
