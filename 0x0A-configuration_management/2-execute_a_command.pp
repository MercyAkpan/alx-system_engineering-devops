file { '/home/mercyakpan/killmenow': #absolute path of file
    ensure => 'present', #ensures file is present
}

exec {'killmeprocess': # Title of custom command 
    command => '/usr/bin/pkill -f killmenow', #command to execute (absolute path)
    onlyif  => '/usr/bin/pgrep -f killmenow' # command executes only if file is RUNNING
}
