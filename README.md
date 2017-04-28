# How to use this repo

Each directory contains a README.md that should be read before exploring
any sub-directories. You can just browse the directories on github.com
in your favorite browser for instructions on how to use the directory's
contents.

Since this README is at the top-level, it contains installation and usage instructions.

## Prerequisites

- ~1GB of free memory on your computer.
- Some hundreds of megabytes free on your computer
- 64-bit processor
- The ability to read a README and follow the instructions in it.

## Setup

#### Optional but strongly suggested

[Sign up](https://github.com/join) for a GitHub account if you don't already have one. Really, it's quite useful.

Note: if looking for a docker smaller footprint jump to the end.

### Step 1 - Install dependencies

Follow each of the links to download and install.

- [git](https://git-scm.com/)
  - If you're on Windows or OS X and don't know what git is, [GitHub Desktop](https://desktop.github.com/) is probably easiest.
  - All others: you probably know what to do.
- [virtualbox](https://www.virtualbox.org)
  - [Windows](http://download.virtualbox.org/virtualbox/5.1.14/VirtualBox-5.1.14-112924-Win.exe)
  - [OS X](http://download.virtualbox.org/virtualbox/5.1.14/VirtualBox-5.1.14-112924-OSX.dmg)
  - All others: again, you probably know what you're doing.
- [vagrant](https://www.vagrantup.com/). *Important note for OSX USERS* please download [vagrant 1.8.5](https://releases.hashicorp.com/vagrant/1.8.5/)
  - [Windows](https://releases.hashicorp.com/vagrant/1.9.1/vagrant_1.9.1.msi)
  - [OS X](https://releases.hashicorp.com/vagrant/1.8.5/)
  - Do I need to say it again? ;-)

### Step 2 - Clone this repo

If you installed git using `GitHub Desktop`, follow [these instructions](https://help.github.com/desktop/guides/contributing/cloning-a-repository-from-github-to-github-desktop/)

If you are cloning from the command line:

- If you have a github account
  - `git clone git@github.com:hershaw/data-science-101.git`
- If you don't have a github account
  - `git clone https://github.com/hershaw/data-science-101.git`
  
Take a note of the filepath on which you cloned the repo!
  
### Step 3 - Start your environment

#### Navigate on the command line to the root of the repo

Assuming you've cloned the repo onto your desktop on OS X, the command would look something like

- `cd ~/Desktop/data-science-101`

#### Start the virtual machine

  - `vagrant up`
  
Note that this will take a LONG time and you should have a good internet connection in order to expedite the process.
  
If you're uncomfortable on the command line, please do your best to power through this and share
your learnings and ask for help on the class' [glitter channel](https://gitter.im/data-science-101/Lobby?utm_source=share-link&utm_medium=link&utm_campaign=share-link).


### Step 4

#### Make sure that jupyter notebook is running

Open [http://localhost:8888](http://localhost:8888) in your browser and you should see the `course` directory.

Using jupyter notebook, enter the `course` directory and run `test.ipynb` to make sure that
everything was installed okay. If you can run this without errors, you are good to go!

If for some reason this doesn't work, head over to the [glitter channel](https://gitter.im/data-science-101/Lobby?utm_source=share-link&utm_medium=link&utm_campaign=share-link).

### Final notes

More useful commands to execute from the `data-science-101` root directory

- `vagrant halt`
  - shuts down the virtual machine for when you're done working for the day
- `vagrant up`
  - start it up again when you're ready to work
- `vagrant reload`
  - if for some reason things get messed up and you need to restart
- `vagrant destroy -f && vagrant up`
  - if things get SUPER messed up and you need to start all over


## Alternative setup using docker 

### Step 1

Install:
- [git](https://git-scm.com/)
  - If you're on Windows or OS X and don't know what git is, [GitHub Desktop](https://desktop.github.com/) is probably easiest.
  - All others: you probably know what to do.
- [docker](https://docs.docker.com/engine/installation/)

### Step 2

If you installed git using `GitHub Desktop`, follow [these instructions](https://help.github.com/desktop/guides/contributing/cloning-a-repository-from-github-to-github-desktop/)

If you are cloning from the command line:
```shell
1. $ git clone https://github.com/hershaw/data-science-101.git
```

### Step 3 

1. Build a docker image (first time takes longer):
```shell
    $ docker build -t data-science -f Dockerfile .
```
2. Run a container:
(Assuming your code is located on "~/Desktop/data-science-101". If needed replace it with something meaningful.)  
```shell
    $ docker run -it --rm -p 127.0.0.1:8888:8888 --volume ~/Desktop/data-science-101:/home/vagrant/ \
    --workdir /home/vagrant/ -e PYTHONPATH=.:/home/vagrant/course data-science
```

### Step 4

Open http://localhost:8888 to access notebook.
To stop everything just hit <ctrl>+c and then "y" on the interactive shell.

### Final notes

This is not the recommended security approach, please use tokens or authentication.
Expect much less hardware requirements.

