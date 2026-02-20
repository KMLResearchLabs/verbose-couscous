from icp_generator import generate_icp
from instagram_finder import InstagramFinder
from analyzer import analyze_profile
from scorer import calculate_score, define_priority
from exporter import export_to_csv


def main():

    icp = generate_icp(
        niche="restaurante",
        city="sao paulo",
        min_followers=1000,
        max_followers=20000,
        min_posts_per_week=2
    )

    finder = InstagramFinder()
    profiles = finder.search_profiles(icp.niche, icp.city)

    final_leads = []

    for profile in profiles:

        ai_analysis = analyze_profile(profile)

        score = calculate_score(profile, icp, ai_analysis)
        priority = define_priority(score)

        final_leads.append({
            "username": profile["username"],
            "followers": profile["followers"],
            "score": score,
            "problemas": ai_analysis["problemas"],
            "prioridade": priority
        })

    export_to_csv(final_leads)


if __name__ == "__main__":
    main()