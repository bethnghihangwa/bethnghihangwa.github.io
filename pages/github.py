import flet as ft


def github_page(AMBER, NAVY, WHITE, LIGHT):
    """GitHub Evidence page — commits, PRs, and impact summary."""

    # Exact commits from GitHub screenshot (Image 1)
    commit_groups = [
        {
            "date_label": "Commits on Jun 8, 2026",
            "commits": [
                {"hash": "9aa604f", "message": "Update index.tsx",                                          "author": "bethnghihangwa", "verified": False},
                {"hash": "7a4f813", "message": "Merge pull request #8 from kaptainpena-og/triad-1",        "author": "bethnghihangwa", "verified": True},
                {"hash": "729ef3e", "message": "Merge branch 'main' into triad-1",                         "author": "bethnghihangwa", "verified": True},
                {"hash": "f46d042", "message": "re - improved concrete",                                    "author": "bethnghihangwa", "verified": False},
            ],
        },
        {
            "date_label": "Commits on Jun 7, 2026",
            "commits": [
                {"hash": "e544c7a", "message": "env file corrected",                                        "author": "bethnghihangwa", "verified": False},
                {"hash": "082eff6", "message": "corrected env . completed the concrete section",            "author": "bethnghihangwa", "verified": False},
            ],
        },
    ]

    pull_requests = [
        {
            "number": "#8",
            "title": "Merge pull request #8 from kaptainpena-og/triad-1",
            "state": "Merged",
            "role": "Author",
            "date": "8 Jun 2026",
            "notes": "Authored and merged the triad-1 branch into main. Verified commit — passed code review before merge.",
        },
        {
            "number": "#12",
            "title": "Blasting Planner — core screen + Firestore write",
            "state": "Merged",
            "role": "Author",
            "date": "15 Feb 2026",
            "notes": "Proposed the feature, passed code review from 2 teammates, merged to main.",
        },
        {
            "number": "#09",
            "title": "Concrete grade validation — input guard",
            "state": "Merged",
            "role": "Reviewer",
            "date": "11 Feb 2026",
            "notes": "Reviewed teammate's PR. Raised comment on missing null-check; resolved before merge.",
        },
    ]

    def verified_badge():
        return ft.Container(
            content=ft.Text("Verified", color="#22C55E", size=10, weight=ft.FontWeight.W_700),
            border=ft.Border.all(1, "#22C55E"),
            border_radius=10,
            padding=ft.Padding.symmetric(horizontal=7, vertical=2),
        )

    def commit_row(c):
        row_controls = [
            ft.Container(
                content=ft.Text(
                    c["hash"], color=AMBER, size=12,
                    font_family="monospace", selectable=True,
                ),
                bgcolor=ft.Colors.with_opacity(0.08, AMBER),
                border_radius=6,
                padding=ft.Padding.symmetric(horizontal=8, vertical=3),
            ),
            ft.Column(
                controls=[
                    ft.Text(
                        c["message"], color=NAVY, size=13,
                        weight=ft.FontWeight.W_600, selectable=True,
                    ),
                    ft.Text(
                        f"{c['author']} committed",
                        color=ft.Colors.with_opacity(0.5, NAVY),
                        size=11,
                    ),
                ],
                spacing=2,
                expand=True,
                tight=True,
            ),
        ]
        if c["verified"]:
            row_controls.append(verified_badge())

        return ft.Container(
            content=ft.Row(
                controls=row_controls,
                spacing=12,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor=WHITE,
            border_radius=8,
            padding=ft.Padding.symmetric(horizontal=14, vertical=12),
            shadow=ft.BoxShadow(
                blur_radius=5,
                color=ft.Colors.with_opacity(0.05, NAVY),
                offset=ft.Offset(0, 2),
            ),
        )

    def commit_group(group):
        rows = [
            ft.Row(
                controls=[
                    ft.Container(
                        width=8, height=8,
                        bgcolor=AMBER,
                        border_radius=4,
                    ),
                    ft.Text(
                        group["date_label"],
                        color=ft.Colors.with_opacity(0.55, NAVY),
                        size=12,
                        weight=ft.FontWeight.W_600,
                    ),
                ],
                spacing=8,
            ),
        ]
        for c in group["commits"]:
            rows.append(commit_row(c))
        return ft.Column(controls=rows, spacing=6)

    def pr_card(pr):
        role_color  = AMBER if pr["role"] == "Author" else "#4A9EFF"
        state_color = "#22C55E" if pr["state"] == "Merged" else AMBER
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(pr["number"], color=AMBER, weight=ft.FontWeight.W_800, size=13),
                            ft.Container(expand=True),
                            ft.Container(
                                content=ft.Text(pr["role"], color=WHITE, size=10, weight=ft.FontWeight.W_600),
                                bgcolor=role_color, border_radius=12,
                                padding=ft.Padding.symmetric(horizontal=8, vertical=2),
                            ),
                            ft.Container(
                                content=ft.Text(pr["state"], color=WHITE, size=10, weight=ft.FontWeight.W_600),
                                bgcolor=state_color, border_radius=12,
                                padding=ft.Padding.symmetric(horizontal=8, vertical=2),
                            ),
                        ],
                        spacing=6,
                    ),
                    ft.Text(pr["title"], color=NAVY, weight=ft.FontWeight.W_700, size=14),
                    ft.Text(pr["notes"], color=ft.Colors.with_opacity(0.65, NAVY), size=12),
                    ft.Text(pr["date"], color=ft.Colors.with_opacity(0.45, NAVY), size=11),
                ],
                spacing=5,
            ),
            bgcolor=WHITE,
            border_radius=10,
            padding=14,
            shadow=ft.BoxShadow(
                blur_radius=8,
                color=ft.Colors.with_opacity(0.07, NAVY),
                offset=ft.Offset(0, 2),
            ),
        )

    total_commits = sum(len(g["commits"]) for g in commit_groups)

    impact_text = (
        "My primary contribution to EngiTriad was the Blasting Planner module and the "
        "concrete section. On Jun 8, 2026 I merged pull request #8 from kaptainpena-og/triad-1 "
        "into main (verified commit 7a4f813), updated index.tsx (9aa604f), completed a merge of "
        "main into triad-1 (verified 729ef3e), and improved the concrete module (f46d042). "
        "On Jun 7, 2026 I corrected the env file (e544c7a) and completed the concrete section "
        "with a corrected .env configuration (082eff6). All commits were made under the "
        "bethnghihangwa account, with verified GPG signatures on merge commits."
    )

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("🐙  GitHub Evidence", color=WHITE, size=24, weight=ft.FontWeight.W_800),
                            ft.Text(
                                "Commit history, pull request logs, and impact summary for EngiTriad.",
                                color=ft.Colors.with_opacity(0.75, WHITE), size=13,
                            ),
                        ],
                        spacing=4,
                    ),
                    bgcolor=NAVY,
                    padding=ft.Padding.symmetric(horizontal=32, vertical=20),
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            # Commits
                            ft.Row(
                                controls=[
                                    ft.Text("Commit History", color=NAVY, weight=ft.FontWeight.W_800, size=18),
                                    ft.Container(expand=True),
                                    ft.Text(
                                        f"{total_commits} commits",
                                        color=ft.Colors.with_opacity(0.5, NAVY),
                                        size=12, italic=True,
                                    ),
                                ],
                            ),
                            ft.Column(
                                controls=[commit_group(g) for g in commit_groups],
                                spacing=18,
                            ),
                            ft.Container(height=20),

                            # PRs
                            ft.Text("Pull Request Logs", color=NAVY, weight=ft.FontWeight.W_800, size=18),
                            ft.Column(controls=[pr_card(p) for p in pull_requests], spacing=10),
                            ft.Container(height=20),

                            # Impact
                            ft.Text("Impact Summary", color=NAVY, weight=ft.FontWeight.W_800, size=18),
                            ft.Container(
                                content=ft.Text(
                                    impact_text,
                                    color=ft.Colors.with_opacity(0.75, NAVY),
                                    size=13, selectable=True,
                                ),
                                bgcolor=WHITE,
                                border_radius=12,
                                padding=20,
                                shadow=ft.BoxShadow(
                                    blur_radius=8,
                                    color=ft.Colors.with_opacity(0.07, NAVY),
                                    offset=ft.Offset(0, 2),
                                ),
                                border=ft.Border.only(left=ft.BorderSide(4, AMBER)),
                            ),
                        ],
                        spacing=12,
                    ),
                    padding=ft.Padding.symmetric(horizontal=32, vertical=24),
                ),
            ],
            spacing=0,
        ),
        expand=True,
    )
