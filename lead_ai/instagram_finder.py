import os
import random
import time
from instagrapi import Client
from dotenv import load_dotenv
from typing import List, Dict


load_dotenv()


class InstagramFinder:

    def __init__(self):
        self.client = Client()
        self._login()

    def _login(self):
        username = os.getenv("IG_USERNAME")
        password = os.getenv("IG_PASSWORD")

        if not username or not password:
            raise Exception("Credenciais do Instagram não encontradas no .env")

        self.client.login(username, password)

    def _random_delay(self):
        time.sleep(random.uniform(3, 7))

    def search_profiles(self, niche: str, city: str, limit: int = 30) -> List[Dict]:
        """
        Busca perfis com base em hashtag e localização.
        """
        results = []

        try:
            hashtag_medias = self.client.hashtag_medias_recent(niche, amount=limit)

            for media in hashtag_medias:
                user = self.client.user_info(media.user.pk)

                profile_data = {
                    "username": user.username,
                    "bio": user.biography,
                    "followers": user.follower_count,
                    "posts": user.media_count,
                    "recent_captions": self._get_recent_captions(user.pk)
                }

                results.append(profile_data)
                self._random_delay()

        except Exception as e:
            print(f"Erro durante busca: {e}")

        return results

    def _get_recent_captions(self, user_id: int):
        captions = []
        try:
            medias = self.client.user_medias(user_id, amount=6)
            for media in medias:
                captions.append(media.caption_text or "")
        except Exception:
            pass
        return captions