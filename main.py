import flet as ft
import math
import time
import threading
import random
from pages.timeline import timeline_page
from pages.blog import blog_page
from pages.github import github_page
from pages.matlab import matlab_page
from components.navbar import build_navbar

AMBER = "#DDA131"
NAVY  = "#02153A"
WHITE = "#FFFFFF"
LIGHT = "#EFF4FB"
GLOW  = "#FFD966"
SKY   = "#D6E8FF"


# ─────────────────────────────────────────────
#  BUTTERFLY — pure Flet controls, no canvas
# ─────────────────────────────────────────────

def make_butterfly_widget(b: dict) -> ft.Container:
    """
    Build one butterfly as a Stack of rotated Containers (wings) + a body.
    Wing beat is simulated by toggling the wing width (open/closed).
    """
    size   = b["size"]
    wu     = size * 0.85   # upper wing width
    wl     = size * 0.60   # lower wing width
    wh_u   = size * 0.55   # upper wing height
    wh_l   = size * 0.38   # lower wing height

    # ── wings ──
    left_upper = ft.Container(
        width=wu, height=wh_u,
        bgcolor=b["wing1"],
        border_radius=ft.BorderRadius.only(
            top_left=wu, top_right=4, bottom_left=4, bottom_right=4,
        ),
        rotate=ft.Rotate(angle=0.18),
        animate_rotation=ft.Animation(180, ft.AnimationCurve.EASE_IN_OUT),
    )
    right_upper = ft.Container(
        width=wu, height=wh_u,
        bgcolor=b["wing1"],
        border_radius=ft.BorderRadius.only(
            top_left=4, top_right=wu, bottom_left=4, bottom_right=4,
        ),
        rotate=ft.Rotate(angle=-0.18),
        animate_rotation=ft.Animation(180, ft.AnimationCurve.EASE_IN_OUT),
    )
    left_lower = ft.Container(
        width=wl, height=wh_l,
        bgcolor=b["wing2"],
        border_radius=ft.BorderRadius.only(
            top_left=4, top_right=4, bottom_left=wl, bottom_right=4,
        ),
        rotate=ft.Rotate(angle=0.25),
        animate_rotation=ft.Animation(180, ft.AnimationCurve.EASE_IN_OUT),
    )
    right_lower = ft.Container(
        width=wl, height=wh_l,
        bgcolor=b["wing2"],
        border_radius=ft.BorderRadius.only(
            top_left=4, top_right=4, bottom_left=4, bottom_right=wl,
        ),
        rotate=ft.Rotate(angle=-0.25),
        animate_rotation=ft.Animation(180, ft.AnimationCurve.EASE_IN_OUT),
    )
    body = ft.Container(
        width=4, height=size * 0.65,
        bgcolor=b["body"],
        border_radius=2,
    )

    # Store refs for animation
    b["ctrl_lu"] = left_upper
    b["ctrl_ru"] = right_upper
    b["ctrl_ll"] = left_lower
    b["ctrl_rl"] = right_lower

    wing_stack = ft.Stack(
        controls=[
            ft.Container(left=0,        top=0,          content=left_upper),
            ft.Container(left=wu + 4,   top=0,          content=right_upper),
            ft.Container(left=0,        top=wh_u - 4,   content=left_lower),
            ft.Container(left=wu + 4,   top=wh_u - 4,   content=right_lower),
            ft.Container(left=wu - 1,   top=2,          content=body),
        ],
        width=wu * 2 + 4,
        height=wh_u + wh_l,
    )

    butterfly = ft.Container(
        content=wing_stack,
        left=b["px"],
        top=b["py"],
        animate_position=ft.Animation(320, ft.AnimationCurve.EASE_IN_OUT),
        opacity=b["alpha"],
        animate_opacity=ft.Animation(600, ft.AnimationCurve.EASE_IN_OUT),
    )
    b["ctrl"] = butterfly
    return butterfly


def make_butterfly_overlay(side: str, count: int = 5):
    """
    Returns (stack_container, start_animation_fn).
    The stack is absolutely positioned and transparent to pointer events.
    """
    rng = random.Random(7 if side == "left" else 13)

    WING_COLORS = [
        ("#A8C8F0", "#D0E8FF"),
        ("#85B3F0", "#C2D9FF"),
        ("#9BB8E8", "#C8DAEF"),
        ("#7EB5E8", "#B8D4F5"),
    ]

    butterflies = []
    for i in range(count):
        wc = rng.choice(WING_COLORS)
        size = rng.uniform(18, 30)
        if side == "left":
            px = rng.uniform(10, 90)
        else:
            px = rng.uniform(10, 90)   # relative within its column
        py = rng.uniform(20, 260)

        b = {
            "px":     px,
            "py":     py,
            "vy":     rng.uniform(-0.4, 0.4),
            "vx":     rng.uniform(-0.2, 0.2),
            "phase":  rng.uniform(0, math.pi * 2),
            "beat":   False,
            "size":   size,
            "wing1":  ft.Colors.with_opacity(rng.uniform(0.55, 0.80), wc[0]),
            "wing2":  ft.Colors.with_opacity(rng.uniform(0.35, 0.60), wc[1]),
            "body":   ft.Colors.with_opacity(rng.uniform(0.65, 0.85), "#4A7CC7"),
            "alpha":  rng.uniform(0.55, 0.85),
            "ctrl":   None,
            "ctrl_lu": None, "ctrl_ru": None,
            "ctrl_ll": None, "ctrl_rl": None,
            "beat_timer": 0,
            "beat_interval": rng.uniform(0.25, 0.55),
        }
        butterflies.append(b)

    widgets = [make_butterfly_widget(b) for b in butterflies]

    overlay = ft.Stack(
        controls=widgets,
        expand=True,
    )

    running = {"v": False}

    def start():
        if running["v"]:
            return
        running["v"] = True

        def tick():
            t = 0.0
            while running["v"]:
                time.sleep(0.35)
                t += 0.35
                needs_update = False
                for b in butterflies:
                    if b["ctrl"] is None:
                        continue

                    # Drift position
                    b["px"] += b["vx"] * 12
                    b["py"] += b["vy"] * 12

                    # Gentle bounce
                    if b["px"] < 4:
                        b["vx"] = abs(b["vx"])
                    elif b["px"] > 75:
                        b["vx"] = -abs(b["vx"])
                    if b["py"] < 4:
                        b["vy"] = abs(b["vy"])
                    elif b["py"] > 270:
                        b["vy"] = -abs(b["vy"])

                    b["ctrl"].left = b["px"]
                    b["ctrl"].top  = b["py"]

                    # Wing beat
                    b["beat_timer"] += 0.35
                    if b["beat_timer"] >= b["beat_interval"]:
                        b["beat_timer"] = 0
                        b["beat"] = not b["beat"]
                        angle_open  =  0.18
                        angle_close =  0.75
                        lu_a = angle_close if b["beat"] else angle_open
                        ru_a = -lu_a
                        ll_a = 0.35 if b["beat"] else 0.12
                        rl_a = -ll_a
                        if b["ctrl_lu"]:
                            b["ctrl_lu"].rotate.angle = lu_a
                            b["ctrl_ru"].rotate.angle = ru_a
                            b["ctrl_ll"].rotate.angle = ll_a
                            b["ctrl_rl"].rotate.angle = rl_a

                    needs_update = True

                if needs_update:
                    try:
                        overlay.update()
                    except Exception:
                        break

        th = threading.Thread(target=tick, daemon=True)
        th.start()

    return overlay, start


# ─────────────────────────────────────────────
#  HERO BANNER
# ─────────────────────────────────────────────
def hero_banner(AMBER, NAVY, WHITE, LIGHT):
    glow_name = ft.Stack(
        controls=[
            ft.Text(
                "Elizabeth Faith Nghihangwa",
                size=32, weight=ft.FontWeight.W_900,
                color=ft.Colors.with_opacity(0.28, GLOW),
                text_align=ft.TextAlign.CENTER,
                style=ft.TextStyle(shadow=ft.BoxShadow(
                    blur_radius=32,
                    color=ft.Colors.with_opacity(0.65, AMBER),
                    offset=ft.Offset(0, 0),
                )),
            ),
            ft.Text(
                "Elizabeth Faith Nghihangwa",
                size=32, weight=ft.FontWeight.W_900,
                color=AMBER,
                text_align=ft.TextAlign.CENTER,
                style=ft.TextStyle(shadow=ft.BoxShadow(
                    blur_radius=14,
                    color=ft.Colors.with_opacity(0.85, AMBER),
                    offset=ft.Offset(0, 0),
                )),
            ),
        ],
        alignment=ft.Alignment(0, 0),
    )

    profile_pic = ft.Container(
        content=ft.Stack(
            controls=[
                ft.Container(
                    width=148, height=148, border_radius=74,
                    bgcolor="transparent",
                    shadow=ft.BoxShadow(
                        blur_radius=34,
                        color=ft.Colors.with_opacity(0.5, AMBER),
                        offset=ft.Offset(0, 0),
                    ),
                ),
                ft.Container(
                    width=148, height=148, border_radius=74,
                    border=ft.Border.all(4, AMBER),
                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                    content=ft.Image(
                        src="profile.jpeg",
                        width=148, height=148,
                        fit=ft.BoxFit.COVER,
                    ),
                ),
            ],
            alignment=ft.Alignment(0, 0),
        ),
        alignment=ft.Alignment(0, 0),
    )

    hero_content = ft.Container(
        content=ft.Column(
            controls=[
                profile_pic,
                ft.Container(height=14),
                glow_name,
                ft.Container(height=4),
                ft.Text(
                    "Computer Programming I  ·  2026",
                    size=13,
                    color=ft.Colors.with_opacity(0.6, NAVY),
                    text_align=ft.TextAlign.CENTER,
                    weight=ft.FontWeight.W_500,
                ),
                ft.Container(height=8),
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Text("EngiTriad", color=NAVY, size=11, weight=ft.FontWeight.W_700),
                            bgcolor=AMBER, border_radius=14,
                            padding=ft.Padding.symmetric(horizontal=14, vertical=5),
                        ),
                        ft.Container(
                            content=ft.Text("Blasting Planner Lead", color=NAVY, size=11, weight=ft.FontWeight.W_600),
                            bgcolor=ft.Colors.with_opacity(0.13, NAVY), border_radius=14,
                            padding=ft.Padding.symmetric(horizontal=14, vertical=5),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=8,
                ),
                ft.Container(height=20),
                ft.Container(
                    content=ft.Text("▼", size=18, color=ft.Colors.with_opacity(0.30, NAVY)),
                    alignment=ft.Alignment(0, 0),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=4,
        ),
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, -1),
            end=ft.Alignment(0, 1),
            colors=[WHITE, SKY, LIGHT],
        ),
        padding=ft.Padding.symmetric(vertical=44, horizontal=24),
        alignment=ft.Alignment(0, 0),
        expand=True,
    )

    return hero_content


# ─────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────
def main(page: ft.Page):
    page.title = "Web Portfolio — EngiTriad"
    page.bgcolor = LIGHT
    page.padding = 0
    page.scroll = ft.ScrollMode.HIDDEN
    page.window.width  = 1140
    page.window.height = 820

    # ── Butterfly overlays ──────────────────────
    left_overlay,  start_left  = make_butterfly_overlay("left",  5)
    right_overlay, start_right = make_butterfly_overlay("right", 5)

    left_strip = ft.Container(
        content=left_overlay,
        width=110,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, -1),
            end=ft.Alignment(0, 1),
            colors=[WHITE, SKY, LIGHT],
        ),
    )
    right_strip = ft.Container(
        content=right_overlay,
        width=110,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, -1),
            end=ft.Alignment(0, 1),
            colors=[WHITE, SKY, LIGHT],
        ),
    )

    # ── Hero centre ─────────────────────────────
    hero_centre = hero_banner(AMBER, NAVY, WHITE, LIGHT)

    hero_row = ft.Row(
        controls=[left_strip, hero_centre, right_strip],
        spacing=0,
        expand=True,
        vertical_alignment=ft.CrossAxisAlignment.STRETCH,
    )

    hero_wrapper = ft.Container(
        content=hero_row,
        height=360,
        visible=True,
    )

    # ── Content area ────────────────────────────
    content_area = ft.Column(
        controls=[timeline_page(AMBER, NAVY, WHITE, LIGHT)],
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        spacing=0,
    )

    # ── Navbar ──────────────────────────────────
    navbar, set_hero_visible = build_navbar(
        lambda route, _=None: navigate(route),
        AMBER, NAVY, WHITE,
    )

    hero_visible = {"val": True}

    def navigate(route: str):
        page_map = {
            "timeline": timeline_page,
            "blog":     blog_page,
            "github":   github_page,
            "matlab":   matlab_page,
        }
        builder = page_map.get(route)
        if not builder:
            return

        content_area.controls.clear()

        if route == "timeline":
            if not hero_visible["val"]:
                hero_visible["val"] = True
                hero_wrapper.visible = True
                set_hero_visible(True)
        else:
            if hero_visible["val"]:
                hero_visible["val"] = False
                hero_wrapper.visible = False
                set_hero_visible(False)

        content_area.controls.append(builder(AMBER, NAVY, WHITE, LIGHT))
        page.update()

    def after_mount(e):
        start_left()
        start_right()

    page.on_resized = after_mount

    page.add(
        ft.Column(
            controls=[
                navbar,
                ft.Container(
                    content=ft.Column(
                        controls=[hero_wrapper, content_area],
                        spacing=0,
                        expand=True,
                    ),
                    expand=True,
                ),
            ],
            expand=True,
            spacing=0,
        )
    )

    start_left()
    start_right()


if __name__ == "__main__":
    # Updated to deployment friendly configuration
    ft.app(target=main, assets_dir="assets")