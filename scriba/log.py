#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Scriba log settings."""

from __future__ import absolute_import, unicode_literals

import logging
import os
import sys

DEFAULT_FORMAT = '%(asctime)s - %(name)-30s - %(levelname)-10s - %(message)s'

LOG = logging.getLogger('scriba')
LOG.setLevel(os.environ.get('SCRIBA_LOG_LEVEL', 'DEBUG'))

HANDLER = logging.StreamHandler(sys.stdout)
HANDLER.setFormatter(logging.Formatter(os.environ.get('SCRIBA_LOG_FORMAT', DEFAULT_FORMAT)))
LOG.addHandler(HANDLER)
