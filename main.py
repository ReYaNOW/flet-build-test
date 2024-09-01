from flet import *
import httpx
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


def main(page: Page):
    user = User(name='name', age='13')
    page.theme_mode = ThemeMode.LIGHT
    r = httpx.get('https://www.google.com/')
    page.appbar = AppBar(title=Text(f'{r.url}', color="white"), bgcolor="blue")
    page.add(
        Column(
            [
                Text(f'{r.status_code}'),
                ElevatedButton(
                    f'{user.name}, {user.age}', bgcolor="blue", color="white"
                ),
            ]
        )
    )


app(main)
