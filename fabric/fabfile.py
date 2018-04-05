#!/usr/bin/env python
import test
from fabric.api import env, run, task

@task(default=True)
def server_setup():
  test.version()


