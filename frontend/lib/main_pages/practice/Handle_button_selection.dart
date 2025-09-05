import 'package:flutter/material.dart';

mixin HandleButtonSelection<T extends StatefulWidget> on State<T> {
  // انتخاب‌ها
  Map<int, int?> selectedIndices = {};

  // کنترل اسکرول
  final ScrollController scrollController = ScrollController();

  // کلیدها برای هر ردیف
  final Map<int, GlobalKey> rowKeys = {
    0: GlobalKey(),
    1: GlobalKey(),
    2: GlobalKey(),
  };

  // پاک کردن انتخاب‌ها
  void clearSelection() {
    setState(() {
      selectedIndices.clear();
    });
  }

  // هندل انتخاب دکمه
  void onButtonSelected(int rowIndex, int buttonIndex) {
    setState(() {
      selectedIndices.clear();
      selectedIndices[rowIndex] = buttonIndex;
    });

    final keyContext = rowKeys[rowIndex]?.currentContext;
    if (keyContext != null) {
      Scrollable.ensureVisible(
        keyContext,
        duration: const Duration(milliseconds: 300),
        alignment: 0.5,
      );
    }
  }
}

