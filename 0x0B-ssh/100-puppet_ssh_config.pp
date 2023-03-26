# This manifest makes changes to our configuration file.

$config_str = "PasswordAuthentication no\nIdentityFile ~/.ssh/school\n"

file { '~/.ssh/config':
  content => $config_str,
}
