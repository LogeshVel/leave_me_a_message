import flet as ft
import telegram_bot


def main(page: ft.Page):
    page.title = "Contact Logesh"
    page.theme_mode = ft.ThemeMode.LIGHT
    main_appbar = ft.AppBar(
        title=ft.Text("Leave me a message", style=ft.TextThemeStyle.TITLE_LARGE),
        center_title=True,
        bgcolor=ft.colors.BLUE_GREY_50,
    )
    page.appbar = main_appbar
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def get_textfield(label_str, is_email=False):
        text_cap = ft.TextCapitalization.SENTENCES
        if is_email:
            text_cap = ft.TextCapitalization.NONE
        return ft.TextField(label=label_str, border=ft.InputBorder.NONE, filled=True, cursor_color=ft.colors.BLACK38,
                             label_style=ft.TextStyle(color=ft.colors.BLACK38), capitalization=text_cap)
  
    name_text = get_textfield("Your Name")
    mail_text = get_textfield("Email id", True)
    msg_text = get_textfield("Your Message/Query")

    def button_clicked(e):
        is_null = False
        if name_text.value == "":
            is_null = True
            name_text.error_text = "Please enter your name"
        if msg_text.value == "":
            is_null = True
            msg_text.error_text = "Please enter some message :("
        if mail_text.value == "":
            is_null = True
            mail_text.error_text = "Please enter your email id"
        page.update()

        if not is_null:
            # send msg
            telegram_bot.send_msg(f"{name_text.value}\n{mail_text.value}\n\n{msg_text.value}")
            name_text.value = ""
            msg_text.value = ""
            mail_text.value = ""
            name_text.error_text = None
            msg_text.error_text = None
            mail_text.error_text = None
            page.views.append(
                ft.View(
                    "/done",
                    [
                        ft.AppBar(title=ft.Text("Message Sent", style=ft.TextThemeStyle.TITLE_LARGE),
                                  bgcolor=ft.colors.SURFACE_VARIANT, center_title=True, ),
                        ft.Text("Thanks for leaving a message :)", style=ft.TextThemeStyle.DISPLAY_SMALL),
                        ft.Text("Will be in touch soon...", style=ft.TextThemeStyle.TITLE_MEDIUM),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER
                )
            )

            page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_view_pop = view_pop

    b = ft.ElevatedButton(text="Submit", on_click=button_clicked, color=ft.colors.BLACK, style=ft.ButtonStyle(
        color=ft.colors.BLACK,
        overlay_color=ft.colors.BLUE_GREY_50
    ))
    row = ft.Row(
        controls=[b],
        alignment=ft.MainAxisAlignment.CENTER
    )
    col1 = ft.Column(
        controls=[name_text, mail_text, msg_text, row],
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
    )
    con1 = ft.Container(
        content=col1,
        alignment=ft.alignment.center,
        padding=10,
        width=500,
        height=350,
        border_radius=10,
        ink=True,
        bgcolor=ft.colors.WHITE54
    )

    page.add(con1)


ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER)
