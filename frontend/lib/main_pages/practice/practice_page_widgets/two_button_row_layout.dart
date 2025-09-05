import 'package:flutter/material.dart';
import '../practice_button.dart';
// dimensions
import '../../../theme/dimensions.dart';


class TwoButtonRowLayout extends StatelessWidget {
  final List<String> icons;
  final int? selectedIndex;
  final bool hasAnySelected;
  final Function(int) onSelected;

  const TwoButtonRowLayout({
    super.key,
    required this.icons,
    required this.selectedIndex,
    required this.hasAnySelected,
    required this.onSelected,
  });

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      crossAxisAlignment: CrossAxisAlignment.center,
      children: [
        PracticeButton(
          iconPath: icons[0],
          isSelected: selectedIndex == 0,
          hasAnySelected: hasAnySelected,
          onTap: () => onSelected(0),
        ),
        SizedBox(width: Dimensions.horizontalMediumGap), // فاصله 16 بین دکمه‌ها
        PracticeButton(
          iconPath: icons[1],
          isSelected: selectedIndex == 1,
          hasAnySelected: hasAnySelected,
          onTap: () => onSelected(1),
        ),
      ],
    );
  }
}