#!/bin/sh

readonly COMMENT=$1
readonly CURRENT_TIME=$(date +"%Y-%m-%d_%H%M%S")
readonly OUT_DIR="snapshots"

declare IMAGE
if [[ ! -z ${COMMENT} ]]; then
    IMAGE="${OUT_DIR}/${CURRENT_TIME}_${COMMENT}.png"
else
    IMAGE="${OUT_DIR}/${CURRENT_TIME}.png"
fi

mv "generated-image.png" "${IMAGE}"

git add src/*
git add snapshots/*

git commit -m "snapshot ${CURRENT_TIME} ${COMMENT}"

echo "Created snapshot ${IMAGE}"
