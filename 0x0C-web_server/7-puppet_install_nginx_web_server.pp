$package = 'Nginx HTTP'
$text = 'Hello World'
$new_string = 'server_name _;\n\tlocation /redirect_me {\n\t\trewrite ^/redirect_me https://www.google.com permanent;\n\t}'

exec { 'install_nginx':
  command => 'sudo apt install -y nginx',
  unless  => 'dpkg -l nginx',
  path    => ['/bin', '/usr/bin'],
}
exec { 'allow_nginx_traffic':
  command => "sudo ufw allow \"$package\"",
#  command => "sudo ufw allow \"$package\"",
  path    => ['/bin', '/usr/bin'],
}

exec { 'set_up_nginx_content':
  command => "echo $text | sudo tee /var/www/html/index.html",
  path    => ['/bin', '/usr/bin'],
}

#exec { 'set_up_nginxcontent':
#  command => "sudo sed -i \"s#server_name _;#$new_string#\"  /etc/nginx/sites-enabled/default",
#  path    => ['/bin', '/usr/bin'],
#}


exec { 'restart_nginx':
  command => 'sudo service nginx restart',
  path    => ['/bin', '/usr/bin'],
}
#exec { 'set_up_nginx':
#       'echo "$landing_text" | sudo tee  /var/www/html/index.html',
#}
