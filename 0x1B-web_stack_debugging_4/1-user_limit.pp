# This script enables holberton login without an error

# Edit /etc/security/limits.conf file
exec { 'Increase User Limit hard':
    command => "sed -i 's/holberton hard nofile.*/holberton hard nofile 1024/' /etc/security/limits.conf",
    path    => ['/usr/local/bin/', '/bin/'],
}

exec { 'Increase User Limit soft':
    command => "sed -i 's/holberton soft nofile.*/holberton soft nofile 1024/' /etc/security/limits.conf",
    path    => ['/usr/local/bin/', '/bin/'],
}