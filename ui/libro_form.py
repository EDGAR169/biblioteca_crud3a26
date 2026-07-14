import flet as ft

def libro_form():

    titulo_input = ft.TextField(
        label = "Titulo del libro:",
        widht = 400
    )

    autor_input = ft.TextField(
        label = "Autor del libro:",
        widht = 400
    )

    isbn_input = ft.TextField(
        label = "ISBN",
        width = 400
    )

    mensaje = ft.Text(
        "",
        color = ft.Colors.GREEN
    )

    return ft.container(
        paddel = 30,
        content = ft.column(
            controls = [
                ft.Text (
                    "Registrar nuevo libro",
                    size = 24,
                    weight = ft.FontWeight.BOLD
                ),
                ft.Text(
                    "Capture los datos basicos del libro",
                    size = 14,
                    color = ft.Colors.BLUE_GREY_600
                ),
                Titulo_input,
                autor,input,
                isb_input,
                
                ft.ElevatedButton(
                    "Registrar libro",
                    icon = ft.Icons.SAVE
                )
            ],

            spacing = 15
        )
    )
    
