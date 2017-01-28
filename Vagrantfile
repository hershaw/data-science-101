Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/trusty64"

  ENV['LC_ALL']="C"

  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
    v.cpus = 4
  end

  config.vm.synced_folder "course", "/home/vagrant/course", type: "nfs"
  config.vm.network "private_network", ip: "192.168.50.13"
  config.vm.network "forwarded_port", guest: 8888, host: 8888

  config.vm.provision "installation", type: "shell", privileged: false, inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y build-essential libblas-dev liblapack-dev gfortran python3 python3-dev python3-pip git
    sudo pip3 install --upgrade pip
    # install six ahead of time because otherwise jupyter installation hits a conflicting bug
    sudo pip3 install -U six
    sudo pip3 install Cython==0.25.2 numpy==1.12.0 jupyter==1.0.0 pandas==0.19.2 scikit-learn==0.18.1 seaborn==0.7.1 matplotlib==2.0.0
    jupyter notebook --generate-config -y
    sed -i -e 's/#c.NotebookApp.open_browser = True/c.NotebookApp.open_browser = False/' /home/vagrant/.jupyter/jupyter_notebook_config.py
    sed -i -e "s/#c.NotebookApp.ip = 'localhost'/c.NotebookApp.ip = '0.0.0.0'/" /home/vagrant/.jupyter/jupyter_notebook_config.py
    sed -i -e "s/#c.NotebookApp.disable_check_xsrf = False/c.NotebookApp.disable_check_xsrf = True/" /home/vagrant/.jupyter/jupyter_notebook_config.py
    sed -i -e "s/#c.NotebookApp.token = '<generated>'/c.NotebookApp.token = ''/" /home/vagrant/.jupyter/jupyter_notebook_config.py
  SHELL

  config.vm.provision "run-notebook", type: "shell", run: "always", privileged: false, inline: <<-SHELL
    export PYTHONPATH=.:/home/vagrant/course
    nohup jupyter-notebook --notebook-dir=/home/vagrant &
  SHELL

end
