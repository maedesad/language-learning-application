import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';

// colors
import '../theme/colors/semantic_colors.dart';

class BaseBackground extends StatelessWidget {
  final Widget child;

  const BaseBackground({super.key, required this.child});

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: [
        // background
        Container(
          decoration: const BoxDecoration(
            color: SemanticColors.backgroundBaseBlueColor, // sky blue background color
          ),
          child: Stack(
            children: [
              Positioned(
                  left: -75.w,
                  top: 54.h,
                child: Container(
                  width: 1100.w,
                  height: 1100.h,
                  decoration: const BoxDecoration(
                    shape: BoxShape.circle,
                    gradient: RadialGradient(
                      center: Alignment.center,
                      radius: 0.5,
                      colors: [
                        SemanticColors.BackgroundPurpleGradientColor, // purple - 100 opacity
                        SemanticColors.BackgroundYellowGradientColor, // yellow - 0 opacity
                      ],
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),

        // page content
        child,
      ],
    );
  }
}
