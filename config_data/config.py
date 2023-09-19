from dataclasses import dataclass
from environs import Env
from typing import List

@dataclass
class TgBot:
    token: str
    admin_ids: List[int]

@dataclass
class Config:
    tg_bot: TgBot

def load_config(path: 'str | None' = None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(tg_bot=TgBot(token=env('BOT_TOKEN'),
                               admin_ids=map(int, env.list('ADMIN_IDS'))))
