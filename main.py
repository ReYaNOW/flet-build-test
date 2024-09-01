import flet as fp


def main(page: fp.Page):
    page.theme_mode = fp.ThemeMode.LIGHT
    page.appbar = fp.AppBar(
        title=fp.Text("hello youtube", color="white"), bgcolor="blue"
    )
    page.add(
        fp.Column(
            [
                fp.Text("hello"),
                fp.ElevatedButton("test123", bgcolor="blue", color="white"),
            ]
        )
    )


fp.app(main)
