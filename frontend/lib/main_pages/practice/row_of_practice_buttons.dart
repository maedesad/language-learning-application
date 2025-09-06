import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'practice_page_widgets/four_button_row_layout.dart';
import 'practice_page_widgets/three_button_row_layout.dart';
import 'practice_page_widgets/two_button_row_layout.dart';
import 'practice_button_data.dart';


// dimensions
import '../../theme/dimensions.dart';
// text style
import '../../theme/text_style/text_style.dart';



class PracticeRow extends StatelessWidget {
  final int rowIndex;
  final String title;
  final List<PracticeButtonData> buttonsData;
  final int? selectedIndex;
  final bool hasAnySelected;
  final Function(int) onSelected;
  final VoidCallback onUnselect;

  const PracticeRow({
    super.key,
    required this.rowIndex,
    required this.title,
    required this.buttonsData,
    required this.selectedIndex,
    required this.hasAnySelected,
    required this.onSelected,
    required this.onUnselect,
  });

  @override
  Widget build(BuildContext context) {
    Widget buttonsWidget;

    if (buttonsData.length == 2) {
      buttonsWidget = TwoButtonRowLayout(
        buttonsData: buttonsData,
        selectedIndex: selectedIndex,
        hasAnySelected: hasAnySelected,
        onSelected: onSelected,
        onUnselect:onUnselect
      );
    } else if (buttonsData.length == 3) {
      buttonsWidget = ThreeButtonRowLayout(
        buttonsData: buttonsData,
        selectedIndex: selectedIndex,
        hasAnySelected: hasAnySelected,
        onSelected: onSelected,
        onUnselect:onUnselect
      );
    } else {
      buttonsWidget = FourButtonRowLayout(
        buttonsData: buttonsData,
        selectedIndex: selectedIndex,
        hasAnySelected: hasAnySelected,
        onSelected: onSelected,
        onUnselect:onUnselect
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

