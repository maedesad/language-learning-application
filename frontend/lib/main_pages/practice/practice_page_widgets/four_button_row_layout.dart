import 'package:flutter/material.dart';
import '../practice_button.dart';
import '../practice_button_data.dart';


// dimensions
import '../../../theme/dimensions.dart';




class FourButtonRowLayout extends StatelessWidget {
  final List<PracticeButtonData> buttonsData; // به جای فقط آیکن
  final int? selectedIndex;
  final bool hasAnySelected;
  final Function(int, GlobalKey, String, Widget) onSelected;
  final VoidCallback onUnselect;
  final List<GlobalKey> buttonKeys;

  const FourButtonRowLayout({
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
    List<Widget> buttons = List.generate(4, (i) {
      return PracticeButton(
          iconPath: buttonsData[i].iconPath,
          title: buttonsData[i].title,
          practiceEntryPage: buttonsData[i].page,
          isSelected: selectedIndex == i,
          shouldShrink: selectedIndex != null && selectedIndex != i,
          buttonKey: buttonKeys[i], // هر دکمه کلید جدا داشته باشه
          onSelected: () => onSelected(i, buttonKeys[i], buttonsData[i].title, buttonsData[i].page),
          onUnselect: onUnselect,
        );
    });

    // ویجت برای ردیف‌ها
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
      case 0: 
        topRow = buildRow(buttons.sublist(0, 2), MainAxisAlignment.start, CrossAxisAlignment.center);
        bottomRow = buildRow(buttons.sublist(2), MainAxisAlignment.center, CrossAxisAlignment.start);
        break;
      case 1: 
        topRow = buildRow(buttons.sublist(0, 2), MainAxisAlignment.end, CrossAxisAlignment.center);
        bottomRow = buildRow(buttons.sublist(2), MainAxisAlignment.center, CrossAxisAlignment.start);
        break;
      case 2: 
        topRow = buildRow(buttons.sublist(0, 2), MainAxisAlignment.center, CrossAxisAlignment.end);
        bottomRow = buildRow(buttons.sublist(2), MainAxisAlignment.start, CrossAxisAlignment.start);
        break;
      case 3: 
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
