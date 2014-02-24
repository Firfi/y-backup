server 'ec2-54-217-196-129.eu-west-1.compute.amazonaws.com', :app, :web, :db, :primary => true
set :user, 'ubuntu'
default_run_options[:pty] = true
ssh_options[:forward_agent] = true
ssh_options[:auth_methods] = ["publickey"]
ssh_options[:keys] = ["../varnish-server2.pem"]
# set :use_sudo, true # default
# set :repository,  'git@bitbucket.org:fmacinnes/yarnee.pyramid.git'
# set :scm, :git


task :varnish do

  set :application, 'yarnee.varnish'

  config_file = "config/files/varnish/default.vcl" # isn't necessary to be in repository
  # config = ERB.new(File.read(config_file)).result(binding)
  config = File.read(config_file)

  put config, "/tmp/#{application}"
  sudo "mv /tmp/#{application} /etc/varnish/default.vcl"
  sudo "service varnish reload"

  # after 'deploy:restart', 'deploy:cleanup'
end

task :nginx do

  set :application, 'yarnee.nginx'

  config_file = "config/files/nginx/nginx.conf" # isn't necessary to be in repository
                                                   # config = ERB.new(File.read(config_file)).result(binding)
  config = File.read(config_file)

  put config, "/tmp/#{application}"
  sudo "mv /tmp/#{application} /etc/nginx/nginx.conf"
  sudo "service nginx reload"

  # after 'deploy:restart', 'deploy:cleanup'

end

