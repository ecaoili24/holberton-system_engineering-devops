# Using Puppet, create a file in /tmp

file {
     '/tmp/holberton':
     mode	=> '0774',
     owner	=> 'www-data',
     group	=> 'www-data',
     content	=> 'I love Puppet',
}