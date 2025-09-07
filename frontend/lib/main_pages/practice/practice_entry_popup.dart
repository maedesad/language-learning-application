import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';


// colors
import '../../theme/colors/semantic_colors.dart';
// dimensions
import '../../theme/dimensions.dart';
// text
import '../../theme/text.dart';
// text style
import '../../theme/text_style/text_style.dart';

class PracticePopup {
  static OverlayEntry? _currentPopup;
  static bool get isVisible => _currentPopup != null;

  static void showPopup({
    required BuildContext context,
    required GlobalKey buttonKey,
    required String title,
    required Widget practiceEntryPage,
    bool isTwoButtonMode = true,
    PopupArrowPosition arrowPosition = PopupArrowPosition.center,
    PopupDirection direction = PopupDirection.down,
    VoidCallback? onHide,
  }) {
    hidePopup();

    final BuildContext? targetContext = buttonKey.currentContext;
    if (targetContext == null) {
      // اگر به هر دلیل هنوز ویجت رندر نشده، از نمایش پاپ‌آپ صرف نظر کن
      return;
    }
    final RenderBox buttonBox =
        targetContext.findRenderObject() as RenderBox;
    final Offset buttonPosition = buttonBox.localToGlobal(Offset.zero);
    final Size buttonSize = buttonBox.size;

    double popupWidth = Dimensions.popupWidth;
    double popupHeight = Dimensions.popupHeight;
    double arrowWidth = 34.w;
    double arrowHeight = 15.h;

    // مرکز صفحه برای الاین افقی پاپ‌آپ
    final double screenWidth = MediaQuery.of(context).size.width;
    final double popupLeft = (screenWidth - popupWidth) / 2;

    // موقعیت نوک فلش نسبت به پاپ‌آپ
    double arrowLeft = buttonPosition.dx + buttonSize.width / 2 - popupLeft - arrowWidth / 2;
    arrowLeft = arrowLeft.clamp(16.0, popupWidth - arrowWidth - 16.0);

    double top = direction == PopupDirection.down
        ? buttonPosition.dy + buttonSize.height + arrowWidth
        : buttonPosition.dy - popupHeight - arrowWidth;

    _currentPopup = OverlayEntry(
      builder: (context) {
        return Stack(
          children: [
            Positioned(
              top: top,
              left: popupLeft,
              width: popupWidth,
              height: popupHeight,
              child: Material(
                color: Colors.transparent,
                child: _PopupContent(
                  title: title,
                  arrowPosition: arrowPosition,
                  direction: direction,
                  isTwoButtonMode: isTwoButtonMode,
                  arrowWidth: arrowWidth,
                  arrowHeight: arrowHeight,
                  arrowLeft: arrowLeft,
                  onPurpleButtonTap: () {
                    hidePopup();
                    Navigator.push(
                      context,
                      MaterialPageRoute(builder: (_) => practiceEntryPage),
                    );
                  },
                  onHide: onHide,
                ),
              ),
            ),
          ],
        );
      },
    );

    Overlay.of(context).insert(_currentPopup!);
  }

  static void hidePopup() {
    _currentPopup?.remove();
    _currentPopup = null;
  }
}

enum PopupArrowPosition { left, center, right }
enum PopupDirection { up, down }

class _PopupContent extends StatelessWidget {
  final String title;
  final VoidCallback onPurpleButtonTap;
  final bool isTwoButtonMode;
  final PopupArrowPosition arrowPosition;
  final PopupDirection direction;
  final double arrowWidth;   // عرض دلخواه مثلث
  final double arrowHeight;
  final double arrowLeft;
  final VoidCallback? onHide;

  const _PopupContent({
    required this.title,
    required this.onPurpleButtonTap,
    required this.isTwoButtonMode,
    required this.arrowPosition,
    required this.direction,
    required this.arrowWidth,
    required this.arrowHeight,
    required this.arrowLeft,
    this.onHide,
  });

  @override
  Widget build(BuildContext context) {
    return Stack(
      clipBehavior: Clip.none,
      children: [
        // مستطیل اصلی پاپ‌آپ
        Container(
          width: double.infinity,
          height: double.infinity,
          decoration: BoxDecoration(
            color: SemanticColors.grayButton,
            borderRadius: BorderRadius.circular(Dimensions.largeRadius),
          ),
          padding: EdgeInsets.symmetric(
            horizontal: Dimensions.Paddingsize1,
            vertical: Dimensions.Paddingsize2,
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            mainAxisSize: MainAxisSize.min,
            children: [
              // Title always aligned left
              Text(
                title,
                style: TextStyles.ButtonTextLight,
              ),
              SizedBox(height: Dimensions.verticalLargeGap),

              if (isTwoButtonMode) ...[
                Center( // 🔹 دکمه در مرکز
                  child: ElevatedButton(
                    onPressed: onPurpleButtonTap,  /// change it later
                    style: ElevatedButton.styleFrom(
                      backgroundColor: SemanticColors.blueButton,
                      minimumSize: Size(248.w, Dimensions.buttonHeight),
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(Dimensions.smallRadius),
                      ),
                    ),
                    child: Text(
                      TextVariables.StartPlannedQuest,
                      style: TextStyles.ButtonTextDark,
                    ),
                  ),
                ),
                SizedBox(height: Dimensions.verticalSmallGap),
              ],

              Center( // 🔹 دکمه دوم هم در مرکز
                child: ElevatedButton(
                  onPressed: onPurpleButtonTap,
                  style: ElevatedButton.styleFrom(
                    backgroundColor: SemanticColors.purpleButton,
                    minimumSize: Size(248.w, Dimensions.buttonHeight),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(Dimensions.smallRadius),
                    ),
                  ),
                  child: Text(
                    TextVariables.StartNewQuest,
                    style: TextStyles.ButtonTextDark,
                  ),
                ),
              ),
            ],
          ),

        ),

        // فلش
        Positioned(
          top: direction == PopupDirection.down ? -arrowHeight : null,
          bottom: direction == PopupDirection.up ? -arrowHeight : null,
          left: arrowLeft,
          child: CustomPaint(
            size: Size(arrowWidth, arrowHeight),
            painter: _ArrowPainter(direction, SemanticColors.grayButton),
          ),
        ),
      ],
    );
  }
}

class _ArrowPainter extends CustomPainter {
  final PopupDirection direction;
  final Color color;
  final double arrowWidth;   // عرض دلخواه مثلث
  final double arrowHeight;  // ارتفاع دلخواه مثلث

  _ArrowPainter(this.direction, this.color, {this.arrowWidth = 34, this.arrowHeight = 15});

  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint()..color = color;
    final path = Path();

    if (direction == PopupDirection.down) {
      // مثلث به سمت بالا
      path.moveTo(0, arrowHeight);
      path.lineTo(arrowWidth / 2, 0);
      path.lineTo(arrowWidth, arrowHeight);
    } else {
      // مثلث به سمت پایین
      path.moveTo(0, 0);
      path.lineTo(arrowWidth / 2, arrowHeight);
      path.lineTo(arrowWidth, 0);
    }

    path.close();
    canvas.drawPath(path, paint);
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}



