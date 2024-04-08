#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6701944692:AAEv1Tf_gGXihfwke1U7B-iRvkh5uR9p-aU")
    API_ID = int(os.environ.get("API_ID", "28127959"))
    API_HASH = os.environ.get("API_HASH", "0debc9c74510961fc8cf134a3c6eae0f")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6370953390")
