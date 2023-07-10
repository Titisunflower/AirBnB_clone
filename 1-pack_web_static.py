#!/usr/bin/python3
"""Python module to compress all web static files"""
from fabric.api import local, task
from datetime import datetime

@task
def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(timestamp)

    local("mkdir -p versions")
    result = local("tar -czvf {} web_static".format(archive_path), capture=True)

    if result.succeeded:
        return archive_path
    else:
        return None
