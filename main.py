import flet as ft
from flet import *
from fletFunctions import start_page

txt_name = ft.TextField(
    label="Summoner#xxxx",
    bgcolor=colors.WHITE,
    width=267)


regiondd = ft.Dropdown(
    width=100,
    options=[
        ft.dropdown.Option("NA1"),
        ft.dropdown.Option("EUW1"),
        ft.dropdown.Option("EUN1"),
        ft.dropdown.Option("KR"),
        ft.dropdown.Option("BR1"),
    ],
)
dd = ft.Container(
    content=regiondd,
    bgcolor=colors.WHITE
)


def main(page: Page):
    start_page(page)


ft.app(target=main)
