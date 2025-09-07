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



class PracticeRow extends StatefulWidget {
  final int rowIndex;
  final String title;
  final List<PracticeButtonData> buttonsData;
  final int? selectedIndex;
  final bool hasAnySelected;
  final Function(int, GlobalKey, String, Widget) onSelected;
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
  State<PracticeRow> createState() => _PracticeRowState();
}

class _PracticeRowState extends State<PracticeRow> {
  late final List<GlobalKey> buttonKeys;

  @override
  void initState() {
    super.initState();
    buttonKeys = List<GlobalKey>.generate(widget.buttonsData.length, (_) => GlobalKey());
  }

  @override
  Widget build(BuildContext context) {
    Widget buttonsWidget;

    if (widget.buttonsData.length == 2) {
      buttonsWidget = TwoButtonRowLayout(
        buttonsData: widget.buttonsData,
        selectedIndex: widget.selectedIndex,
        hasAnySelected: widget.hasAnySelected,
        buttonKeys: buttonKeys,
        onSelected: widget.onSelected,
        onUnselect: widget.onUnselect,
      );
    } else if (widget.buttonsData.length == 3) {
      buttonsWidget = ThreeButtonRowLayout(
        buttonsData: widget.buttonsData,
        selectedIndex: widget.selectedIndex,
        hasAnySelected: widget.hasAnySelected,
        buttonKeys: buttonKeys,
        onSelected: widget.onSelected,
        onUnselect: widget.onUnselect,
      );
    } else {
      buttonsWidget = FourButtonRowLayout(
        buttonsData: widget.buttonsData,
        selectedIndex: widget.selectedIndex,
        hasAnySelected: widget.hasAnySelected,
        buttonKeys: buttonKeys,
        onSelected: widget.onSelected,
        onUnselect: widget.onUnselect,
      );
    }

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Container(
          height: 77.h,
          padding: EdgeInsets.symmetric(
            horizontal: Dimensions.screenHorizontalPadding,
          ),
          alignment: Alignment.centerLeft,
          child: Text(
            widget.title,
            style: TextStyles.h2_mainTitle,
          ),
        ),

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

