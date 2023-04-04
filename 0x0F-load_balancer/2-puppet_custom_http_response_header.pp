# This manifest installs and configure an Nginx server.

# Install Nginx
package { 'nginx':
  ensure   => 'installed',
  provider => 'apt',
}

# Add header
file_line { 'add_header':
  path  => '/etc/nginx/sites-enabled/default',
  line  => "	add_header X-Served-By ${hostname};",
  match => '^	listen 80 default_server;$',
}

# Start server
service { 'nginx':
  ensure => 'running',
  enable => 'true',
}
