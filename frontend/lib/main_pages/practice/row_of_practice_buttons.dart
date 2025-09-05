import 'package:flutter/material.dart';
import 'practice_button.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';

// dimensions
import '../../theme/dimensions.dart';
// text style
import '../../theme/text_style/text_style.dart';

class PracticeRow extends StatelessWidget {
  final int rowIndex;
  final String title;
  final List<String> icons;
  final int? selectedIndex;
  final bool hasAnySelected;
  final Function(int) onSelected;

  const PracticeRow({
    super.key,
    required this.rowIndex,
    required this.title,
    required this.icons,
    required this.selectedIndex,
    required this.hasAnySelected,
    required this.onSelected,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        // Row title
        Container(
          height: 77.h,
          padding: EdgeInsets.symmetric(
            horizontal: Dimensions.screenHorizontalPadding,
          ),
          alignment: Alignment.centerLeft,
          child: Text(
            title,
            style: TextStyles.h2_mainTitle,
          ),
        ),

        // Buttons in the row
        Padding(
          padding: EdgeInsets.only(
            left: Dimensions.screenHorizontalLargePadding,
            right: Dimensions.screenHorizontalLargePadding,
            top: 24.h,
            bottom: 58.h,
          ),
          child: Wrap(
            spacing: Dimensions.horizontalMediumGap,
            runSpacing: Dimensions.verticalMediumGap,
            children: List.generate(icons.length, (i) {
              return PracticeButton(
                iconPath: icons[i],
                isSelected: selectedIndex == i,
                hasAnySelected: hasAnySelected,
                onTap: () => onSelected(i),
              );
            }),
          ),
        ),
      ],
    );
  }
}
