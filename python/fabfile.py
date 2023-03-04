from fabric import task, Connection, Config
from fabric import Config, task


@task
def play_locally(c):
    print('ls -la')
    c.run('ls -la')


def connection(host, **kwargs):
    if 'user' not in kwargs:
        print('Make sure to put username in key arguments')
        return

    # Connection:
    # Host -> hostname or IP @
    # user -> username
    # key_filename -> key-pair connection
    # connect_kwargs = {'password': 'my_password'} -> for password connection

    conn = Connection(host, **kwargs)
    # after connection try to list directory files
    result = conn.run('ls -la')
    print(result.stdout)
