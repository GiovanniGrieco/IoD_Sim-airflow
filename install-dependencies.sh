#!/bin/bash

. /etc/os-release

case $ID in
	debian | ubuntu)
		sudo apt install --no-install-recommends \
			qtbase5-dev
		;;
	*)
		echo "OS $ID not supported by this script."
		exit 1
		;;
esac

