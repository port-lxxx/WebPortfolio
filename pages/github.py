import flet as ft

def github_page():

    return ft.ListView(
        expand=True,
        padding=30,
        spacing=20,
        controls=[

            ft.Text(
                "GitHub Evidence",
                size=32,
                weight=ft.FontWeight.BOLD,
            ),

            ft.Text(
                "Verified contribution history to the group project repository.",
                size=16,
                color="grey",
            ),

            # COMMIT HISTORY
            ft.Container(
                bgcolor="#f5f5f7",
                border_radius=20,
                padding=20,
                content=ft.Column(
                    [
                        ft.Text(
                            "Commit History",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                        ),

                        ft.Image(
                            src="github/commits.png",
                            height=350,
                        ),

                        ft.Text(
                            "Record of commits made to the main project repository."
                        ),
                    ]
                ),
            ),

            # CODE REVIEWS / CONTRIBUTIONS
            ft.Container(
                bgcolor="#f5f5f7",
                border_radius=20,
                padding=20,
                content=ft.Column(
                    [
                        ft.Text(
                            "Code Reviews / Contributions",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                        ),

                        ft.Image(
                            src="github/reviews.png",
                            height=350,
                        ),

                        ft.Text(
                            "Evidence of participation in code reviews and collaboration on improvements."
                        ),
                    ]
                ),
            ),

            # IMPACT SUMMARY (NOW REALISTIC)
            ft.Container(
                bgcolor="#f5f5f7",
                border_radius=20,
                padding=20,
                content=ft.Column(
                    [
                        ft.Text(
                            "Impact Summary",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                        ),

                        ft.Text(
                            "My contribution focused on improving the usability and structure of the application interface. "
                            "I participated in reviewing team code, identifying UI inconsistencies, and suggesting improvements "
                            "to navigation and layout. This helped ensure a more stable and user-friendly final system."
                        ),
                    ]
                ),
            ),
        ],
    )