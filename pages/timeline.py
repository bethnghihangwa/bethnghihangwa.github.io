import flet as ft


def timeline_page(AMBER, NAVY, WHITE, LIGHT):
    """Weekly project timeline — individual contributions to EngiTriad."""

    weeks = [
        {
            "week": "Week 1",
            "dates": "20 – 26 Jan 2026",
            "task": "Project Kickoff & SRS Contributions",
            "detail": (
                "Attended the group formation meeting. Contributed to Section 4.3 "
                "(Blasting Planner module) in the SRS document. Drafted the Firestore "
                "blastingEvents collection schema including fields: eventName, scheduledDate, "
                "blastLocation, crewAssignments, exclusionZone, and attachmentURL."
            ),
            "status": "Done",
        },
        {
            "week": "Week 2",
            "dates": "27 Jan – 2 Feb 2026",
            "task": "Figma UI Design — Blast Screens",
            "detail": (
                "Designed the Slope Stability Blast Calculator screen and Blast Results screen "
                "in Figma using the Amber (#DDA131) and Navy (#02153A) colour theme. Applied "
                "Inter font across all components and ensured consistent bottom-tab navigation flow."
            ),
            "status": "Done",
        },
        {
            "week": "Week 3",
            "dates": "3 – 9 Feb 2026",
            "task": "Firebase Setup & Auth Integration",
            "detail": (
                "Initialised the Firebase project. Configured Firebase Authentication with "
                "email/password provider. Stored all keys in a .env file and added it to "
                ".gitignore. Verified session persistence and UID-scoped Firestore security rules."
            ),
            "status": "Done",
        },
        {
            "week": "Week 4",
            "dates": "10 – 16 Feb 2026",
            "task": "Blasting Planner — Core Screen",
            "detail": (
                "Built the BlastingPlanner.jsx screen in React Native. Implemented form inputs "
                "for event name, scheduled date (DateTimePicker), blast location, materials list, "
                "crew assignments, and exclusion zone radius. Validated all required fields before "
                "allowing Firestore submission."
            ),
            "status": "Done",
        },
        {
            "week": "Week 5",
            "dates": "17 – 23 Feb 2026",
            "task": "Firestore Real-Time Sync",
            "detail": (
                "Integrated onSnapshot Firestore listener for the blastingEvents collection so all "
                "authorised personnel see live updates without manual refresh. Confirmed updates "
                "reflect within the 2-second NFR threshold on a 4G connection."
            ),
            "status": "Done",
        },
        {
            "week": "Week 6",
            "dates": "24 Feb – 2 Mar 2026",
            "task": "Firebase Storage — File Attachments",
            "detail": (
                "Added optional file/photo attachment to the Blasting Planner using Firebase Storage. "
                "On upload success the download URL is saved to the attachmentURL field of the "
                "corresponding blastingEvents Firestore document."
            ),
            "status": "Done",
        },
        {
            "week": "Week 7",
            "dates": "3 – 9 Mar 2026",
            "task": "Code Review & Pull Requests",
            "detail": (
                "Reviewed two pull requests from teammates: concrete grade validation logic and "
                "corrosion unit conversion. Raised inline comments on Firestore query efficiency "
                "and approved both merges after revisions."
            ),
            "status": "Done",
        },
        {
            "week": "Week 8",
            "dates": "10 – 16 Mar 2026",
            "task": "Portfolio Setup — Flet Framework",
            "detail": (
                "Scaffolded this Flet web portfolio. Created the project structure "
                "(main.py, components/navbar.py, pages/*), implemented the navigation system "
                "with active tab highlighting across all four pages (Timeline, Blog, GitHub, MATLAB), "
                "and deployed the app as a live web application. Added a centred hero banner with "
                "a glowing name display and circular profile photo. Built the GitHub Evidence page "
                "with real commit history grouped by date, verified badge indicators, and a PR log. "
                "Implemented the Blog page with embedded video support using ft.WebView so the "
                "contribution video plays directly inside the portfolio without redirecting to YouTube."
            ),
            "status": "Done",
        },
    ]

    def status_chip(status):
        bg = AMBER if status == "Done" else ft.Colors.with_opacity(0.15, AMBER)
        fg = NAVY if status == "Done" else AMBER
        return ft.Container(
            content=ft.Text(status, color=fg, size=11, weight=ft.FontWeight.W_600),
            bgcolor=bg,
            padding=ft.Padding.symmetric(horizontal=10, vertical=3),
            border_radius=20,
        )

    def week_card(entry, index):
        is_last = index == len(weeks) - 1
        return ft.Row(
            controls=[
                # Timeline spine
                ft.Column(
                    controls=[
                        ft.Container(
                            width=36, height=36,
                            bgcolor=AMBER if entry["status"] == "Done" else WHITE,
                            border=ft.Border.all(2, AMBER),
                            border_radius=18,
                            content=ft.Text(
                                "✓" if entry["status"] == "Done" else str(index + 1),
                                color=NAVY if entry["status"] == "Done" else AMBER,
                                size=14,
                                weight=ft.FontWeight.W_700,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            alignment=ft.Alignment(0, 0),
                        ),
                        ft.Container(
                            width=2,
                            height=80,
                            bgcolor=ft.Colors.with_opacity(0.0 if is_last else 0.3, AMBER),
                            margin=ft.Margin.only(left=17),
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=0,
                ),
                # Card
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Text(entry["week"], color=AMBER, weight=ft.FontWeight.W_800, size=13),
                                    ft.Text("·", color=ft.Colors.with_opacity(0.4, NAVY), size=13),
                                    ft.Text(entry["dates"], color=ft.Colors.with_opacity(0.55, NAVY), size=12),
                                    ft.Container(expand=True),
                                    status_chip(entry["status"]),
                                ],
                                spacing=6,
                            ),
                            ft.Text(entry["task"], color=NAVY, weight=ft.FontWeight.W_700, size=15),
                            ft.Text(entry["detail"], color=ft.Colors.with_opacity(0.7, NAVY), size=13, selectable=True),
                        ],
                        spacing=6,
                    ),
                    expand=True,
                    bgcolor=WHITE,
                    border_radius=12,
                    padding=16,
                    shadow=ft.BoxShadow(blur_radius=8, color=ft.Colors.with_opacity(0.07, NAVY), offset=ft.Offset(0, 2)),
                    margin=ft.Margin.only(bottom=8),
                ),
            ],
            spacing=16,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )

    rows = [week_card(w, i) for i, w in enumerate(weeks)]

    return ft.Container(
        content=ft.Column(
            controls=[
                # Section header
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("📅  Project Timeline", color=WHITE, size=24, weight=ft.FontWeight.W_800),
                            ft.Text(
                                "Weekly log of individual contributions to the EngiTriad group project.",
                                color=ft.Colors.with_opacity(0.75, WHITE),
                                size=13,
                            ),
                        ],
                        spacing=4,
                    ),
                    bgcolor=NAVY,
                    padding=ft.Padding.symmetric(horizontal=32, vertical=20),
                ),
                ft.Container(
                    content=ft.Column(controls=rows, spacing=0),
                    padding=ft.Padding.symmetric(horizontal=32, vertical=24),
                ),
            ],
            spacing=0,
        ),
        expand=True,
    )