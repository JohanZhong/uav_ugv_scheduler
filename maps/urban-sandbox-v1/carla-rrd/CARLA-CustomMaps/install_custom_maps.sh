#!/usr/bin/env bash
set -euo pipefail

BUNDLE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ -z "${CARLA_ROOT:-}" ]; then
  echo "CARLA_ROOT is not set." >&2
  echo "Usage: CARLA_ROOT=/path/to/CARLA ./install_custom_maps.sh" >&2
  exit 1
fi

TARGET_CARLA_DIR="$CARLA_ROOT/CarlaUE4"
SOURCE_CARLA_DIR="$BUNDLE_DIR/CarlaUE4"
SOURCE_CUSTOM_MAPS="$SOURCE_CARLA_DIR/Content/CustomMaps"

if [ ! -d "$SOURCE_CUSTOM_MAPS" ]; then
  echo "Bundle is incomplete: $SOURCE_CUSTOM_MAPS not found." >&2
  exit 1
fi

if [ ! -d "$TARGET_CARLA_DIR/Content" ]; then
  echo "CARLA content directory not found: $TARGET_CARLA_DIR/Content" >&2
  echo "Check CARLA_ROOT. It should point to the CARLA directory that contains CarlaUE4/." >&2
  exit 1
fi

rsync -a "$SOURCE_CARLA_DIR/" "$TARGET_CARLA_DIR/"

cat <<EOF
Custom maps installed into:
  $TARGET_CARLA_DIR/Content/CustomMaps
  $TARGET_CARLA_DIR/Content/33333_udatasmith
  $TARGET_CARLA_DIR/Plugins/RoadRunner*

For the UrbanAgent bridge, use:
  export CARLA_ROOT="$CARLA_ROOT"
  export CARLA_MAP=RRD

Then start CARLA and run UrbanAgent's urbanagent-main/run_bridge.sh.
EOF
