export QT_QPA_PLATFORMTHEME="qt5ct"

# EDITOR variable
export EDITOR=/usr/bin/vim

# PyWal set wallpaper and colors
wal -R

# Remap caps to esc
setxkbmap -option "caps:swapescape"

# Compton compositor
picom --config ~/.config/picom.conf -b
