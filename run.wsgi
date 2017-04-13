import sys
root=r'/usr/local/share/virtualenvs/rrdscout'
sys.path.insert(0, root)

activate_this = root + '/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from app import app as application

application.config['SECRET_KEY'] = 'F34TF$($e34D';
