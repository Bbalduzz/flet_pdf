import flet as ft
from flet_pdfviewer import PdfViewer


def main(page: ft.Page):
    page.title = "Flet PDF Viewer"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    
    # Define function before using it
    def pick_files_result(e: ft.FilePickerResultEvent):
        if e.files:
            pdf_viewer.source = e.files[0].path
            pdf_viewer.source_type = "file"
            page.update()
    
    async def update_pdf_info():
        try:
            current_page = await pdf_viewer.get_current_page()
            total_pages = await pdf_viewer.get_total_pages()
            zoom_level = await pdf_viewer.get_current_zoom_level()
            
            page_info.value = f"Page {current_page} of {total_pages}"
            zoom_info.value = f"Zoom: {zoom_level:.1f}x"
            page_input.hint_text = str(current_page)
            page.update()
        except Exception as e:
            print(f"Error updating PDF info: {e}")
    
    def handle_zoom_changed(e):
        data = eval(e)  # Convert string to dict
        zoom_info.value = f"Zoom: {data['newZoomLevel']:.1f}x"
        page.update()
    
    pdf_viewer = PdfViewer(
        source="https://cdn.syncfusion.com/content/PDFViewer/flutter-succinctly.pdf",
        source_type="network",
        show_bookmark=True,
        enable_double_tap_zooming=True,
        on_zoom_level_changed=handle_zoom_changed,
        expand=True,
    )

    file_picker = ft.FilePicker(on_result=pick_files_result)
    page.overlay.append(file_picker)
    
    def change_document(e):
        if source_field.value:
            pdf_viewer.source = source_field.value
            pdf_viewer.source_type = source_type_dropdown.value
            if password_field.value:
                pdf_viewer.password = password_field.value
            page.update()
            page.run_async(update_pdf_info())
    
    source_field = ft.TextField(
        label="PDF Source",
        value="https://cdn.syncfusion.com/content/PDFViewer/flutter-succinctly.pdf",
        expand=True,
    )
    
    source_type_dropdown = ft.Dropdown(
        width=120,
        options=[
            ft.dropdown.Option("network", "Network"),
            ft.dropdown.Option("file", "File"),
            ft.dropdown.Option("asset", "Asset"),
        ],
        value="network",
    )
    
    password_field = ft.TextField(
        label="Password",
        password=True,
        width=120,
    )
    
    # PDF navigation controls
    page_info = ft.Text(f"Page 1 of 1", weight=ft.FontWeight.BOLD)
    zoom_info = ft.Text("Zoom: 1.0x", weight=ft.FontWeight.BOLD)
    
    page_input = ft.TextField(
        label="Go to page",
        width=100,
        hint_text="1",
        keyboard_type=ft.KeyboardType.NUMBER,
    )
    
    def jump_to_page(e):
        try:
            page_num = int(page_input.value)
            pdf_viewer.jump_to_page(page_num)
            page.run_task(update_pdf_info())
        except ValueError:
            pass
    
    def set_zoom(level):
        def handle_zoom(e):
            pdf_viewer.set_zoom_level(level)
            page.run_task(update_pdf_info())
        return handle_zoom
    
    def open_bookmarks(e):
        pdf_viewer.open_bookmark_view()
    
    page.add(
        ft.Column([
            ft.Text("PDF Viewer", size=28, weight=ft.FontWeight.BOLD),
            ft.Container(height=10),
            
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Row([
                            source_field,
                            source_type_dropdown,
                            password_field,
                        ], spacing=10),
                        
                        ft.Row([
                            ft.ElevatedButton(
                                "Load PDF",
                                icon=ft.icons.CLOUD_DOWNLOAD,
                                on_click=change_document,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=8),
                                ),
                            ),
                            ft.ElevatedButton(
                                "Browse Files",
                                icon=ft.icons.FOLDER_OPEN,
                                on_click=lambda _: file_picker.pick_files(
                                    allowed_extensions=["pdf"]
                                ),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=8),
                                ),
                            ),
                        ], alignment=ft.MainAxisAlignment.END, spacing=10),
                    ]),
                    padding=15,
                ),
                elevation=2,
            ),
            
            ft.Container(height=10),
            
            # PDF controls
            ft.Card(
                content=ft.Container(
                    content=ft.Row([
                        # Page navigation
                        ft.Row([
                            page_info,
                            page_input,
                            ft.IconButton(
                                icon=ft.icons.ARROW_FORWARD,
                                tooltip="Go to page",
                                on_click=jump_to_page,
                            ),
                        ], spacing=10),
                        
                        # Zoom controls
                        ft.Row([
                            zoom_info,
                            ft.IconButton(
                                icon=ft.icons.ZOOM_OUT,
                                tooltip="Zoom out",
                                on_click=set_zoom(1.0),
                            ),
                            ft.IconButton(
                                icon=ft.icons.ZOOM_IN,
                                tooltip="Zoom in",
                                on_click=set_zoom(2.0),
                            ),
                            ft.IconButton(
                                icon=ft.icons.BOOKMARK,
                                tooltip="Bookmarks",
                                on_click=open_bookmarks,
                            ),
                        ], spacing=10),
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    padding=10,
                ),
                elevation=2,
            ),
            
            ft.Container(height=10),
            pdf_viewer,
        ], expand=True)
    )
    
    # Initialize PDF info
    page.on_load = lambda _: page.run_task(update_pdf_info())


ft.app(target=main)