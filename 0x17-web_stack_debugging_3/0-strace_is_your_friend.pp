# This puppet file fixes the server.
exec { 'settings_file':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php'
}