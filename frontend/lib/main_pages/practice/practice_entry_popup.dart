import 'package:flutter/material.dart';


class PracticePopup {
  static OverlayEntry? _currentPopup;

  static void showPopup({
    required BuildContext context,
    required GlobalKey buttonKey,
    required String title,
    required Widget practiceEntryPage, // صفحه مقصد
    bool isTwoButtonMode = true,
    PopupArrowPosition arrowPosition = PopupArrowPosition.center,
    PopupDirection direction = PopupDirection.down,
    VoidCallback? onHide,
  }) {
    // بستن پاپ‌آپ قبلی اگه وجود داشته باشه
    hidePopup();

    final RenderBox buttonBox =
        buttonKey.currentContext!.findRenderObject() as RenderBox;
    final Offset buttonPosition = buttonBox.localToGlobal(Offset.zero);
    final Size buttonSize = buttonBox.size;

    _currentPopup = OverlayEntry(
      builder: (context) {
        // تعیین موقعیت پاپ‌آپ
        double top = direction == PopupDirection.down
            ? buttonPosition.dy + buttonSize.height + 8
            : buttonPosition.dy - 140; // ارتفاع تقریبی پاپ‌آپ

        double left;
        if (arrowPosition == PopupArrowPosition.left) {
          left = buttonPosition.dx;
        } else if (arrowPosition == PopupArrowPosition.right) {
          left = buttonPosition.dx + buttonSize.width - 200;
        } else {
          left = buttonPosition.dx + buttonSize.width / 2 - 100;
        }

        return Stack(
          children: [
            // کلیک روی فضای خالی → بستن پاپ‌آپ
            Positioned.fill(
              child: GestureDetector(
                onTap: () {
                  hidePopup();
                  if (onHide != null) onHide(); // 🔹 به parent خبر بده
                },
                child: Container(color: Colors.transparent),
              ),
            ),

            // خود پاپ‌آپ
            Positioned(
              top: top,
              left: left,
              width: 200,
              child: Material(
                color: Colors.transparent,
                child: _PopupContent(
                  title: title,
                  arrowPosition: arrowPosition,
                  direction: direction,
                  isTwoButtonMode: isTwoButtonMode,
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

  const _PopupContent({
    required this.title,
    required this.onPurpleButtonTap,
    required this.isTwoButtonMode,
    required this.arrowPosition,
    required this.direction,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        if (direction == PopupDirection.up) _buildArrow(),
        Container(
          decoration: BoxDecoration(
            color: Colors.grey[800],
            borderRadius: BorderRadius.circular(12),
          ),
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(title,
                  style: const TextStyle(color: Colors.white, fontSize: 16)),
              const SizedBox(height: 12),
              if (isTwoButtonMode) ...[
                ElevatedButton(
                  onPressed: null, // غیرفعال
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
        if (direction == PopupDirection.down) _buildArrow(),
      ],
    );
  }

  Widget _buildArrow() {
    Alignment alignment;
    if (arrowPosition == PopupArrowPosition.left) {
      alignment = Alignment.centerLeft;
    } else if (arrowPosition == PopupArrowPosition.right) {
      alignment = Alignment.centerRight;
    } else {
      alignment = Alignment.center;
    }

    return Align(
      alignment: alignment,
      child: Icon(
        direction == PopupDirection.down
            ? Icons.arrow_drop_up
            : Icons.arrow_drop_down,
        color: Colors.grey[800],
        size: 32,
      ),
    );
  }
}