import flet as ft

def timeline_page():

    weeks = [
        ("Week 1", "Project planning & system design"),
        ("Week 2", "UI structure development"),
        ("Week 3", "Navigation system implementation"),
        ("Week 4", "Engineering module integration"),
    ]

    cards = []

    for w, d in weeks:
        cards.append(
            ft.Card(
                elevation=2,
                content=ft.Container(
                    padding=20,
                    content=ft.Column(
                        [
                            ft.Text(w, size=18, weight=ft.FontWeight.BOLD),
                            ft.Text(d),
                        ]
                    ),
                ),
            )
        )

    return ft.ListView(
        controls=cards,
        expand=True,
        spacing=10,
        padding=20,
    )