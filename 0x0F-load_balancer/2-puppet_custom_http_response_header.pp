#MINE
exec { 'apt-update':
  command => '/usr/bin/sudo apt-get -y update',
  path    => ['/usr/bin', '/bin'],
}

exec { 'install_nginx':
  command => 'sudo apt install -y nginx',
  unless  => '/usr/bin/dpkg-query -l nginx ',
  path    => ['/bin', '/usr/bin'],
}

exec { 'adding_headers':
  command => 'sudo sed -i "0,/server {/s#server {#server {\n\tadd_header X-Served-By \$hostname;#" /etc/nginx/sites-enabled/default',
  path    => ['/bin', '/usr/bin'],
}

exec { 'restart_nginx':
  command => 'sudo service nginx restart',
  path    => ['/bin', '/usr/bin'],
}
