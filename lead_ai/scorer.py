def calculate_score(profile: dict, icp, ai_analysis: dict) -> float:

    score = 0

    # Followers Score (30)
    if icp.min_followers <= profile["followers"] <= icp.max_followers:
        score += 30
    else:
        score += 10

    # Frequência estimada (25)
    posts_score = min(profile["posts"] / 100, 1) * 25
    score += posts_score

    # Engajamento estimado simples (20)
    engagement_estimate = min(profile["followers"] / 1000, 1)
    score += engagement_estimate * 20

    # Problemas detectados (25)
    opportunity_score = (100 - ai_analysis["nota"]) / 100
    score += opportunity_score * 25

    return round(score, 2)


def define_priority(score: float) -> str:
    if score >= 75:
        return "Alta"
    elif score >= 50:
        return "Média"
    return "Baixa"