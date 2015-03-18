#!/bin/bash

SOURCE_DIR="~/eclipseworkspace/"
TARGET_DIR="~/eclipseworkspace/tknorris-beta-repo/"

declare -a PLUGINS
PLUGINS=("1ch" "1Channel" "plugin.video.1channel"
                  "salts" "salts" "plugin.video.salts"
                  "tlm" "plugin.video.trakt_list_manager" "plugin.video.trakt_list_manager"
                  "themepak" "1channel.themepaks" "script.1channel.themepak"
                  "trakt" "script.trakt" "script.trakt"
                  "trakt.module" "script.module.trakt" "script.module.trakt")

while [ $# -gt 0 ]; do
    i=0
    argv=$1
    while [ $i -lt ${#PLUGINS[@]} ]; do
        if [ "$argv" == "${PLUGINS[$i]}" ]; then
            CMD="rsync --delete -av --exclude='.*' --exclude='*.pyc' ${SOURCE_DIR}${PLUGINS[$i+1]}/ ${TARGET_DIR}${PLUGINS[$i+2]}"
            eval "$CMD"
        fi
        ((i=i+3))
    done
    shift
done
