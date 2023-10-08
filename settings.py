import os
from pathlib import Path

DEFAULT_ENABLED_GUILDS = () # Leave as empty tuple for slash commands to show up everywhere
#   1145433323594842166,
# )

DEV_ID    = 507642999992352779
DEV_GUILD = 1145433323594842166

VERSION = '4.0'

os.chdir(Path(__file__).resolve().parent)

with open('VERSION.txt', encoding='utf-8') as f:
  VERSION += '.' + f.read().strip()

class ALIASES:
  LIST   = ['.', 'list', 'reminders', 'rems']
  WIPE   = ['clear', 'wipe', 'deleteall', 'cancelall']
  DELETE = ['del', 'delete', 'delete this', 'deletethis', 'del this', 'delthis']

class LIMITS:
  REMINDER         = 24 # Reminders
  MINIMAL_DURATION = 15 # Seconds

class RUNNING_ON:
  LINUX   = '24/7 server (aka my phone bruh)'
  WINDOWS = 'Debugging testbench'

MAIN_COLOR     = '#8000ff'
MAIN_COLOR_ALT = '#5000dd'
MAIN_COLOR_OLD = '#00ccff'

STATUS = "Used in DMs"

USE_TEST_TOKEN_IF_AVAILABLE = True