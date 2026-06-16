import flet as ft

def certificate_card(title, image_path):
    return ft.Container(
        width=350,
        bgcolor="#f5f5f7",
        border_radius=20,
        padding=15,
        content=ft.Column(
            [
                ft.Text(
                    title,
                    size=18,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Image(
                    src=image_path,
                    height=220,
                ),
            ],
            spacing=10,
        ),
    )


def matlab_page():

    certificates = [
        ("MATLAB Onramp", "certificates/matlab_onramp.png"),
        ("Simulink Onramp", "certificates/simulink_onramp.png"),
        ("Machine Learning Onramp", "certificates/machine_learning_onramp.png"),
        ("Calculations with Vectors and Matrices", "certificates/calculations_with_vectors_and_matrices.png"),
        ("Explore Data with MATLAB Plots", "certificates/explore_data_with_matlab_plots.png"),
        ("Make and Manipulate Matrices", "certificates/make_and_manipulate_matrices.png"),
        ("Signal Segmentation with Deep Learning", "certificates/signal_segmentation_with_deep_learning.png"),
    ]

    cards = [certificate_card(title, image) for title, image in certificates]

    return ft.ListView(
        expand=True,
        padding=30,
        spacing=20,
        controls=[

            ft.Text(
                "MATLAB Achievement Hub",
                size=32,
                weight=ft.FontWeight.BOLD,
            ),

            ft.Text(
                "MathWorks Learning Center Certificates",
                size=16,
                color="grey",
            ),
            ft.Row(
                wrap=True,
                spacing=20,
                run_spacing=20,
                controls=cards,
),
        ]
    )