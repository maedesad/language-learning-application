import 'package:flutter_screenutil/flutter_screenutil.dart';

/// This class centralizes all constant dimensions
/// like border radius, paddings, margins, button sizes, etc.
/// All values are responsive with ScreenUtil.
class Dimensions {
  //Screen dimensions
  static double screenHeight = 956.h;
  static double screenWidth = 440.w; 

  // Border radius 
  static double mediumRadius = 8.r;  /// unused

  // Border thickness
  static double border = 0.5.w;
  static double bottomNavBarBorder = 1.w;

  // Button sizes
  static double buttonHeight = 48.h;            /// unused
  static double buttonWidth = 200.w;            /// unused

  // Padding
  static double screenHorizontalPadding = 32.w;  
 
  // Gaps
  static double smallGap = 8.h; /// unused

  // app text size
  static double h2_mainTilte = 22.sp;
  static double h2_figmaLineHeight = 45.h;
  static double figmaLetterSpacing = 7.w;
  static double h2_text_hight = h2_figmaLineHeight / h2_mainTilte;
  static double text_letterSpacing = (figmaLetterSpacing / 100) * h2_mainTilte;
}
