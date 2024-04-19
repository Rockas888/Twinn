#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6478288853:AAF7c67L2FTBEtFlW6Ebb6x1lkPo0VTDdxI")
    API_ID = int(os.environ.get("API_ID", "24478892"))
    API_HASH = os.environ.get("API_HASH", "b7b00353625f83dbf6ca2438353515a0")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6585878012")
