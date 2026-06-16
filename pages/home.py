import flet as ft

def home_page():

    return ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[

            # PROFILE IMAGE
            ft.Container(
                content=ft.CircleAvatar(
                    foreground_image_src="profile/profile.jpg",
                    radius=60,
                ),
                margin=20,
            ),

            # NAME
            ft.Text(
                "Saima Tangi Iileka",
                size=34,
                weight=ft.FontWeight.W_600,
            ),

            ft.Text(
                "BSc in Metallurgical Engineering Student",
                size=16,
                color="grey",
            ),

            ft.Container(height=20),

            # DESCRIPTION CARD
            ft.Container(
                width=600,
                padding=20,
                border_radius=20,
                bgcolor="#f5f5f7",
                content=ft.Text(
                    "Engineering portfolio showcasing my project timeline, MATLAB certifications, "
                    "technical blog in metallurgical engineering, and GitHub development evidence.",
                    size=14,
                ),
            ),
        ],
    )