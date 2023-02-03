<img src="https://github.com/ajipelumi/alx-system_engineering-devops/blob/7d57e3d2f082c630cb5609f4ce0d8e853ce13065/images/what-is-localhost-1024x512.png" alt="local host" width="400">
Image Credit: Kinsta

##

**[localhost](https://en.wikipedia.org/wiki/Localhost)** is a hostname that refers to the current device used to access it.
It is used to access the network services that are running on the host via the loopback network interface.

This README decribes what each script/program is doing:

The file `0-change_your_home_IP` is a bash script that configures an Ubuntu server with the below requirements.
Requirements:
- `localhost` resolves to `127.0.0.2`
- `facebook.com` resolves to `8.8.8.8`

The file `1-show_attached_IPs` is a bash script that displays all active IPv4 IPs on the machine it’s executed on.

The file `100-port_listening_on_localhost` is a bash script that listens on port `98` on `localhost`.
