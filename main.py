import flet as ft

from pages.home import home_page
from pages.timeline import timeline_page
from pages.matlab import matlab_page
from pages.blog import blog_page
from pages.github import github_page


def main(page: ft.Page):
    page.title = "Engineering Portfolio"
    page.theme_mode = ft.ThemeMode.LIGHT

    page.padding = 30
    page.bgcolor = "#f5f7fb"   
    page.assets_dir = "assets"

    # Fonts (clean version)
    page.fonts = {
        "Poppins": "https://raw.githubusercontent.com/google/fonts/main/ofl/poppins/Poppins-Regular.ttf"
    }

    page.theme = ft.Theme(font_family="Poppins")

    content = ft.Container(expand=True, content=home_page())

    def change_page(e):
        pages = [
            home_page(),
            timeline_page(),
            matlab_page(),
            blog_page(),
            github_page(),
        ]
        content.content = pages[e.control.selected_index]
        page.update()

    nav = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationRailDestination(icon=ft.Icons.TIMELINE, label="Timeline"),
            ft.NavigationRailDestination(icon=ft.Icons.SCHOOL, label="MATLAB"),
            ft.NavigationRailDestination(icon=ft.Icons.BOOK, label="Blog"),
            ft.NavigationRailDestination(icon=ft.Icons.CODE, label="GitHub"),
        ],
        on_change=change_page,
    )

    page.add(
        ft.Row(
            [
                nav,
                ft.VerticalDivider(width=1),
                content,
            ],
            expand=True,
        )
    )


ft.app(target=main)