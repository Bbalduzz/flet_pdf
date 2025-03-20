# PDF Viewer for Flet

https://github.com/user-attachments/assets/9b30611e-b8b4-45fa-a8b6-a7a50d9a234d

PdfViewer is a powerful PDF viewer component for Flet applications. It provides a feature-rich interface for displaying and interacting with PDF documents in your Flet applications.

## License Notice
This extension is built upon [syncfusion_flutter_pdfviewer](https://pub.dev/packages/syncfusion_flutter_pdfviewer), a commercial Flutter package by Syncfusion. To use this package in your projects, you must obtain either:
- A Syncfusion® Commercial License, or
- A Free Syncfusion® Community License

Please refer to [Syncfusion's licensing page](https://github.com/syncfusion/flutter-examples/blob/a73a7042c8361ceb2dffb2bcc80e74aaecc9e2d5/LICENSE) for more details about licensing requirements.

## Installation

```bash
pip install flet_pdfviewer
```

## Usage

This pdf viewer supports numerous features, including:
1. Virtual Scrolling - Easily scroll through the pages in the document with a fluent experience. The pages are rendered only when required to increase the loading and scrolling performance.
2. Magnification - The content of the document can be efficiently zoomed in and out.
3. Page Layout and Scroll Options - Layout the pages efficiently in a page by page (single page) scrolling mode or continuous scrolling mode. Also, scroll through pages in both horizontal and vertical direction.
4. Page navigation - Navigate to the desired pages instantly.
5. Text selection - Select text presented in a PDF document.
6. Bookmark navigation - Bookmarks saved in the document are loaded and made ready for easy navigation. This feature helps in navigation within the PDF document of the topics bookmarked already.
7. Document link annotation navigation - Navigate to the desired topic or position by tapping the document link annotation of the topics in the table of contents in a PDF document.
8. Hyperlink navigation - Detects hyperlinks, and tapping on the hyperlink will open the URL in a default web browser.
9. Text markup annotations - Add, remove, and modify text markup annotations in PDF files. The available text markups are highlight, underline, strikethrough and squiggly. This feature will help mark important passages, emphasize specific words or phrases, indicate that certain content should be removed or indicate that text contains possible errors.
10. Form filling - Fill, edit, flatten, save, export, and import AcroForm field data in a PDF document.

more to be implemented ...

Here's a simple example of how to use the FletPdfviewer component:

```python
import flet as ft
from flet_pdfviewer import Pdfviewer

def main(page: ft.Page):
    pdf_viewer = Pdfviewer(
        source="https://example.com/sample.pdf",
        source_type="network",
        show_bookmark=True,
        enable_double_tap_zooming=True
    )
    
    page.add(pdf_viewer)

ft.app(target=main)
```

## Advanced Example

Here's a more comprehensive example that demonstrates various features:

```python
import flet as ft
from flet_pdfviewer import Pdfviewer

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Create PDF viewer with event handling
    def handle_zoom_changed(e):
        print(f"Zoom level changed: {e}")

    pdf_viewer = Pdfviewer(
        source="https://example.com/sample.pdf",
        source_type="network",
        show_bookmark=True,
        enable_double_tap_zooming=True,
        on_zoom_level_changed=handle_zoom_changed,
        password="optional_password",  # If PDF is password-protected
        expand=True
    )

    # Add controls for PDF interaction
    def jump_to_page_3(e):
        pdf_viewer.jump_to_page(3)

    def set_zoom_2x(e):
        pdf_viewer.set_zoom_level(2.0)

    page.add(
        pdf_viewer,
        ft.Row(
            [ft.ElevatedButton("Go to Page 3", on_click=jump_to_page_3),
             ft.ElevatedButton("Zoom 2x", on_click=set_zoom_2x)]
        )
    )

ft.app(target=main)
```

## API Reference

### Constructor Parameters

- `source` (Optional[str]): The source of the PDF document. Can be a URL, file path, or asset path.
- `source_type` (Optional[str]): Type of the source. Can be "network", "file", or "asset". Default is "network".
- `show_bookmark` (Optional[bool]): Whether to show the bookmark panel. Default is True.
- `memory_bytes` (Optional[str]): PDF data as bytes in memory.
- `password` (Optional[str]): Password for protected PDF documents.
- `enable_double_tap_zooming` (Optional[bool]): Enable zooming with double tap. Default is True.
- `on_zoom_level_changed` (Optional[Callable]): Callback function for zoom level changes.

### Standard Control Properties

- `width` (OptionalNumber): Control width.
- `height` (OptionalNumber): Control height.
- `expand` (Optional[bool]): Whether the control should expand to fill available space.
- `opacity` (OptionalNumber): Control opacity.
- `tooltip` (Optional[str]): Tooltip text.
- `visible` (Optional[bool]): Control visibility.

### Properties

- `source`: Get or set the PDF source.
- `source_type`: Get or set the source type ("network", "file", "asset").
- `show_bookmark`: Get or set bookmark panel visibility.
- `memory_bytes`: Get or set PDF data in memory.
- `password`: Get or set PDF password.
- `enable_double_tap_zooming`: Get or set double tap zooming.

### Methods

- `open_bookmark_view()`: Opens the bookmark view.
- `jump_to_page(page_number: int)`: Jumps to the specified page number.
- `set_zoom_level(zoom_level: float)`: Sets the zoom level (between 1.0 and 3.0).
- `get_current_page() -> int`: Gets the current page number (async).
- `get_current_zoom_level() -> float`: Gets the current zoom level (async).
- `get_total_pages() -> int`: Gets the total number of pages (async).

### Events

- `on_zoom_level_changed`: Triggered when zoom level changes.

## Notes

- For network PDFs, ensure the URL is accessible and the PDF is not blocked by CORS policies.
- Password-protected PDFs require the correct password to be set before viewing.
- Zoom levels are typically constrained between 1.0 and 3.0.
- Async methods should be awaited when called.


