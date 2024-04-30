#MINE
$package = 'Nginx HTTP'
$text = 'Hello World!'
#$new_string = 'server_name _;\n\tlocation /redirect_me {\n\t\trewrite ^/redirect_me https://www.google.com permanent;\n\t}'
exec { 'install_nginx':
  command => 'sudo apt install -y nginx',
  unless  => 'dpkg -l nginx',
  path    => ['/bin', '/usr/bin'],
}
exec { 'allow_nginx_traffic':
  command => "sudo ufw allow ${package}",
  path    => ['/bin', '/usr/bin'],
}

exec { 'set_up_landing_content':
  command => "echo ${text} | sudo tee /var/www/html/index.html",
  path    => ['/bin', '/usr/bin'],
}

exec { 'redirect':
  command => "sudo sed -i \"s#server_name _;#'server_name _;\n\tlocation /redirect_me {\n\t\trewrite ^/redirect_me https://www.google.com permanent;\n\t}'#\"  /etc/nginx/sites-enabled/default",
  path    => ['/bin', '/usr/bin'],
}
exec { 'adding_headers':
  command => "sudo sed -i '/server {/a \\\tadd_header X-Served-By \$hostname;' /etc/nginx/sites-enabled/default",
  path    => ['/bin', '/usr/bin'],
}

exec { 'restart_nginx':
  command => 'sudo service nginx restart',
  path    => ['/bin', '/usr/bin'],
}
