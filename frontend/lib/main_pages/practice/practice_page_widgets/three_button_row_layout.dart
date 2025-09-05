import 'package:flutter/material.dart';
import '../practice_button.dart';

// dimensions
import '../../../theme/dimensions.dart';

class ThreeButtonRowLayout extends StatelessWidget {
  final List<String> icons;
  final int? selectedIndex;
  final bool hasAnySelected;
  final Function(int) onSelected;

  const ThreeButtonRowLayout({
    super.key,
    required this.icons,
    required this.selectedIndex,
    required this.hasAnySelected,
    required this.onSelected,
  });

  @override
  Widget build(BuildContext context) {
    // دکمه‌ها
    List<Widget> buttons = List.generate(3, (i) {
      return PracticeButton(
        iconPath: icons[i],
        isSelected: selectedIndex == i,
        hasAnySelected: hasAnySelected,
        onTap: () => onSelected(i),
      );
    });

    // تابع کمکی برای اضافه کردن فاصله بین دکمه‌ها
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

    // ردیف بالا با دو دکمه و فاصله 16
    Widget topRow = buildRow(buttons.sublist(0, 2), MainAxisAlignment.center, CrossAxisAlignment.center);

    // دکمه پایین تکی
    Widget bottomRow = Align(
      alignment: Alignment.topCenter,
      child: buttons[2],
    );

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