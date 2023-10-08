import flet as ft


def main(page: ft.Page):
    page.window_maximized = True
    page.gradient = ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.Alignment(0.8, 1),
            colors=[

            ],

        )
    page.title = "Flet App"
    page.bgcolor = "#4A4A4A"

    card_row_1 = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.TextField(label="window" , width=380, height=80, ),
        ]
    )
    card_row_2 = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.ElevatedButton(text='AC', width=80, height=80, color='#FFFFFF', bgcolor='#AEAEAE'),
            ft.ElevatedButton(text='+/-', width=80, height=80, color='#FFFFFF', bgcolor='#AEAEAE'),
            ft.ElevatedButton(text='%', width=80, height=80, color='#FFFFFF', bgcolor='#AEAEAE'),
            ft.ElevatedButton(text='÷', width=80, height=80, color='#FFFFFF',  bgcolor='#FFB800'),

        ]
    )
    card_row_3 = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.ElevatedButton(text='1', width=80, height=80, color='#FFFFFF', bgcolor='#6D6D6D'),
            ft.ElevatedButton(text='2', width=80, height=80, color='#FFFFFF', bgcolor='#6D6D6D'),
            ft.ElevatedButton(text='3', width=80, height=80, color='#FFFFFF', bgcolor='#6D6D6D'),
            ft.ElevatedButton(text='X', width=80, height=80, color='#FFFFFF', bgcolor='#FFB800'),

        ]
    )
    card_row_4 = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.ElevatedButton(text='4', width=80, height=80, color='#FFFFFF', bgcolor='#6D6D6D'),
            ft.ElevatedButton(text='5', width=80, height=80, color='#FFFFFF', bgcolor='#6D6D6D'),
            ft.ElevatedButton(text='6', width=80, height=80, color='#FFFFFF', bgcolor='#6D6D6D'),
            ft.ElevatedButton(text='-', width=80, height=80, color='#FFFFFF', bgcolor='#FFB800'),

        ]
    )
    card_row_8 = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.ElevatedButton(text='7', width=80, height=80, color='#FFFFFF', bgcolor='#6D6D6D'),
            ft.ElevatedButton(text='8', width=80, height=80, color='#FFFFFF', bgcolor='#6D6D6D'),
            ft.ElevatedButton(text='9', width=80, height=80, color='#FFFFFF', bgcolor='#6D6D6D'),
            ft.ElevatedButton(text='+', width=80, height=80, color='#FFFFFF', bgcolor='#FFB800'),

        ]
    )
    card_row_9 = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.ElevatedButton(text='0', width=167, height=80, color='#FFFFFF', bgcolor='#6D6D6D'),
            ft.ElevatedButton(text='.', width=80, height=80, color='#FFFFFF', bgcolor='#6D6D6D'),
            ft.ElevatedButton(text='=', width=80, height=80, color='#FFFFFF', bgcolor='#FFB800'),


        ]
    )
    card_column_1 = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            card_row_1,
            card_row_2,
            card_row_3,
            card_row_4,
            card_row_8,
            card_row_9,
        ]
    )
    card = ft.Card(card_column_1, width=400, height=700, color='#4A4A4A')
    row = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            card,

        ]
    )
    container = ft.Container(
        row,
        expand=True,
        alignment=ft.alignment.center,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[
                "0xffFF3A3A",
                "0xffE44040",
            ],
            tile_mode=ft.GradientTileMode.MIRROR,
        ),
    )

    page.add(container)
    page.update()


ft.app(target=main)