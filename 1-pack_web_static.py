#!/usr/bin/python3
"""

"""


from fabric.api import local, task
from datetime import datetime


@task
def do_pack():
    """archive web_static"""
    try:
        currentTime = datetime.now().strftime('%Y%m%d%H%M%S')
        fileName = f'web_static_{currentTime}.tgz web_static'
        local("mkdir -p versions")
        local(f"tar -cvzf versions/{fileName}")
        return "versions/"
    except Exception as e:
        return None
