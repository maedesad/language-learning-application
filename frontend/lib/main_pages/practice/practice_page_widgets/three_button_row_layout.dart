import 'package:flutter/material.dart';
import '../practice_button.dart';
import '../practice_button_data.dart';

// dimensions
import '../../../theme/dimensions.dart';

class ThreeButtonRowLayout extends StatelessWidget {
  final List<PracticeButtonData> buttonsData;
  final int? selectedIndex;
  final bool hasAnySelected;
  final Function(int, GlobalKey, String, Widget) onSelected;
  final VoidCallback onUnselect;
  final List<GlobalKey> buttonKeys;

  const ThreeButtonRowLayout({
    super.key,
    required this.buttonsData,
    required this.selectedIndex,
    required this.hasAnySelected,
    required this.onSelected,
    required this.onUnselect,
    required this.buttonKeys,
  });

  @override
  Widget build(BuildContext context) {
    // ساخت دکمه‌ها
    List<Widget> buttons = List.generate(3, (i) {
      return PracticeButton(
          iconPath: buttonsData[i].iconPath,
          title: buttonsData[i].title,
          practiceEntryPage: buttonsData[i].page,
          isSelected: selectedIndex == i,
          shouldShrink: selectedIndex != null && selectedIndex != i,
          buttonKey: buttonKeys[i],
          onSelected: () => onSelected(i, buttonKeys[i], buttonsData[i].title, buttonsData[i].page),
          onUnselect: onUnselect,
        );
    });

    // تابع کمکی برای فاصله بین دکمه‌ها
    Row buildRow(List<Widget> rowButtons) {
      List<Widget> spacedButtons = [];
      for (int i = 0; i < rowButtons.length; i++) {
        spacedButtons.add(rowButtons[i]);
        if (i != rowButtons.length - 1) {
          spacedButtons.add(SizedBox(width: Dimensions.horizontalMediumGap));
        }
      }
      return Row(
        mainAxisAlignment: MainAxisAlignment.center,
        children: spacedButtons,
      );
    }

    // ردیف بالا (۲ دکمه)
    Widget topRow = buildRow(buttons.sublist(0, 2));

    // دکمه پایین (۱ دکمه وسط)
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