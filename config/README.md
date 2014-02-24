It is deploy file for varnish config.
Varnish cache logic supposed to know something about backend rooting, so we keep it in this repository.
Varnish config don't supposed to be changed by hands on server but instead uploaded through git/capistrano.

Deploy commands:

varnish: cap varnish deploy:setup
nginx: cap nginx deploy:setup

Latest versions of files isn't necessary to be comitted in repository but better keep it up-to-date eventually.