#!/usr/bin/env sh
cd ~/apps/TmNCT_News/

case $1 in
    main) ./main.py;;
    weather) ./weatherreporter.py
esac

