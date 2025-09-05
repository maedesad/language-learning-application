import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';

// dimensions
import '../../theme/dimensions.dart';
// text style
import '../../theme/text_style/text_style.dart';
import 'practice_page_widgets/four_button_row_layout.dart';
import 'practice_page_widgets/three_button_row_layout.dart';
import 'practice_page_widgets/two_button_row_layout.dart';

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
    // مقداردهی اولیه به متغیر ویجت دکمه‌ها
    Widget buttonsWidget = SizedBox();

    if (icons.length == 2) {
      buttonsWidget = TwoButtonRowLayout(
        icons: icons,
        selectedIndex: selectedIndex,
        hasAnySelected: hasAnySelected,
        onSelected: onSelected,
      );
    } else if (icons.length == 3) {
      buttonsWidget = ThreeButtonRowLayout(
        icons: icons,
        selectedIndex: selectedIndex,
        hasAnySelected: hasAnySelected,
        onSelected: onSelected,
      );
    } else {
      buttonsWidget = FourButtonRowLayout(
        icons: icons,
        selectedIndex: selectedIndex,
        hasAnySelected: hasAnySelected,
        onSelected: onSelected,
      );
    }

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        // عنوان ردیف
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

        // دکمه‌های ردیف
        Padding(
          padding: EdgeInsets.only(
            left: Dimensions.screenHorizontalLargePadding,
            right: Dimensions.screenHorizontalLargePadding,
            top: 24.h,
            bottom: 58.h,
          ),
          child: buttonsWidget,
        ),
      ],
    );
  }
}