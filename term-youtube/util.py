# -*- coding: utf-8 -*-
"""
Utility methods

"""
import os.path


def inves_app_path():
    """
    Investigate the absolute path of this app.
    """
    return (os.path.dirname(__file__))[:-13]
