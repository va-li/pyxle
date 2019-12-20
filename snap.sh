#!/bin/sh

readonly COMMENT=$1
readonly CURRENT_TIME=$(date +"%Y-%m-%d_%H%M%S")
readonly OUT_DIR="snapshots"

declare IMAGE
if [ -n "${COMMENT}" ]; then
    IMAGE="${OUT_DIR}/${CURRENT_TIME}_${COMMENT}.png"
else
    IMAGE="${OUT_DIR}/${CURRENT_TIME}.png"
fi

cp "generated-image.png" "${IMAGE}"

git add image-generator.py
git add "${IMAGE}"

git commit -m "snapshot ${CURRENT_TIME} ${COMMENT}"

echo "Created snapshot ${IMAGE}"
