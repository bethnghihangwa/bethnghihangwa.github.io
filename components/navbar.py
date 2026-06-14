import flet as ft


def build_navbar(on_navigate, AMBER, NAVY, WHITE, page=None):
    """
    Top navigation bar.
    - Shows 'Elizabeth Faith Nghihangwa' subtly when hero is hidden.
    - Returns (navbar_widget, set_hero_visible_fn).
    """

    GLOW = "#FFD966"

    nav_items = [
        ("timeline", "📅", "Timeline"),
        ("blog",     "✍️",  "Blog"),
        ("github",   "🐙", "GitHub"),
        ("matlab",   "📐", "MATLAB"),
    ]

    selected = {"route": "timeline"}

    # Name display in navbar — shown only when hero is off-screen
    name_in_navbar = ft.AnimatedSwitcher(
        content=ft.Container(key="empty", width=0),
        transition=ft.AnimatedSwitcherTransition.FADE,
        duration=400,
        reverse_duration=300,
    )

    def set_hero_visible(is_visible: bool):
        if is_visible:
            name_in_navbar.content = ft.Container(key="empty", width=0)
        else:
            name_in_navbar.content = ft.Row(
                key="name",
                controls=[
                    ft.Container(
                        content=ft.Text(
                            "Elizabeth Faith Nghihangwa",
                            color=AMBER,
                            weight=ft.FontWeight.W_700,
                            size=14,
                            style=ft.TextStyle(
                                shadow=ft.BoxShadow(
                                    blur_radius=10,
                                    color=ft.Colors.with_opacity(0.55, AMBER),
                                    offset=ft.Offset(0, 0),
                                )
                            ),
                        ),
                        margin=ft.Margin.only(left=8),
                    ),
                    ft.Container(
                        width=1,
                        height=18,
                        bgcolor=ft.Colors.with_opacity(0.25, WHITE),
                        margin=ft.Margin.symmetric(horizontal=10),
                    ),
                ],
                spacing=0,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
        try:
            name_in_navbar.update()
        except Exception:
            pass

    nav_row = ft.Row(controls=[], spacing=2, wrap=True)

    def build_button(route, icon, label):
        is_active = selected["route"] == route

        def make_handler(r):
            def handler(e):
                selected["route"] = r
                on_navigate(r)
                nav_row.controls.clear()
                for ri, ic, lb in nav_items:
                    nav_row.controls.append(build_button(ri, ic, lb))
                nav_row.update()
            return handler

        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text(icon, size=15),
                    ft.Text(
                        label,
                        color=AMBER if is_active else ft.Colors.with_opacity(0.78, WHITE),
                        weight=ft.FontWeight.W_700 if is_active else ft.FontWeight.W_400,
                        size=14,
                    ),
                ],
                spacing=6,
                tight=True,
            ),
            padding=ft.Padding.symmetric(horizontal=18, vertical=8),
            border_radius=10,
            bgcolor=ft.Colors.with_opacity(0.14, WHITE) if is_active else "transparent",
            border=ft.Border.all(1, ft.Colors.with_opacity(0.18, AMBER)) if is_active else None,
            on_click=make_handler(route),
            ink=True,
        )

    for route, icon, label in nav_items:
        nav_row.controls.append(build_button(route, icon, label))

    # Brand monogram
    brand = ft.Container(
        content=ft.Text("EFN", color=NAVY, weight=ft.FontWeight.W_900, size=13),
        width=40, height=40,
        bgcolor=AMBER,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        shadow=ft.BoxShadow(blur_radius=8, color=ft.Colors.with_opacity(0.4, AMBER), offset=ft.Offset(0, 2)),
    )

    portfolio_label = ft.Column(
        controls=[
            ft.Text("Web Portfolio", color=WHITE, weight=ft.FontWeight.W_800, size=18),
            ft.Text(
                "Computer Programming I  ·  2026",
                color=ft.Colors.with_opacity(0.55, WHITE),
                size=10,
            ),
        ],
        spacing=2,
        tight=True,
    )

    divider = ft.Container(
        height=1,
        bgcolor=ft.Colors.with_opacity(0.15, WHITE),
        margin=ft.Margin.symmetric(vertical=7),
    )

    navbar = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        brand,
                        ft.Container(width=12),
                        portfolio_label,
                        ft.Container(expand=True),
                        name_in_navbar,
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=0,
                ),
                divider,
                nav_row,
            ],
            spacing=0,
        ),
        bgcolor=NAVY,
        padding=ft.Padding.symmetric(horizontal=28, vertical=14),
        shadow=ft.BoxShadow(
            blur_radius=18,
            color=ft.Colors.with_opacity(0.30, NAVY),
            offset=ft.Offset(0, 5),
        ),
    )

    return navbar, set_hero_visible
