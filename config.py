#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6478288853:AAF7c67L2FTBEtFlW6Ebb6x1lkPo0VTDdxI")
    API_ID = int(os.environ.get("API_ID", "20089019"))
    API_HASH = os.environ.get("API_HASH", "0b2eb6aa72d5983fa9e4b8c77791c9c4")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6585878012")
