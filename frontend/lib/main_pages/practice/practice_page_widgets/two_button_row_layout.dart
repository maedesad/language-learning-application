import 'package:flutter/material.dart';
import '../practice_button.dart';
import '../practice_button_data.dart';

// dimensions
import '../../../theme/dimensions.dart';


class TwoButtonRowLayout extends StatelessWidget {
  final List<PracticeButtonData> buttonsData;
  final int? selectedIndex;
  final bool hasAnySelected;
  final Function(int) onSelected;

  const TwoButtonRowLayout({
    super.key,
    required this.buttonsData,
    required this.selectedIndex,
    required this.hasAnySelected,
    required this.onSelected,
  });

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        PracticeButton(
          iconPath: buttonsData[0].iconPath,
          title: buttonsData[0].title,
          practiceEntryPage: buttonsData[0].page,
          isSelected: selectedIndex == 0,
          shouldShrink: selectedIndex != null && selectedIndex != 0,
          buttonKey: GlobalKey(),
          onSelected: () => onSelected(0),
        ),
        SizedBox(width: Dimensions.horizontalMediumGap),
        PracticeButton(
          iconPath: buttonsData[1].iconPath,
          title: buttonsData[1].title,
          practiceEntryPage: buttonsData[1].page,
          isSelected: selectedIndex == 1,
          shouldShrink: selectedIndex != null && selectedIndex != 1,
          buttonKey: GlobalKey(),
          onSelected: () => onSelected(1),
        ),
      ],
    );
  }
}
