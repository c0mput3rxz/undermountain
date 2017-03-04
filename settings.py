"""
SETTINGS
Provide options and flags for users to customize.
"""
import os.path
from modules.core import Core
from modules.telnet import Telnet
from modules.websocket import Websocket


MODULES = (
    Core,
    Telnet,
    Websocket
)

DATA_PATH = os.path.dirname(__file__) + "/data"
ROT_DATA_PATH = DATA_PATH + "/__rot__"


PID_FILE = "pid"
SHUTDOWN_FILE = 'SHUTDOWN'
REBOOT_FILE = 'REBOOT'

TELNET_PORTS = (
    {"host": "0.0.0.0", "port": 4201},
    {"host": "0.0.0.0", "port": 4202},
)

WEBSOCKET_PORTS = (
    {"host": "0.0.0.0", "port": 14201},
    {"host": "0.0.0.0", "port": 14202},
)

DEBUG_CONNECTION_COUNTS = False
DEBUG_INPUT_TIMING = True

DIRECTIONS = {
    "north": {"name": "{Rnorth", "opposite_id": "south"},
    "east": {"name": "{Meast", "opposite_id": "west"},
    "south": {"name": "{rsouth", "opposite_id": "north"},
    "west": {"name": "{mwest", "opposite_id": "west"},
    "up": {"name": "{Yup", "opposite_id": "down"},
    "down": {"name": "{ydown", "opposite_id": "up"},
}

SWEAR_WORDS = (
    "cunt",
    "cunts",
    "fag",
    "faggot",
    "fags",
    "fuck",
    "fucker",
    "fucking",
    "fucked",
    "fucks",
    "nigger",
    "niggers",
)
SWEAR_WORDS_REPLACE_SYMBOL = "*"
SWEAR_WORDS_IGNORE_CHARS = "'\",\n\r-_?!"

ORGANIZATION_TYPES = {
    "clan": {
        "leader_count": 1,
        "ranks": [
            {
                "id": "leader",
                "name": "Leader",
                "who_symbol": "L",
                "rank": 1,

                "max_count": 1,
                "powers": {
                    "invite": True,
                    "remove": True,
                    "promote": True,
                    "demote": True
                }
            },
            {
                "id": "officer",
                "name": "Officer",
                "who_symbol": "O",
                "rank": 2,
                "powers": {
                    "invite": True,
                    "remove": True,
                    "promote": True,
                    "demote": True
                }

            },
            {
                "id": "member",
                "name": "Member",
                "who_symbol": "M",
                "rank": 3,
                "powers": {
                    "invite": False,
                    "remove": False,
                    "promote": False,
                    "demote": False
                }
            },
            {
                "id": "recruit",
                "name": "Recruit",
                "who_symbol": "R",
                "rank": 4,
                "powers": {
                    "invite": False,
                    "remove": False,
                    "promote": False,
                    "demote": False
                }
            }
        ]
    }
}
ORGANIZATIONS = {
    "vector": {
        "type_id": "clan",
        "name": "{MV{mectorian {ME{mmpire",
        "who_name": "{MV{mectr",
        "rank_names": {
            "leader": "{ML{meader",
            "officer": "{ML{meader",
            "member": "{MM{member",
            "recruit": "{MR{mecruit",
        }
    },
    "blackchurch": {
        "type_id": "clan",
        "name": "{8Black Church",
        "who_name": "BlkCh",
        "allies": [
            "radiantheart"
        ],
        "rank_names": {
            "leader": "Leader",
            "officer": "Officer",
            "member": "Member",
            "recruit": "Recruit",
        }
    },
    "strife": {
        "type_id": "clan",
        "name": "{MCh{murc{8h of S{mtrife",
        "who_name": "{MC{8o{MS",
        "rank_names": {
            "leader": "{MH{mig{8hpri{mes{Mt",
            "officer": "{MB{mi{8sh{mo{Mp",
            "member": "{MM{me{8mb{me{Mr",
            "recruit": "{MA{mc{8oly{mt{Me",
        }
    },
    "radiantheart": {
        "type_id": "clan",
        "allies": [
            "blackchurch"
        ],
        "name": "{RO{rr{yd{re{Rr {cof the {RR{rad{yi{ran{Rt H{re{ya{rr{Rt",
        "who_name": "{RR{rd{RH{rr{Rt",
        "rank_names": {
            "leader": "Lord Knight",
            "officer": "Officer",
            "member": "Member",
            "recruit": "Recruit",
        }
    },
}

CHANNELS = {
    "ooc": {
        "name": "Out Of Character",
        "default_active": True,
        "force_visible": True,
        "force_immortal_visible": False,
        "default_color": "{w",
        "self_format": "{{WYou OOC {{8'{{w{message}{{8'{{x",
        "format": "{{W[*OOC*]{{c{actor.name} {{8'{{w{message}{{8'{{x",
    },
    "bitch": {
        "name": "Bitch",
        "default_active": False,
        "confirmation": True,
        "confirmation_message": "Are you sure you wish to activate the trash channel?\nType 'trash' again if so.",
        "force_visible": True,
        "format": "{actor.name} {{RB{{ri{{Bt{{bc{{Bh{{re{{Rs {{8'{{Y{message}{{8'",
        "self_format": "{{WYou {{YBITCH {{8'{{Y{message}{{8'",
    },
    "clan": {
        "name": "Clan Chat",
        "self_format": "You clan '{{M{message}{{x'",
        "format": "{actor.name} clans '{{M{message}{{x'",
        "default_active": True,
        "activate_check": lambda self: self.clan_id is not None,
        "receive_check": lambda self, other: self.clan_id == other.clan_id,
        "send_check": lambda self: self.clan_id is not None,
    },
    "say": {
        "name": "Say",
        "format": "{{M{actor.name}{{M says {{x'{{m{message}{{x'",
        "self_format": "{{MYou say {{x'{{m{message}{{x'"
    },
    "immtalk": {
        "name": "Immortal Talk",
        "format": "{{x{actor.name}: {{W{message}{{x"
    },
    "auction": {
        "name": "Auction",
        "self_format": "{{xYou {{R<{{G-{{Y={{MA/B{{Y={{G-{{R> {{CAuction {{x'{{G{message}{{x'",
        "format": "{{x{actor.name} {{R<{{G-{{Y={{MA/B{{Y={{G-{{R> {{CAuctions {{x'{{G{message}{{x'",
    },
    "bid": {
        "name": "Bid",
        "self_format": "{{xYou {{R<{{G-{{Y={{MA/B{{Y={{G-{{R> {{CBid {{x'{{G{message}{{x'",
        "format": "{{x{actor.name} {{R<{{G-{{Y={{MA/B{{Y={{G-{{R> {{CBids {{x'{{G{message}{{x'",
    },
    "cgossip": {
        "name": "Clan Gossip",
        "self_format": "You cgossip '{{R{message}{{x'",
        "format": "{actor.name} cgossips '{{R{message}{{x'",
    },
    "agossip": {
        "name": "Area Gossip",
        "self_format": "{{xYou {{8({{Rag{{ro{{Bs{{rs{{Rip{{8) '{{B{message}{{x'",
        "format": "{{x{actor.name} {{8({{Rag{{ro{{Bs{{rs{{Rip{{8) '{{B{message}{{x'",
    },
    "gtell": {
        "name": "Group Tell",
        "self_format": "You tell the group '{{c{message}{{x'",
        "format": "{actor.name} tells the group '{{c{message}{{x'",
    },
    "quote": {
        "name": "Quote",
        "self_format": "You quote '{{g{message}{{x'",
        "format": "{actor.name} quotes '{{g{message}{{x'",
    },
    "heronet": {
        "name": "Heronet",
        "format": "{{g[{{R{actor.name} {{GHero-Nets{{g]:'{message}{{g'{{x",
        "self_format": "{{g[You {{GHero-Net{{g]:'{message}{{g'{{x",
    },
    "qgossip": {
        "name": "Quest Gossip",
        "format": "{{x{actor.name} {{C({{Wqg{{Bo{{bs{{Bs{{Wip{{C) {{x'{{C{message}{{x'",
        "self_format": "{{xYou {{C({{Wqg{{Bo{{bs{{Bs{{Wip{{C) {{x'{{C{message}{{x'",
    },
    "music": {
        "name": "Music",
        "format": "{actor.name} MUSIC: '{{C{message}{{x'",
        "self_format": "You MUSIC: '{{C{message}{{x'",
    },
    "ask": {
        "name": "Ask",
        "format": "{actor.name} [Q/A] Asks '{{Y{message}{{x'",
        "self_format": "You [Q/A] Ask '{{Y{message}{{x'",
    },
    "answer": {
        "name": "Answer",
        "format": "{actor.name} [Q/A] Answers '{{Y{message}{{x'",
        "self_format": "You [Q/A] Answer '{{Y{message}{{x'",
    },
    "grats": {
        "name": "Congratulations",
        "format": "{actor.name} {{Gg{{Yr{{Ra{{Bt{{Ms '{{y{message}{{x'",
        "self_format": "You grats '{{y{message}{{x'",
    },
    "shout": {
        "name": "Shout",
        "format": "{actor.name} shouts '{{r{message}{{x'",
        "self_format": "You shout '{{r{message}{{x'",
    },
}
