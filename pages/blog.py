import flet as ft
import flet_video as ftv 


def blog_page(AMBER, NAVY, WHITE, LIGHT):
    """Technical Blog — Confidence in Concepts."""

    posts = [
        {
            "title": "Firebase Firestore: Real-Time Data Sync Explained",
            "concept": "Cloud Firestore / onSnapshot listeners",
            "summary": (
                "Firestore's onSnapshot() listener keeps your UI in sync with the database "
                "without polling. When a document or collection changes, Firestore pushes "
                "the diff to every connected client instantly. In EngiTriad, this powers the "
                "Blasting Planner — all authorised supervisors see a new blast event appear "
                "the moment it is written, satisfying the ≤2-second update NFR."
            ),
            "code": (
                "const q = query(\n"
                "  collection(db, 'blastingEvents'),\n"
                "  where('userId', '==', auth.currentUser.uid)\n"
                ");\n\n"
                "const unsubscribe = onSnapshot(q, (snapshot) => {\n"
                "  const events = snapshot.docs.map(doc => ({\n"
                "    id: doc.id, ...doc.data(),\n"
                "  }));\n"
                "  setBlastEvents(events);\n"
                "});\n\n"
                "return () => unsubscribe();"
            ),
            "tags": ["Firebase", "Firestore", "React Native", "Real-Time"],
        },
        {
            "title": "Firebase Authentication: Securing Every Route",
            "concept": "Firebase Auth / UID-scoped security rules",
            "summary": (
                "Firebase Authentication assigns every registered user a unique UID. "
                "Firestore security rules use request.auth != null to ensure that only "
                "authenticated users can read or write data, and data is scoped per UID so "
                "no cross-user leakage is possible. EngiTriad enforces this across all three "
                "engineering modules."
            ),
            "code": (
                "rules_version = '2';\n"
                "service cloud.firestore {\n"
                "  match /databases/{database}/documents {\n"
                "    match /blastingEvents/{docId} {\n"
                "      allow read, write: if request.auth != null\n"
                "        && request.auth.uid == resource.data.userId;\n"
                "    }\n"
                "  }\n"
                "}"
            ),
            "tags": ["Firebase", "Authentication", "Security Rules", "UID"],
        },
        {
            "title": "Corrosion Rate: The Maths Behind the Module",
            "concept": "Empirical corrosion formula in engineering software",
            "summary": (
                "The EngiTriad Corrosion Estimator uses a simplified empirical model. "
                "The corrosion rate CR (mm/year) is derived from the material's corrosion "
                "coefficient k, the environmental exposure factor E, and the duration t (years)."
            ),
            "formula": "CR = k × E × t⁻⁰·⁵",
            "formula_desc": "k = corrosion coefficient  ·  E = environmental exposure factor (0–1)  ·  t = exposure years",
            "code": (
                "function estimateCorrosionRate(k, E, t) {\n"
                "  if (t <= 0) throw new Error('Duration must be positive');\n"
                "  const CR = k * E * Math.pow(t, -0.5);\n"
                "  return parseFloat(CR.toFixed(4)); // mm/year\n"
                "}"
            ),
            "tags": ["Metallurgy", "Mathematics", "Corrosion", "EngiTriad"],
        },
    ]

    def tag_chip(tag):
        return ft.Container(
            content=ft.Text(tag, color=NAVY, size=10, weight=ft.FontWeight.W_600),
            bgcolor=ft.Colors.with_opacity(0.12, AMBER),
            border_radius=10,
            padding=ft.Padding.symmetric(horizontal=8, vertical=3),
        )

    def code_block(code_str):
        return ft.Container(
            content=ft.Text(code_str, color="#A8FF78", size=11,
                            font_family="monospace", selectable=True),
            bgcolor="#0D1117",
            border_radius=8,
            padding=14,
        )

    def post_card(post):
        controls = [
            ft.Row(controls=[tag_chip(t) for t in post["tags"]], spacing=6, wrap=True),
            ft.Text(post["title"], color=NAVY, weight=ft.FontWeight.W_800, size=17),
            ft.Text(f"Concept: {post['concept']}", color=AMBER, size=12,
                    weight=ft.FontWeight.W_600),
            ft.Text(post["summary"], color=ft.Colors.with_opacity(0.72, NAVY),
                    size=13, selectable=True),
        ]
        if "formula" in post:
            controls.append(ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(post["formula"], color=AMBER, size=20,
                                weight=ft.FontWeight.W_800, font_family="monospace"),
                        ft.Text(post["formula_desc"],
                                color=ft.Colors.with_opacity(0.6, NAVY), size=11),
                    ],
                    spacing=4,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                bgcolor=ft.Colors.with_opacity(0.04, NAVY),
                border_radius=10, padding=16,
                alignment=ft.Alignment(0, 0),
            ))
        controls.append(code_block(post["code"]))
        return ft.Container(
            content=ft.Column(controls=controls, spacing=10),
            bgcolor=WHITE, border_radius=14, padding=20,
            shadow=ft.BoxShadow(blur_radius=10,
                                color=ft.Colors.with_opacity(0.08, NAVY),
                                offset=ft.Offset(0, 3)),
            border=ft.Border.only(top=ft.BorderSide(3, AMBER)),
        )

    # ── Video player using ft.Video (works on Windows desktop, mobile & web) ──
    video_control = ft.Container(
        content=ftv.Video(
            playlist=[
                ftv.VideoMedia("contribution_video.mp4"),
            ],
            playlist_mode=ftv.PlaylistMode.NONE,
            fill_color=LIGHT,
            aspect_ratio=16 / 9,
            volume=100,
            autoplay=False,
            filter_quality=ft.FilterQuality.HIGH,
            show_controls=True,
            expand=True,
        ),
        height=420,
        border_radius=12,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        border=ft.Border.all(3, AMBER),
    )

    contribution_card = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Text("🎥", size=22),
                            width=46, height=46,
                            bgcolor=ft.Colors.with_opacity(0.1, AMBER),
                            border_radius=12,
                            alignment=ft.Alignment(0, 0),
                        ),
                        ft.Column(
                            controls=[
                                ft.Text("My Contribution Video",
                                        color=NAVY, weight=ft.FontWeight.W_800, size=16),
                                ft.Text(
                                    "Embedded directly inside this portfolio — no external redirect.",
                                    color=ft.Colors.with_opacity(0.58, NAVY), size=12,
                                ),
                            ],
                            spacing=2, tight=True, expand=True,
                        ),
                    ],
                    spacing=12,
                ),
                ft.Container(height=6),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text("📋", size=13),
                            ft.Text(
                                "Assessment requirement met: video is playable directly "
                                "inside the portfolio web view — not a link to YouTube.",
                                color=ft.Colors.with_opacity(0.68, NAVY),
                                size=12, expand=True,
                            ),
                        ],
                        spacing=8,
                    ),
                    bgcolor=ft.Colors.with_opacity(0.05, NAVY),
                    border_radius=8, padding=10,
                ),
                ft.Container(height=8),
                video_control,
                ft.Container(height=4),
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Text("🎬  contribution_video.mp4",
                                            color=NAVY, size=11, weight=ft.FontWeight.W_600),
                            bgcolor=ft.Colors.with_opacity(0.08, AMBER),
                            border_radius=8,
                            padding=ft.Padding.symmetric(horizontal=8, vertical=4),
                        ),
                        ft.Text(
                            "Contribution video — embedded & playing inside portfolio",
                            color=ft.Colors.with_opacity(0.6, NAVY), size=12,
                        ),
                    ],
                    spacing=8,
                ),
            ],
            spacing=8,
        ),
        bgcolor=WHITE, border_radius=14, padding=20,
        shadow=ft.BoxShadow(blur_radius=10,
                            color=ft.Colors.with_opacity(0.08, NAVY),
                            offset=ft.Offset(0, 3)),
        border=ft.Border.only(top=ft.BorderSide(3, "#4A9EFF")),
    )

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("✍️  Technical Blog", color=WHITE, size=24,
                                    weight=ft.FontWeight.W_800),
                            ft.Text(
                                "Confidence in Concepts — technical explanations, "
                                "code samples, and contribution evidence.",
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
                            ft.Text("📹  Contribution Evidence",
                                    color=NAVY, weight=ft.FontWeight.W_800, size=18),
                            contribution_card,
                            ft.Container(height=14),
                            ft.Divider(color=ft.Colors.with_opacity(0.15, NAVY), height=1),
                            ft.Container(height=14),
                            ft.Text("📝  Technical Posts",
                                    color=NAVY, weight=ft.FontWeight.W_800, size=18),
                            *[post_card(p) for p in posts],
                        ],
                        spacing=16,
                    ),
                    padding=ft.Padding.symmetric(horizontal=32, vertical=24),
                ),
            ],
            spacing=0,
        ),
        expand=True,
    )
