# This script increases Nginx limit to handle more requests

# Edit /etc/default/nginx file
exec { 'Increase Limit':
    command => "sed -i 's/^ULIMIT=.*/ULIMIT=\"-n 4096\"/' /etc/default/nginx",
    path    => '/usr/bin:/bin'
}

# Restart Nginx
exec { 'Restart Nginx':
    command => 'service nginx restart',
    path    => '/usr/sbin:/sbin'
}