import 'package:flutter/material.dart';

class PracticePopup {
  static OverlayEntry? _currentPopup;

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

    final RenderBox buttonBox =
        buttonKey.currentContext!.findRenderObject() as RenderBox;
    final Offset buttonPosition = buttonBox.localToGlobal(Offset.zero);
    final Size buttonSize = buttonBox.size;

    const double popupWidth = 312;
    const double popupHeight = 201;
    const double arrowSize = 20;

    // مرکز صفحه برای الاین افقی پاپ‌آپ
    final double screenWidth = MediaQuery.of(context).size.width;
    final double popupLeft = (screenWidth - popupWidth) / 2;

    // موقعیت نوک فلش نسبت به پاپ‌آپ
    double arrowLeft = buttonPosition.dx + buttonSize.width / 2 - popupLeft - arrowSize / 2;
    arrowLeft = arrowLeft.clamp(16.0, popupWidth - arrowSize - 16.0);

    double top = direction == PopupDirection.down
        ? buttonPosition.dy + buttonSize.height + arrowSize
        : buttonPosition.dy - popupHeight - arrowSize;

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
                  arrowSize: arrowSize,
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
  final double arrowSize;
  final double arrowLeft;
  final VoidCallback? onHide;

  const _PopupContent({
    required this.title,
    required this.onPurpleButtonTap,
    required this.isTwoButtonMode,
    required this.arrowPosition,
    required this.direction,
    required this.arrowSize,
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
            color: Colors.grey[800],
            borderRadius: BorderRadius.circular(12),
          ),
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            mainAxisSize: MainAxisSize.min,
            children: [
              Text(title,
                  style: const TextStyle(color: Colors.white, fontSize: 16)),
              const SizedBox(height: 12),
              if (isTwoButtonMode) ...[
                ElevatedButton(
                  onPressed: null,
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.blue[200],
                  ),
                  child: const Text("Start Planned Quest"),
                ),
                const SizedBox(height: 8),
              ],
              ElevatedButton(
                onPressed: onPurpleButtonTap,
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.purple[200],
                ),
                child: const Text("Start New Quest"),
              ),
            ],
          ),
        ),

        // فلش
        Positioned(
          top: direction == PopupDirection.down ? -arrowSize : null,
          bottom: direction == PopupDirection.up ? -arrowSize : null,
          left: arrowLeft,
          child: CustomPaint(
            size: Size(arrowSize, arrowSize),
            painter: _ArrowPainter(direction, Colors.grey[800]!),
          ),
        ),
      ],
    );
  }
}

class _ArrowPainter extends CustomPainter {
  final PopupDirection direction;
  final Color color;

  _ArrowPainter(this.direction, this.color);

  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint()..color = color;
    final path = Path();
    if (direction == PopupDirection.down) {
      path.moveTo(0, size.height);
      path.lineTo(size.width / 2, 0);
      path.lineTo(size.width, size.height);
    } else {
      path.moveTo(0, 0);
      path.lineTo(size.width / 2, size.height);
      path.lineTo(size.width, 0);
    }
    path.close();
    canvas.drawPath(path, paint);
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}
