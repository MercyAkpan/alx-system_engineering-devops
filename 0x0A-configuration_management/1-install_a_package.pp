package { 'python3-flask': # package to be installed
  ensure   => '2.1.0', # 'installed'== latest version, 'version_num'=> installs particular version
  provider => 'pip3', #provider(package manager) to install package
}
# catalog is compiled intermediate of the puppet manifest(puppet script)
