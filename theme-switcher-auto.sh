#!/bin/bash

time=$(date +"%H:%M")

# List and set your gnome-terminal profiles:
# gsettings get org.gnome.Terminal.ProfilesList list
terminal_dark='88173e30-df6e-4442-b012-4e1119c7385f'
terminal_light='b4bd0ffd-117e-4778-82ef-da4ccdf4cb2c'

if [[ $time > '20:00' ]] || [[ $time < '06:00' ]]; then
    gsettings set org.gnome.desktop.interface gtk-theme 'Adwaita-dark'
    gsettings set org.gnome.Terminal.ProfilesList default $terminal_dark
    exit 0
else
    gsettings set org.gnome.desktop.interface gtk-theme 'Adwaita'
    gsettings set org.gnome.Terminal.ProfilesList default $terminal_light
    exit 0
fi
