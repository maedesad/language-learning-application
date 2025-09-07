import 'package:flutter/material.dart';


// colors
import '../colors/semantic_colors.dart';
// dimensions
import '../dimensions.dart';

class TextStyles {

  static const String fontFamily = "Inter";
  
  static TextStyle get h2_mainTitle => TextStyle(
      fontSize: Dimensions.h2_mainTilte,      
      color: SemanticColors.textColor,
      fontWeight: FontWeight.w700,
      height: Dimensions.h2_text_hight,
      letterSpacing: Dimensions.text_letterSpacing,
      fontFamily: fontFamily,
    );

  static TextStyle get ButtonTextDark => TextStyle(
      fontSize: Dimensions.ButtonText,      
      color: SemanticColors.textColor,
      fontWeight: FontWeight.w600,      
      letterSpacing: Dimensions.text_letterSpacing,
      fontFamily: fontFamily,
  );  

  static TextStyle get ButtonTextLight => TextStyle(
      fontSize: Dimensions.ButtonText,      
      color: SemanticColors.surface,
      fontWeight: FontWeight.w600,      
      letterSpacing: Dimensions.text_letterSpacing,
      fontFamily: fontFamily,
  ); 

}  