# CARLA RRD Map Manifest

The physical sandbox raster in this package is intentionally separate from the
CARLA/Unreal RRD map. RRD depends on a CARLA 0.9.16-compatible runtime and
RoadRunner/Unreal binary assets, so copying only `RRD.umap` would produce an
unloadable map.

The original source package is:

```text
D:\UrbanProject\CARLA-CustomMaps\CarlaUE4\Content\CustomMaps\roadrunne3\
```

It includes `RRD.umap`, `RRD.uexp`, `RRD_BuiltData.*`, OpenDRIVE data and the
referenced `33333_udatasmith` assets. When a CARLA digital twin is required,
install the complete custom-map patch into the target CARLA installation using
the original `CARLA-CustomMaps/install_custom_maps.sh` workflow, then set:

```bash
export CARLA_MAP=RRD
```

Do not put those Unreal assets in this DDS scheduler repository unless this
project explicitly adopts CARLA as a runtime dependency. Their source layout,
version coupling and size make them a deployment artifact rather than a small
navigation-map asset.
