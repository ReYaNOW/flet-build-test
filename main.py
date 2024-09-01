from flet import *
import httpx


def main(page: Page):
    page.theme_mode = ThemeMode.LIGHT
    r = httpx.get('https://www.google.com/')
    page.appbar = AppBar(
        title=Text(f'{r.url}', color="white"), bgcolor="blue"
    )
    page.add(
        Column(
            [
                Text(f'{r.status_code}'),
                ElevatedButton("test123", bgcolor="blue", color="white"),
            ]
        )
    )


app(main)
