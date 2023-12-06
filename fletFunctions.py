import flet as ft
from flet import *
from apiFunctions import profile_info, get_account, find_name


# Function for the start page of the app


def start_page(page):
    page.clean()
    page.window_width = 400
    page.bgcolor = '#111211'

    # Function to show summoner profile
    def show_summ_profile(e):
        page.update()
        name = txt_name.value
        page.clean()
        username = find_name(name)
        acc = get_account(username[0], regiondd.value, username[1])

        # Function call that prints the profile stats
        print_player_info(acc['puuid'], page, regiondd.value)
        page.add(ft.ElevatedButton("Back", on_click=back, bgcolor=ft.colors.WHITE, color=colors.BLACK))

    # Function that goes back to start page
    def back(e):
        start_page(page)

    txt_name = ft.TextField(
        label="Summoner#xxxx",
        bgcolor=colors.WHITE,
        width=267)

    regiondd = ft.Dropdown(
        width=100,
        label='>',
        options=[
            ft.dropdown.Option("NA1"),
            ft.dropdown.Option("EUW1"),
            ft.dropdown.Option("EUN1"),
            ft.dropdown.Option("KR"),
            ft.dropdown.Option("BR1"),
        ]
    )

    dd = ft.Container(
        content=regiondd,
        bgcolor=colors.WHITE
    )
    search_bar = ft.Row(spacing=0, controls=[dd, txt_name])

    page.add(search_bar,
             ft.ElevatedButton("Search", on_click=show_summ_profile, bgcolor=ft.colors.WHITE, color=colors.BLACK)
             )


# Function that prints player info


def print_player_info(pid, page, region):
    page.add(ft.Text(profile_info(pid, region)['name'], color=colors.WHITE))
    page.add(ft.Text(profile_info(pid, region)['summonerLevel'], color=colors.WHITE))
    page.add(ft.Text(profile_info(pid, region)['id'], color=colors.WHITE))
    page.add(ft.Text(profile_info(pid, region)['profileIconId'], color=colors.WHITE))
