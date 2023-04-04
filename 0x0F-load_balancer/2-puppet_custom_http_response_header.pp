# This manifest installs and configure an Nginx server.

include stdlib

package { 'nginx':
  ensure => 'installed',
}

file_line { 'add_header':
  ensure => 'present',
  path   => '/etc/nginx/nginx.conf',
  line   => "\tadd_header X-Served-By ${hostname};",
  after  => 'include \/etc\/nginx\/sites-enabled\/\*;',
}

exec { 'restart-nginx':
  command => '/etc/init.d/nginx restart',
}
