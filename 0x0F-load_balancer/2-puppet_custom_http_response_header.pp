# This manifest installs and configure an Nginx server.

# Install stdlib for file_line
class { 'stdlib': }

# Install Nginx
package { 'nginx':
  ensure   => 'installed',
  provider => 'apt',
}

# Add header
file_line { 'add_header':
  path    => '/etc/nginx/sites-enabled/default',
  line    => "\tadd_header X-Served-By ${hostname};",
  after   => '^	listen 80 default_server;$',
  require => Class['stdlib'],
}

# Start server
service { 'nginx':
  ensure => 'running',
  enable => 'true',
}
