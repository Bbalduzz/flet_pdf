# FletPdfviewer

FletPdfviewer is a powerful PDF viewer component for Flet applications. It provides a feature-rich interface for displaying and interacting with PDF documents in your Flet applications.

## Installation

```bash
pip install flet_pdfviewer
```

## Basic Usage

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


