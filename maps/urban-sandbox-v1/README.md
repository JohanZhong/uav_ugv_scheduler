# Urban Sandbox v1

This directory contains the ROS occupancy map recovered from the UrbanProject
physical UAV/UGV sandbox. It is an asset package for a real sandbox, not the
synthetic campus background rendered by this project's current DDS demo.

## Contents

| File | Purpose |
| --- | --- |
| `map.pgm` | Original binary PGM occupancy raster: 300 x 300 pixels. |
| `map.yaml` | ROS map-server metadata for the raster. |
| `alignment.yaml` | Coordinate-frame record and historical calibration values. |
| `CARLA_RRD_MANIFEST.md` | Instructions for the separate CARLA digital-twin map. |

## ROS map contract

- Frame: `sandbox_map`
- Resolution: `0.05 m/pixel`
- Origin: `[-7.5, -7.5, 0.0]`
- Covered extent: `15 m x 15 m`
- Occupancy thresholds: occupied `0.65`, free `0.25`

For a ROS 2 deployment, pass the full path to `map.yaml` to the map server:

```bash
ros2 run nav2_map_server map_server --ros-args -p yaml_filename:=/absolute/path/to/maps/urban-sandbox-v1/map.yaml
```

Activating the node still requires the rest of the Nav2 lifecycle setup; this
repository does not currently start ROS 2 or Nav2.

## Coordinate boundary

The current C++ demo publishes `park_enu_v1` / `CAMPUS_LOCAL` and projects it
to a 640 x 440 browser illustration. It must not claim `sandbox_map` merely
because this folder is present. To use this real map for dispatch, add an
explicit transform from the incoming mission frame to `sandbox_map`, then set
the DDS `frame_id` and `map_version` consistently.

`alignment.yaml` records the known legacy UAV/UWB baseline plus field points
from the original project. Those values are calibration starting points, not
portable truth: recalibrate after moving the sandbox, UWB anchors, vehicle,
or CARLA map.

## Integrity

The migrated source fingerprints are:

```text
map.pgm   SHA-256 127542157DED3AE59FAA8DF52CFFC6EB492A4650C65DB0CACDB44CB9EA508B5F
map.yaml  SHA-256 94E461AA91E6E13B8E505FB8F5FC14261107561180A61A1820827AF47AF9FA3A
```

Run the repository verifier after copying or packaging the assets:

```powershell
python .\tests\verify_sandbox_map.py
```
