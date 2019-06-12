#!/bin/bash

time=$(date +"%H:%M")

if [[ $time > '19:00' ]] || [[ $time < '06:00' ]]; then
    gsettings set org.gnome.desktop.interface gtk-theme 'Adwaita-dark'
    gsettings set org.gnome.Terminal.ProfilesList default '88173e30-df6e-4442-b012-4e1119c7385f'
    exit 0
else
    gsettings set org.gnome.desktop.interface gtk-theme 'Adwaita'
    gsettings set org.gnome.Terminal.ProfilesList default 'b4bd0ffd-117e-4778-82ef-da4ccdf4cb2c'
    exit 0
fi
