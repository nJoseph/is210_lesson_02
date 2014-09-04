#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


from inquisition import SPANISH

FISHY = inquisition.SPANISH.replace('surprise', 'haddock')

S = 'Spanish'

FLEMISH = FISHY[: FISHY.index(S)] + 'Flemish' + FISHY[FISHY.index(S) + len(S):]
