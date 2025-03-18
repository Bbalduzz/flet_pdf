import 'dart:io';
import 'dart:typed_data';
import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'package:syncfusion_flutter_pdfviewer/pdfviewer.dart';

class FletPdfviewerControl extends StatefulWidget {
  final Control? parent;
  final Control control;
  final List<Control> children;
  final FletControlBackend backend;

  const FletPdfviewerControl({
    Key? key,
    required this.parent,
    required this.control,
    required this.children,
    required this.backend,
  }) : super(key: key);

  @override
  State<FletPdfviewerControl> createState() => _FletPdfviewerControlState();
}

class _FletPdfviewerControlState extends State<FletPdfviewerControl> {
  final GlobalKey<SfPdfViewerState> _pdfViewerKey = GlobalKey();
  final PdfViewerController _pdfViewerController = PdfViewerController();

  @override
  void initState() {
    super.initState();
    
    // Subscribe to methods
    widget.backend.subscribeMethods(
      widget.control.id,
      _handleMethodCall
    );
  }

  @override
  void dispose() {
    // Unsubscribe from methods
    widget.backend.unsubscribeMethods(widget.control.id);
    super.dispose();
  }
  
  // Method handler
  Future<String?> _handleMethodCall(String methodName, Map<String, String> args) async {
    switch (methodName) {
      case "openBookmarkView":
        _pdfViewerKey.currentState?.openBookmarkView();
        break;
      case "jumpToPage":
        final pageNumber = int.tryParse(args["pageNumber"] ?? "") ?? 1;
        _pdfViewerController.jumpToPage(pageNumber);
        break;
      case "setZoomLevel":
        final zoomLevel = double.tryParse(args["zoomLevel"] ?? "") ?? 1.0;
        _pdfViewerController.zoomLevel = zoomLevel;
        break;
      case "getCurrentPage":
        return _pdfViewerController.pageNumber.toString();
      case "getCurrentZoomLevel":
        return _pdfViewerController.zoomLevel.toString();
      case "getTotalPages":
        return _pdfViewerController.pageCount.toString();
    }
    return null;
  }

  void _handleZoomLevelChanged(PdfZoomDetails details) {
    widget.backend.triggerControlEvent(
      widget.control.id,
      "zoom_level_changed",
      '{"oldZoomLevel": ${details.oldZoomLevel}, "newZoomLevel": ${details.newZoomLevel}}',
    );
  }

  @override
  Widget build(BuildContext context) {
    // Get properties from the control
    final source = widget.control.attrString("source", "");
    final sourceType = widget.control.attrString("sourceType", "network");
    final showBookmark = widget.control.attrBool("showBookmark", true);
    final password = widget.control.attrString("password", "");
    final enableDoubleTapZooming = widget.control.attrBool("enableDoubleTapZooming", true);
    
    // Get memory bytes if provided
    Uint8List? memoryBytes;
    if (sourceType == "memory") {
      final bytesStr = widget.control.attrString("memoryBytes", "");
      if (bytesStr!.isNotEmpty) {
        try {
          memoryBytes = Uint8List.fromList(bytesStr.codeUnits);
        } catch (e) {
          print("Error converting memory bytes: $e");
        }
      }
    }

    Widget pdfViewer;
    
    if (source!.isEmpty && sourceType != "memory") {
      pdfViewer = const Center(
        child: Text("Please specify a PDF source"),
      );
    } else if (sourceType == "network") {
      pdfViewer = SfPdfViewer.network(
        source,
        key: _pdfViewerKey,
        controller: _pdfViewerController,
        password: password!.isNotEmpty ? password : null,
        enableDoubleTapZooming: enableDoubleTapZooming ?? true,
        onZoomLevelChanged: _handleZoomLevelChanged,
      );
    } else if (sourceType == "asset") {
      pdfViewer = SfPdfViewer.asset(
        source,
        key: _pdfViewerKey,
        controller: _pdfViewerController,
        password: password!.isNotEmpty ? password : null,
        enableDoubleTapZooming: enableDoubleTapZooming ?? true,
        onZoomLevelChanged: _handleZoomLevelChanged,
      );
    } else if (sourceType == "file") {
      pdfViewer = SfPdfViewer.file(
        File(source),
        key: _pdfViewerKey,
        controller: _pdfViewerController,
        password: password!.isNotEmpty ? password : null,
        enableDoubleTapZooming: enableDoubleTapZooming ?? true,
        onZoomLevelChanged: _handleZoomLevelChanged,
      );
    } else if (sourceType == "memory" && memoryBytes != null) {
      pdfViewer = SfPdfViewer.memory(
        memoryBytes,
        key: _pdfViewerKey,
        controller: _pdfViewerController,
        password: password!.isNotEmpty ? password : null,
        enableDoubleTapZooming: enableDoubleTapZooming ?? true,
        onZoomLevelChanged: _handleZoomLevelChanged,
      );
    } else {
      pdfViewer = const Center(
        child: Text("Invalid source type or missing data"),
      );
    }

    // Return the PDF viewer directly without Scaffold
    return constrainedControl(context, pdfViewer, widget.parent, widget.control);
  }
}