import docker
import pytest
import time

@pytest.fixture
def mysqld():
    client = docker.from_env()
    c = None
    environment={
        'MYSQL_ROOT_PASSWORD': 'snippet',
        'MYSQL_DATABASE': 'snippet',
        'MYSQL_USER': 'snippet',
        'MYSQL_PASSWORD': 'snippet'
    }
    ports={
        '3306': 3306,
    }
    c = client.containers.run('mysql', environment=environment, ports=ports, detach=True)
    time.sleep(25)
    yield
    c.kill()
    c.remove()

if __name__ == '__main__':
    mysqld()
