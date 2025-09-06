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

    const double popupWidth = 200;
    const double popupHeight = 140;
    const double arrowSize = 12;

    double left;
    if (arrowPosition == PopupArrowPosition.left) {
      left = buttonPosition.dx;
    } else if (arrowPosition == PopupArrowPosition.right) {
      left = buttonPosition.dx + buttonSize.width - popupWidth;
    } else {
      left = buttonPosition.dx + buttonSize.width / 2 - popupWidth / 2;
    }

    double top = direction == PopupDirection.down
        ? buttonPosition.dy + buttonSize.height + arrowSize
        : buttonPosition.dy - popupHeight - arrowSize;

    _currentPopup = OverlayEntry(
      builder: (context) {
        return Stack(
          children: [
            Positioned(
              top: top,
              left: left,
              width: popupWidth,
              child: Material(
                color: Colors.transparent,
                child: _PopupContent(
                  title: title,
                  arrowPosition: arrowPosition,
                  direction: direction,
                  isTwoButtonMode: isTwoButtonMode,
                  arrowSize: arrowSize,
                  onPurpleButtonTap: () {
                    hidePopup();
                    Navigator.push(
                      context,
                      MaterialPageRoute(builder: (_) => practiceEntryPage),
                    );
                  },
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

  const _PopupContent({
    required this.title,
    required this.onPurpleButtonTap,
    required this.isTwoButtonMode,
    required this.arrowPosition,
    required this.direction,
    required this.arrowSize,
  });

  @override
  Widget build(BuildContext context) {
    return Stack(
      clipBehavior: Clip.none,
      children: [
        // مستطیل اصلی پاپ‌آپ
        Container(
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
          left: _calculateArrowLeft(),
          child: CustomPaint(
            size: Size(arrowSize, arrowSize),
            painter: _ArrowPainter(direction, Colors.grey[800]!),
          ),
        ),
      ],
    );
  }

  double _calculateArrowLeft() {
    switch (arrowPosition) {
      case PopupArrowPosition.left:
        return 16;
      case PopupArrowPosition.right:
        return 200 - arrowSize - 16;
      case PopupArrowPosition.center:
      default:
        return 200 / 2 - arrowSize / 2;
    }
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
      // مثلث به سمت بالا
      path.moveTo(0, size.height);
      path.lineTo(size.width / 2, 0);
      path.lineTo(size.width, size.height);
    } else {
      // مثلث به سمت پایین
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