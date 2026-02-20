import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_profile(profile: dict) -> dict:
    """
    Analisa perfil usando heurísticas + IA.
    """

    prompt = f"""
    Analise este perfil comercial do Instagram:

    Bio: {profile['bio']}
    Seguidores: {profile['followers']}
    Posts: {profile['posts']}
    Últimas legendas: {profile['recent_captions']}

    Avalie:
    1. Clareza da proposta
    2. Problemas visuais potenciais
    3. Oportunidades de melhoria
    4. Nota de 0 a 100
    Responda em JSON com campos:
    problemas, oportunidades, nota
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
    )

    return eval(response.choices[0].message.content)