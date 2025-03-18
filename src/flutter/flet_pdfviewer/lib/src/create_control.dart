import 'package:flet/flet.dart';

import 'flet_pdfviewer.dart';

CreateControlFactory createControl = (CreateControlArgs args) {
  switch (args.control.type) {
    case "flet_pdfviewer":
      return FletPdfviewerControl(
        parent: args.parent,
        control: args.control,
        children: args.children,
        backend: args.backend,
      );
    default:
      return null;
  }
};

void ensureInitialized() {
  // nothing to initialize
}
