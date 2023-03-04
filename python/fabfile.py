from fabric import task, Connection, Config
from fabric import Config, task

@task
def play_localy(c):
    c.run('ls -la')