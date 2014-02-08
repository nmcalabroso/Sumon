# SUMOn

## Installation

### Dependencies

First, install all required dependencies:
```bash
$ sudo apt-get update && sudo apt-get upgrade
$ sudo apt-get install python-pip python-dev python-setuptools python-imaging build-essential python-virtualenv virtualenvwrapper libpq-dev
```

Then, create our virtual environment:
```bash
$ mkvirtualenv game_dev
$ workon game_dev
```
Note: Restart might be needed before the command mkvirtualenv be available

Your prompt should now look similar to this:
```
(game_dev)neegool@bulalo ~ $
```

Next, from within the virtual environment, we install pyglet.
```bash
pip install --upgrade http://pyglet.googlecode.com/archive/tip.zip
```

### Project

Clone our repository, and switch to that directory (make sure you've been added to the repo as a collaborator. Otherwise, kindly inform me so that I can add you)
```bash
$ git clone https://github.com/nmcalabroso/Sumon.git
$ cd Sumon
```
༼ つ ◕_◕ ༽つ GIFF ME MP2 <3