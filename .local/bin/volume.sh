#!/bin/sh

# volume.sh
# Requires: pulseaudio (pactl) and libnotify (notify-send)

get_bar() {
    local vol=$1
    [ "$vol" -gt 100 ] && vol=100
    
    # 20-character bar (perfect for 5% increments)
    local filled=$(( vol / 5 ))
    local empty=$(( 20 - filled ))
    
    local bar_filled=""
    local bar_empty=""
    
    # Using heavy line '━' for filled, light line '─' for empty
    while [ $filled -gt 0 ]; do bar_filled="${bar_filled}━"; filled=$((filled - 1)); done
    while [ $empty -gt 0 ]; do bar_empty="${bar_empty}─"; empty=$((empty - 1)); done
    
    # Use Pango markup to colorize the filled vs empty sections
    echo "[<span foreground='#aaaaaa'>${bar_filled}</span><span foreground='#708090'>${bar_empty}</span>]"
}

send_notification() {
    # Check if muted
    mute_status=$(pactl get-sink-mute @DEFAULT_SINK@ | awk '{print $2}')
    
    if [ "$mute_status" = "yes" ]; then
        # Muted bar is fully empty and colored slate-blue
        notify-send -h string:x-canonical-private-synchronous:volume "Volume" "Muted  [<span foreground='#708090'>────────────────────</span>]" -t 2000
    else
        # Extract the percentage from pactl output
        vol_level=$(pactl get-sink-volume @DEFAULT_SINK@ | head -n 1 | awk -F '/' '{print $2}' | tr -d ' %')
        
        # Generate the visual bar
        bar=$(get_bar "$vol_level")
        
        notify-send -h string:x-canonical-private-synchronous:volume "Volume" "${vol_level}%  ${bar}" -t 2000
    fi
}

case "$1" in
    up)
        # Unmute and raise volume by 5%
        pactl set-sink-mute @DEFAULT_SINK@ 0
        pactl set-sink-volume @DEFAULT_SINK@ +5%
        send_notification
        ;;
    down)
        # Unmute and lower volume by 5%
        pactl set-sink-mute @DEFAULT_SINK@ 0
        pactl set-sink-volume @DEFAULT_SINK@ -5%
        send_notification
        ;;
    mute)
        # Toggle mute
        pactl set-sink-mute @DEFAULT_SINK@ toggle
        send_notification
        ;;
    *)
        echo "Usage: $0 {up|down|mute}"
        ;;
esac
