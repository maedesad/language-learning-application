import 'package:flutter/material.dart';
import 'practice_entry_popup.dart';

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
  Future<void> onButtonSelected(int rowIndex, int buttonIndex, GlobalKey buttonKey, String title, Widget practiceEntryPage) async {
    setState(() {
      selectedIndices.clear();
      selectedIndices[rowIndex] = buttonIndex;
    });

    final keyContext = rowKeys[rowIndex]?.currentContext;
    if (keyContext != null) {
      await Scrollable.ensureVisible(
        keyContext,
        duration: const Duration(milliseconds: 500),
        alignment: 0.5,
      );
      if (!mounted) return;
      // صبر برای اتمام انیمیشن دکمه (AnimatedContainer ~300ms) و فریم پایانی
      await Future<void>.delayed(const Duration(milliseconds: 50));
      await WidgetsBinding.instance.endOfFrame;
      if (!mounted) return;
      PracticePopup.showPopup(
        context: context,
        buttonKey: buttonKey,
        title: title,
        practiceEntryPage: practiceEntryPage,
        arrowPosition: PopupArrowPosition.left,
        direction: PopupDirection.down,
      );
    }
  }
}

