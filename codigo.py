import flet as ft
def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK

    product_images = ft.Container(
        content=ft.Column(
            controls=[
                ft.Image(
                    src='https://pin.it/56PMX2tgo',
                )
            ]    
        )
    )

    product_details = ft.Container()

    layout = ft.Container(
        width=900,
        height=200,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.CYAN),
        content==ft.ResponsiveRow(
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