import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';


// colors
import '../../theme/colors/semantic_colors.dart';
// dimensions
import '../../theme/dimensions.dart';

class PracticeButton extends StatelessWidget {
  final String iconPath;
  final String title; // تایتل به عنوان ورودی
  final bool isSelected;
  final bool shouldShrink;
  final GlobalKey buttonKey;
  final Widget practiceEntryPage;
  final VoidCallback onSelected;
  final VoidCallback? onUnselect;

  const PracticeButton({
    super.key,
    required this.iconPath,
    required this.title,
    required this.isSelected,
    required this.shouldShrink,
    required this.buttonKey,
    required this.practiceEntryPage,
    required this.onSelected,
    required this.onUnselect,
  });

  @override
  Widget build(BuildContext context) {
    double size;
    if (isSelected) {
      size = Dimensions.practiceButtonNormal;
    } else if (shouldShrink) {
      size = Dimensions.practiceButtonSmall;
    } else {
      size = Dimensions.practiceButtonNormal;
    }

    Color bgColor = isSelected ? SemanticColors.grayButton : SemanticColors.surface;

    return GestureDetector(
      onTap: () {
        onSelected();
      },
      child: AnimatedContainer(
        key: buttonKey,
        duration: const Duration(milliseconds: 300),
        width: size,
        height: size,
        decoration: BoxDecoration(
          color: bgColor,
          borderRadius: BorderRadius.circular(Dimensions.largeRadius),
          border: Border.all(color: SemanticColors.border, width: Dimensions.border),
        ),
        child: Center(
          child: SvgPicture.asset(
            iconPath,
            width: size * 0.5,
            height: size * 0.5,
          ),
        ),
      ),
    );
  }
}
