import 'package:flutter_screenutil/flutter_screenutil.dart';

/// This class centralizes all constant dimensions
/// like border radius, paddings, margins, button sizes, etc.
/// All values are responsive with ScreenUtil.
class Dimensions {
  //Screen dimensions
  static double screenHeight = 956.h;
  static double screenWidth = 440.w; 

  // Border radius 
  static double largeRadius = 16.r;  
  static double smallRadius = 8.r; 

  // Border thickness
  static double border = 0.5.w;
  static double bottomNavBarBorder = 1.w;

  // Button sizes
  static double buttonHeight = 48.h;            
  static double buttonWidth = 200.w;            /// unused

  // Padding
  static double screenHorizontalPadding = 32.w;  
  static double screenHorizontalLargePadding = 64.w;  
  static double Paddingsize1 = 16.w; 
  static double Paddingsize2 = 24.w; 
 
  // Gaps
  static double verticalSmallGap = 8.h; 
  static double horizontalSmallGap = 8.w; 
  static double verticalMediumGap = 16.h; 
  static double horizontalMediumGap = 16.w;
  static double verticalLargeGap = 24.h;

  // app text size
  static double h2_mainTilte = 22.sp;
  static double ButtonText = 17.sp;
  static double h2_figmaLineHeight = 45.h;
  static double figmaLetterSpacing = 7.w;
  static double h2_text_hight = h2_figmaLineHeight / h2_mainTilte;
  static double text_letterSpacing = (figmaLetterSpacing / 100) * h2_mainTilte;

  // practice button
    static double practiceButtonNormal = 148.w;        
    static double practiceButtonSmall = 132.w;

  // practice button popup 
  static double popupHeight = 201.h;            /// unused
  static double popupWidth = 312.w; 


 
}
