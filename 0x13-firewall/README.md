**Firewalls** can be hardware or software-based and they are used to prevent unauthorized access to or from private networks or devices, by analyzing the network traffic based on predefined security rules.

They can also be used to filter out certain types of traffic, such as malicious traffic or traffic coming from specific IP addresses or ports.

**Firewalls** are a fundamental component of network security and are commonly used in corporate networks, as well as in home networks, to protect against various types of cyber attacks, such as malware infections, hacking attempts, and other malicious activities.

`ufw` allows us to define rules that determine which network traffic is allowed to pass through the firewall and which traffic should be blocked.
The rules are based on ports, protocols, IP addresses, and other criteria.

Some `ufw` commands are:
- `sudo ufw enable`: Enables the firewall and starts it at boot time.
- `sudo ufw disable`: Disables the firewall.
- `sudo ufw status`: Shows the current status of the firewall and the rules that are applied.
- `sudo ufw allow <port>/<protocol>`: Allows incoming traffic on a specific port and protocol.
- `sudo ufw deny <port>/<protocol>`: Denies incoming traffic on a specific port and protocol.
