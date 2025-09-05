import 'package:flutter/material.dart';
import '../practice_button.dart';

// dimensions
import '../../../theme/dimensions.dart';




class FourButtonRowLayout extends StatelessWidget {
  final List<String> icons;
  final int? selectedIndex;
  final bool hasAnySelected;
  final Function(int) onSelected;

  const FourButtonRowLayout({
    super.key,
    required this.icons,
    required this.selectedIndex,
    required this.hasAnySelected,
    required this.onSelected,
  });

  @override
  Widget build(BuildContext context) {
    // دکمه‌ها
    List<Widget> buttons = List.generate(4, (i) {
      return PracticeButton(
        iconPath: icons[i],
        isSelected: selectedIndex == i,
        shouldShrink: selectedIndex != null && selectedIndex != i, // فقط هم‌ردیفی‌ها
        onTap: () => onSelected(i),
      );
    });

    // ویجت برای ردیف دکمه‌ها با فاصله 16
    Row buildRow(List<Widget> rowButtons, MainAxisAlignment mainAxis, CrossAxisAlignment crossAxis) {
      List<Widget> spacedButtons = [];
      for (int i = 0; i < rowButtons.length; i++) {
        spacedButtons.add(rowButtons[i]);
        if (i != rowButtons.length - 1) {
          spacedButtons.add(SizedBox(width: Dimensions.horizontalMediumGap));
        }
      }
      return Row(
        mainAxisAlignment: mainAxis,
        crossAxisAlignment: crossAxis,
        children: spacedButtons,
      );
    }

    if (selectedIndex == null) {
      return Wrap(
        spacing: Dimensions.horizontalMediumGap,
        runSpacing: Dimensions.verticalMediumGap,
        children: buttons,
      );
    }

    Widget topRow;
    Widget bottomRow;

    switch (selectedIndex) {
      case 0: // بالا چپ
        topRow = buildRow(buttons.sublist(0, 2), MainAxisAlignment.start, CrossAxisAlignment.center);
        bottomRow = buildRow(buttons.sublist(2), MainAxisAlignment.center, CrossAxisAlignment.start);
        break;
      case 1: // بالا راست
        topRow = buildRow(buttons.sublist(0, 2), MainAxisAlignment.end, CrossAxisAlignment.center);
        bottomRow = buildRow(buttons.sublist(2), MainAxisAlignment.center, CrossAxisAlignment.start);
        break;
      case 2: // پایین چپ
        topRow = buildRow(buttons.sublist(0, 2), MainAxisAlignment.center, CrossAxisAlignment.end);
        bottomRow = buildRow(buttons.sublist(2), MainAxisAlignment.start, CrossAxisAlignment.start);
        break;
      case 3: // پایین راست
        topRow = buildRow(buttons.sublist(0, 2), MainAxisAlignment.center, CrossAxisAlignment.end);
        bottomRow = buildRow(buttons.sublist(2), MainAxisAlignment.end, CrossAxisAlignment.start);
        break;
      default:
        topRow = buildRow(buttons.sublist(0, 2), MainAxisAlignment.start, CrossAxisAlignment.center);
        bottomRow = buildRow(buttons.sublist(2), MainAxisAlignment.start, CrossAxisAlignment.center);
    }

    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        topRow,
        SizedBox(height: Dimensions.verticalMediumGap),
        bottomRow,
      ],
    );
  }
}