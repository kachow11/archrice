#!/bin/sh

slstatus -s | dwl -s " \
    wlr-randr --output DP-1 --mode 1920x1080 --pos 0,0; \
    wlr-randr --output eDP-1 --custom-mode 1620x1080@60 --pos 1920,0; \
    swaybg -i ~/Pictures/dwl-guile-my-comfy-lisp-machine-v0-fwxvj722h41b1.jpeg & \
    mako & \
"
