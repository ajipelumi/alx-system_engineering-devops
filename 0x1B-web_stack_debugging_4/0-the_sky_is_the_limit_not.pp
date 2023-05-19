# This script increases Nginx limit to handle more requests

# Edit /etc/default/nginx file
exec { 'Increase Limit':
    command => "sed -i 's/^ULIMIT=.*/ULIMIT=\"-n 4096\"/' /etc/default/nginx",
    path    => ['/usr/local/bin/', '/bin/'],
}

# Restart Nginx
exec { 'Restart Nginx':
    command => 'nginx restart',
    path    => ['/etc/init.d/'],
}