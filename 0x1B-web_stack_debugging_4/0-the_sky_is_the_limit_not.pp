# This script increases Nginx limit to handle more requests

# Edit /etc/default/nginx file
exec { 'Increase Limit':
    command => "sed -i 's/15/4096/g' /etc/default/nginx",
    path    => '/usr/bin:/bin'
}

# Restart Nginx
exec { 'Restart Nginx':
    command => 'service nginx restart',
    path    => '/usr/sbin:/sbin'
}