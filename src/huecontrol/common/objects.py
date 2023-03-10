from enum import Enum


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
