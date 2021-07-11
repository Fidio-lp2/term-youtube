# -*- coding: utf-8 -*-
"""
Making be enable to import from the ``term-youtube`` directory.

"""
import os
import sys


def inves_home_path():
    """
    Investigate the absolute path of ``term-youtube`` in this app.
    """
    sys.path.append(os.path.join(os.path.dirname(__file__), "../term-youtube"))
