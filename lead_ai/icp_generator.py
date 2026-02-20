import json
from dataclasses import dataclass, asdict


@dataclass
class ICP:
    niche: str
    city: str
    min_followers: int
    max_followers: int
    min_posts_per_week: int

    def to_dict(self):
        return asdict(self)

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)


def generate_icp(niche: str, city: str, min_followers: int,
                 max_followers: int, min_posts_per_week: int) -> ICP:
    """
    Gera um Perfil Ideal de Cliente estruturado.
    """
    return ICP(
        niche=niche.lower(),
        city=city.lower(),
        min_followers=min_followers,
        max_followers=max_followers,
        min_posts_per_week=min_posts_per_week
    )