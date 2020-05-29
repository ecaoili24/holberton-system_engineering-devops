# Fixes the # of failed requests to 0

exec { 'nginx-fix':
  command => "sed -i 's/worker_processes 4;/worker_processes 7;/g'
  	      /etc/nginx/nginx.conf; sudo service nginx restart",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}