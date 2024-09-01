import flet as fp
import httpx


def main(page: fp.Page):
    page.theme_mode = fp.ThemeMode.LIGHT
    r = httpx.get('https://www.google.com/')
    page.appbar = fp.AppBar(
        title=fp.Text(f'{r.url}{r.status_code}', color='white'), bgcolor='blue'
    )
    page.add(
        fp.Column(
            [
                fp.Text(f'{r.url}{r.status_code}'),
                fp.ElevatedButton('test123', bgcolor='blue', color='white'),
            ]
        )
    )


fp.app(main)
