import flet as ft


def matlab_page(AMBER, NAVY, WHITE, LIGHT):
    """MATLAB Achievement Hub — 10 verified MathWorks certificates."""

    courses = [
        {"num": 1,  "title": "MATLAB Onramp",                                    "score": 100, "date": "13 March 2026",  "type": "Course",        "img": "certificates/matlab_c1.jpg"},
        {"num": 2,  "title": "Simulink Onramp",                                  "score": 100, "date": "13 April 2026",  "type": "Course",        "img": "certificates/matlab_c2.jpg"},
        {"num": 3,  "title": "Machine Learning Onramp",                          "score": 100, "date": "21 April 2026",  "type": "Course",        "img": "certificates/matlab_c3.jpg"},
        {"num": 4,  "title": "Calculations with Vectors and Matrices",           "score": 100, "date": "23 April 2026",  "type": "Course",        "img": "certificates/matlab_c4.jpg"},
        {"num": 5,  "title": "The How and Why of Writing Functions",             "score": 100, "date": "23 April 2026",  "type": "Course",        "img": "certificates/matlab_c5.jpg"},
        {"num": 6,  "title": "MATLAB Desktop Tools and Troubleshooting Scripts", "score": 100, "date": "27 April 2026",  "type": "Course",        "img": "certificates/matlab_c6.jpg"},
        {"num": 7,  "title": "Make and Manipulate Matrices",                     "score": 100, "date": "27 April 2026",  "type": "Course",        "img": "certificates/matlab_c7.jpg"},
        {"num": 8,  "title": "Explore Data with MATLAB Plots",                   "score": 100, "date": "28 April 2026",  "type": "Course",        "img": "certificates/matlab_c8.jpg"},
        {"num": 9,  "title": "Core MATLAB Skills",                               "score": 100, "date": "28 April 2026",  "type": "Learning Path", "img": "certificates/matlab_c9.jpg"},
        {"num": 10, "title": "Battery State Estimation",                         "score": 96,  "date": "28 April 2026",  "type": "Course",        "img": "certificates/matlab_c10.jpg"},
    ]

    done_count = len(courses)
    avg_score  = sum(c["score"] for c in courses) / done_count

    def cert_card(course):
        type_color  = "#4A9EFF" if course["type"] == "Learning Path" else AMBER
        score_color = "#22C55E" if course["score"] == 100 else AMBER

        return ft.Container(
            content=ft.Column(
                controls=[
                    # Header row
                    ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Text(str(course["num"]), color=NAVY, size=14,
                                                weight=ft.FontWeight.W_900,
                                                text_align=ft.TextAlign.CENTER),
                                width=34, height=34,
                                bgcolor=AMBER, border_radius=17,
                                alignment=ft.Alignment(0, 0),
                            ),
                            ft.Column(
                                controls=[
                                    ft.Text(course["title"], color=NAVY,
                                            weight=ft.FontWeight.W_700, size=13),
                                    ft.Text(course["date"],
                                            color=ft.Colors.with_opacity(0.5, NAVY), size=11),
                                ],
                                spacing=1, expand=True, tight=True,
                            ),
                            ft.Container(
                                content=ft.Text(course["type"], color=WHITE, size=10,
                                                weight=ft.FontWeight.W_600),
                                bgcolor=type_color, border_radius=10,
                                padding=ft.Padding.symmetric(horizontal=8, vertical=2),
                            ),
                            ft.Text(f"{course['score']}%", color=score_color,
                                    size=14, weight=ft.FontWeight.W_800),
                            ft.Icon(ft.Icons.CHECK_CIRCLE, color="#22C55E", size=20),
                        ],
                        spacing=10,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    # Certificate image
                    ft.Image(
                        src=course["img"],
                        fit="contain",
                        border_radius=ft.BorderRadius.all(8),
                        height=300,
                    ),
                ],
                spacing=10,
            ),
            bgcolor=WHITE,
            border_radius=12,
            padding=ft.Padding.symmetric(horizontal=14, vertical=12),
            shadow=ft.BoxShadow(blur_radius=6,
                                color=ft.Colors.with_opacity(0.07, NAVY),
                                offset=ft.Offset(0, 2)),
            border=ft.Border.only(left=ft.BorderSide(4, AMBER)),
        )

    stats_row = ft.Row(
        controls=[
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(f"{done_count}/10", color=AMBER, size=26, weight=ft.FontWeight.W_900),
                        ft.Text("Completed", color=ft.Colors.with_opacity(0.7, WHITE), size=11),
                    ],
                    spacing=2, horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                expand=True, alignment=ft.Alignment(0, 0),
            ),
            ft.Container(width=1, height=44, bgcolor=ft.Colors.with_opacity(0.2, WHITE)),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(f"{avg_score:.1f}%", color=AMBER, size=26, weight=ft.FontWeight.W_900),
                        ft.Text("Avg Score", color=ft.Colors.with_opacity(0.7, WHITE), size=11),
                    ],
                    spacing=2, horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                expand=True, alignment=ft.Alignment(0, 0),
            ),
            ft.Container(width=1, height=44, bgcolor=ft.Colors.with_opacity(0.2, WHITE)),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Mar–Apr 2026", color=AMBER, size=22, weight=ft.FontWeight.W_900),
                        ft.Text("All Completed", color=ft.Colors.with_opacity(0.7, WHITE), size=11),
                    ],
                    spacing=2, horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                expand=True, alignment=ft.Alignment(0, 0),
            ),
        ],
        spacing=0,
    )

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("📐  MATLAB Achievement Hub", color=WHITE,
                                    size=24, weight=ft.FontWeight.W_800),
                            ft.Text(
                                "Elizabeth Nghihangwa  ·  MathWorks Training Services  ·  10 Certificates",
                                color=ft.Colors.with_opacity(0.7, WHITE), size=12,
                            ),
                            ft.Container(height=8),
                            stats_row,
                        ],
                        spacing=4,
                    ),
                    bgcolor=NAVY,
                    padding=ft.Padding.symmetric(horizontal=32, vertical=20),
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[cert_card(c) for c in courses],
                        spacing=10,
                    ),
                    padding=ft.Padding.symmetric(horizontal=32, vertical=24),
                ),
            ],
            spacing=0,
        ),
        expand=True,
    )