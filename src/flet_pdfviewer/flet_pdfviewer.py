from typing import Any, Optional, Union, Callable

from flet.core.constrained_control import ConstrainedControl
from flet.core.control import OptionalNumber


class PdfViewer(ConstrainedControl):
    def __init__(
        self,
        source: Optional[str] = None,
        source_type: Optional[str] = "network",
        is_network: Optional[bool] = None,  # For backward compatibility
        show_bookmark: Optional[bool] = True,
        memory_bytes: Optional[str] = None,
        password: Optional[str] = None,
        enable_double_tap_zooming: Optional[bool] = True,
        on_zoom_level_changed: Optional[Callable] = None,
        
        # ConstrainedControl properties
        ref=None,
        width: OptionalNumber = None,
        height: OptionalNumber = None,
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        expand: Optional[bool] = None,
        opacity: OptionalNumber = None,
        tooltip: Optional[str] = None,
        visible: Optional[bool] = None,
        data: Any = None,
    ):
        ConstrainedControl.__init__(
            self,
            ref=ref,
            width=width,
            height=height,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
            expand=expand,
            opacity=opacity,
            tooltip=tooltip,
            visible=visible,
            data=data,
        )

        self.source = source
        
        # Handle backward compatibility with is_network
        if is_network is not None:
            self.source_type = "network" if is_network else "file"
        else:
            self.source_type = source_type
            
        self.show_bookmark = show_bookmark
        self.memory_bytes = memory_bytes
        self.password = password
        self.enable_double_tap_zooming = enable_double_tap_zooming
        self.on_zoom_level_changed = on_zoom_level_changed

    def _get_control_name(self):
        return "flet_pdfviewer"

    # Event handlers
    def _handle_event(self, e):
        if e.name == "zoom_level_changed" and self.on_zoom_level_changed is not None:
            event_data = e.data
            self.on_zoom_level_changed(event_data)
        super()._handle_event(e)

    # Properties
    
    # source
    @property
    def source(self) -> Optional[str]:
        return self._get_attr("source")

    @source.setter
    def source(self, value: Optional[str]):
        self._set_attr("source", value)
    
    # source_type
    @property
    def source_type(self) -> Optional[str]:
        return self._get_attr("sourceType")

    @source_type.setter
    def source_type(self, value: Optional[str]):
        self._set_attr("sourceType", value)
    
    # is_network (for backward compatibility)
    @property
    def is_network(self) -> Optional[bool]:
        return self.source_type == "network"

    @is_network.setter
    def is_network(self, value: Optional[bool]):
        self.source_type = "network" if value else "file"
    
    # show_bookmark
    @property
    def show_bookmark(self) -> Optional[bool]:
        return self._get_attr("showBookmark", data_type="bool", def_value=True)

    @show_bookmark.setter
    def show_bookmark(self, value: Optional[bool]):
        self._set_attr("showBookmark", value)
    
    # memory_bytes
    @property
    def memory_bytes(self) -> Optional[str]:
        return self._get_attr("memoryBytes")

    @memory_bytes.setter
    def memory_bytes(self, value: Optional[str]):
        self._set_attr("memoryBytes", value)
    
    # password
    @property
    def password(self) -> Optional[str]:
        return self._get_attr("password")

    @password.setter
    def password(self, value: Optional[str]):
        self._set_attr("password", value)
    
    # enable_double_tap_zooming
    @property
    def enable_double_tap_zooming(self) -> Optional[bool]:
        return self._get_attr("enableDoubleTapZooming", data_type="bool", def_value=True)

    @enable_double_tap_zooming.setter
    def enable_double_tap_zooming(self, value: Optional[bool]):
        self._set_attr("enableDoubleTapZooming", value)
    
    # Methods
    def open_bookmark_view(self):
        """Opens the bookmark view in the PDF viewer."""
        self.invoke_method("openBookmarkView")
    
    def jump_to_page(self, page_number: int):
        """Jumps to the specified page number in the PDF document."""
        self.invoke_method("jumpToPage", {"pageNumber": str(page_number)})
    
    def set_zoom_level(self, zoom_level: float):
        """Sets the zoom level of the PDF document (between 1.0 and 3.0)."""
        self.invoke_method("setZoomLevel", {"zoomLevel": str(zoom_level)})
    
    async def get_current_page(self) -> int:
        """Gets the current page number of the PDF document."""
        result = await self.invoke_method_async("getCurrentPage")
        return int(result) if result else 1
    
    async def get_current_zoom_level(self) -> float:
        """Gets the current zoom level of the PDF document."""
        result = await self.invoke_method_async("getCurrentZoomLevel")
        return float(result) if result else 1.0
    
    async def get_total_pages(self) -> int:
        """Gets the total number of pages in the PDF document."""
        result = await self.invoke_method_async("getTotalPages")
        return int(result) if result else 0