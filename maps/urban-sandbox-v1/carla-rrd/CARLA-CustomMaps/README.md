# CARLA Custom Maps Portable Patch

This archive contains the complete custom CARLA map assets found under:

```text
/home/changjinli/UrbanProject/406-3090/CarlaUE4/Content/CustomMaps
```

It does not contain the full CARLA simulator. It includes the map dependencies
that are outside `CustomMaps`, so the packaged `RRD` map can be restored without
copying the full CARLA source tree.

## Included Maps

- `CustomMaps/roadrunne3/RRD.umap`
- `CustomMaps/roadrunne3/RRD.uexp`
- `CustomMaps/roadrunne3/RRD_BuiltData.uasset`
- `CustomMaps/roadrunne3/RRD_BuiltData.uexp`
- `CustomMaps/roadrunne3/RRD_BuiltData.ubulk`
- `CustomMaps/roadrunne3/OpenDrive/RRD.xodr`
- Supporting assets under `CustomMaps/roadrunne3/33333_udatasmith/`
- External assets under `Content/33333_udatasmith/` referenced by `RRD`
- Runtime RoadRunner content and plugin descriptors under `CarlaUE4/Plugins/`
- Updated `AssetRegistry.bin` and project packaging metadata for the custom maps

Editor-only RoadRunner import plugins are intentionally excluded from the
shipping patch. The runtime package keeps `RoadRunnerRuntime` plus the baked
RoadRunner content required to load `RRD`.
- Additional custom map folders found in the same source `CustomMaps/` directory,
  including `sandbox-v29/` and `roadrunner2/`.

## Install On The Target Machine

First install or copy a compatible CARLA environment to the target machine.
Then unpack this archive and run:

```bash
cd CARLA-CustomMaps
CARLA_ROOT=/path/to/CARLA ./install_custom_maps.sh
```

`CARLA_ROOT` must be the directory that contains `CarlaUE4/`.

The script copies the patch contents:

```text
CARLA-CustomMaps/CarlaUE4/
```

to:

```text
$CARLA_ROOT/CarlaUE4/
```

## Use With UrbanAgent

The UrbanAgent bridge defaults to the custom map name `RRD`.

```bash
export CARLA_ROOT=/path/to/CARLA
export CARLA_MAP=RRD
```

Then start CARLA, and in the UrbanAgent project run:

```bash
cd urbanagent-main
./run_bridge.sh
```

If CARLA cannot load `RRD`, open the CARLA/Unreal project and verify that the
map path `/Game/CustomMaps/roadrunne3/RRD` exists in the target installation.
