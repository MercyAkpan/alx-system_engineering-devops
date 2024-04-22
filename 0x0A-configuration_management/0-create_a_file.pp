file { '/tmp/school': # title of file,and by default path of file
  ensure  => 'file', # ensures such file exists, or creates it
  content => 'I love Puppet', # content inside files
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744', # for making directories the '0'is not needed for octal notation
}
# puppet -lint is === betty 
# puppet apply runs puppet as a script
