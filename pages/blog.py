import flet as ft

def blog_page():

    def article(title, body, formula):
        return ft.Card(
            elevation=2,
            content=ft.Container(
                padding=20,
                content=ft.Column(
                    [
                        ft.Text(title, size=18, weight=ft.FontWeight.BOLD),
                        ft.Text(body),
                        ft.Text(formula, size=16, weight=ft.FontWeight.W_500),
                    ]
                ),
            ),
        )

    return ft.ListView(
        controls=[

            article(
                "Iron Ore Processing in Namibia",
                "Namibia has significant mineral resources, including iron ore deposits. "
                "In metallurgical engineering, ore beneficiation is used to increase iron concentration "
                "before smelting, improving efficiency and reducing waste.",
                "Fe₂O₃ + CO → Fe + CO₂"
            ),

            article(
                "Gold Extraction via Cyanidation",
                "In metallurgical processes, gold is commonly extracted using cyanide leaching. "
                "This process is widely used in Southern Africa, including gold recovery operations.",
                "4Au + 8CN⁻ + O₂ + 2H₂O → 4[Au(CN)₂]⁻ + 4OH⁻"
            ),

            article(
                "Copper Refining and Electrolysis",
                "Copper refining is essential for electrical applications. In electrorefining, impure copper "
                "is purified to produce high-grade copper used in electrical wiring and electronics.",
                "Cu²⁺ + 2e⁻ → Cu (pure metal deposition)"
            ),

            article(
                "Mining Waste and Tailings Management in Namibia",
                "Namibia’s mining sector generates tailings that must be managed to reduce environmental impact. "
                "Metallurgical engineering focuses on waste reduction, water recycling, and safe storage systems.",
                "Recovery Efficiency = (Recovered Metal / Total Metal in Ore) × 100%"
            ),

        ],
        expand=True,
        spacing=10,
        padding=20,
    )