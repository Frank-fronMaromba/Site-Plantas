import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK

    def change_image(e):
        for elem in options.controls:
            if elem == e.control:
                elem.opacity = 1
                main_image.src = elem.content.src
            else:
                elem.opacity = 0.5

        main_image.update()
        options.update()

    options = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[]
    )

    product_images = ft.Container(
        col={'xs': 12, 'md': 6},
        bgcolor=ft.colors.BLACK87,
        padding=ft.padding.all(30),
        aspect_ratio=9 / 16,
        content=ft.Column(
            controls=[
                main_image := ft.Image(src="https://pin.it/3vxLJ3VJC"),  # Definindo main_image aqui
                options := ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            content=ft.Image(src="https://pin.it/3vxLJ3VJC"),
                            width=80,
                            height=80,
                            opacity=1,
                            on_click=change_image
                        ),
                        ft.Container(
                            content=ft.Image(src="https://pin.it/7KxQ64cR5"),
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_image
                        ),
                        ft.Container(
                            content=ft.Image(src="https://pin.it/32yjNAJEq"),
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_image
                        )
                    ]
                )
            ]
        )
    )

    product_details = ft.Container(
        col={'xs': 12, 'md': 6},
        padding=ft.padding.all(30),
        bgcolor=ft.colors.BLACK87,
        aspect_ratio=9 / 16,
        content=ft.Column(
            controls=[
                ft.Text(
                    value='Plantas',
                    color=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Text(value='Planta de interiores', color=ft.colors.WHITE, weight=ft.FontWeight.BOLD, size=30),
                ft.Text(value='Decoração', color=ft.colors.GREY, italic=True),
                ft.ResponsiveRow(
                    columns=12,
                    controls=[
                        ft.Text(col={'xs': 12, 'sm': 6}, value='R$ 100,20', color=ft.colors.WHITE, size=30),
                        ft.Row(
                            col={'xs': 12, 'sm': 6},
                            controls=[
                                ft.Icon(
                                    name=ft.icons.STAR,
                                    color=ft.colors.AMBER if _ < 4 else ft.colors.RED,
                                ) for _ in range(5)
                            ]
                        )
                    ]
                ),
                ft.Tabs(
                    selected_index=0,
                    height=150,
                    indicator_color=ft.colors.AMBER,
                    label_color=ft.colors.WHITE,
                    unselected_label_color=ft.colors.GREY,
                    tabs=[
                        ft.Tab(
                            text='Descrição',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='Planta ideal para decorar ambientes internos e externos e deixar sua casa mais viva e verde',
                                    color=ft.colors.GREY,
                                )
                            )
                        ),
                        ft.Tab(
                            text='Detalhes',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='Aproximadamente 1,20m, perfeita para cantos de salas, quartos ou escritórios, não precisa de muita água, grandes folhas verdes com textura brilhante, que adicionam um toque natural e sofisticado à decoração do ambiente',
                                    color=ft.colors.GREY,
                                )
                            )
                        )
                    ]
                ),
                ft.ResponsiveRow(
                    columns=12,
                    controls=[
                        ft.Dropdown(
                            col=6,
                            label='Opções de plantas',
                            label_style=ft.TextStyle(color=ft.colors.WHITE, size=16),
                            border_color=ft.colors.GREY,
                            border_width=0.5,
                            options=[
                                ft.dropdown.Option(text='Figueira-Lira'),
                                ft.dropdown.Option(text='Samambaia'),
                                ft.dropdown.Option(text='Rosa do Deserto'),
                            ]
                        ),
                        ft.Dropdown(
                            col=6,
                            label='Quantidade',
                            label_style=ft.TextStyle(color=ft.colors.WHITE, size=16),
                            border_color=ft.colors.GREY,
                            border_width=0.5,
                            options=[
                                ft.dropdown.Option(text='1 unidade'),
                                ft.dropdown.Option(text='3 unidades'),
                                ft.dropdown.Option(text='5 unidades'),
                            ]
                        ),
                        ft.Container(expand=True),
                        ft.ElevatedButton(
                            width=900,
                            text='Adicionar a lista de desejos',
                                style=ft.ButtonStyle(
                                    padding=ft.padding.all(20),
                                    side={
                                        ft.MaterialState.Default: ft.BorderSide(width=2, color=ft.colors.WHITE),
                                    },
                                    bgcolor={
                                        ft.MaterialState.HOVERED: ft.colors.WHITE,
                                    },
                                    color={
                                        ft.MaterialState.Default: ft.colors.WHITE,
                                        ft.MaterialState.HOVERED: ft.colors.BLACK,
                                    }
                            )
                        ),
                        ft.ElevatedButton(
                            width=900,
                            text='Adicionar ao carrinho',
                                style=ft.ButtonStyle(
                                    padding=ft.padding.all(20),
                                    side={
                                        ft.MaterialState.Default: ft.BorderSide(width=2, color=ft.colors.WHITE),
                                    },
                                    bgcolor={
                                        ft.MaterialState.HOVERED: ft.colors.WHITE,
                                    },
                                    color={
                                        ft.MaterialState.Default: ft.colors.WHITE,
                                        ft.MaterialState.HOVERED: ft.colors.BLACK,
                                    }
                            )
                        )
                    ]
                )
            ]
        )
    )

    layout = ft.Container(
        width=900,
        height=200,
        margin=ft.margin.all(30),
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[
                product_images,
                product_details
            ]
        )
    )

    page.add(layout)

if __name__ == "__main__":
    ft.app(target=main)
