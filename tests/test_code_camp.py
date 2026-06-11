import pytest


@pytest.mark.parametrize(
    "ideas, expected",
    [
        (
            [
                ["Add logging", 2, 5, 15],
                ["SEO optimization", 4, 8, 20],
                ["Fix bug", 1, 3, 5],
            ],
            ["Fix bug", "Add logging", "SEO optimization"],
        ),
        (
            [
                ["Dark mode", 1, 3, 8],
                ["Real-time collaboration feature", 6, 12, 20],
                ["Add tooltip", 1, 2, 4],
            ],
            ["Add tooltip", "Dark mode", "Real-time collaboration feature"],
        ),
        (
            [
                ["Update user profile page", 3, 7, 14],
                ["Add pagination", 2, 5, 10],
                ["Add tags", 2, 3, 6],
                ["Fix login bug", 1, 4, 8],
            ],
            ["Add tags", "Fix login bug", "Add pagination", "Update user profile page"],
        ),
        (
            [
                ["Migrate database", 14, 25, 40],
                ["Add chat assistant", 8, 15, 24],
                ["Redesign onboarding flow", 3, 7, 13],
                ["Add language support", 6, 11, 18],
            ],
            [
                "Redesign onboarding flow",
                "Add language support",
                "Add chat assistant",
                "Migrate database",
            ],
        ),
        (
            [
                ["Add email notifications", 3, 7, 10],
                ["Migrate deployment flow", 6, 10, 16],
                ["Add push notifications", 2, 6, 10],
                ["Optimize continuous integration", 5, 8, 15],
                ["Analyze user patterns", 5, 10, 18],
                ["Create onboarding curriculum", 6, 15, 25],
            ],
            [
                "Add push notifications",
                "Add email notifications",
                "Analyze user patterns",
                "Migrate deployment flow",
                "Optimize continuous integration",
                "Create onboarding curriculum",
            ],
        ),
    ],
)
def test_analyze_ideas(ideas, expected):
    from code_camp import analyze_ideas

    result = analyze_ideas(ideas)

    assert result == expected, f"expected {expected} but got {result}"
