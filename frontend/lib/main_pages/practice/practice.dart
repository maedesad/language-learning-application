import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';

class PracticingPage extends StatefulWidget {
  const PracticingPage({super.key});

  @override
  State<PracticingPage> createState() => _PracticingPageState();
}

class _PracticingPageState extends State<PracticingPage> {
  // -----------------------------
  // Selected button per row
  // key = rowIndex, value = selected button index
  // -----------------------------
  Map<int, int?> selectedIndices = {};

  // -----------------------------
  // Scroll controller to scroll to selected button
  // -----------------------------
  final ScrollController _scrollController = ScrollController();

  // -----------------------------
  // Keys to identify each row
  // -----------------------------
  final Map<int, GlobalKey> rowKeys = {
    0: GlobalKey(),
    1: GlobalKey(),
    2: GlobalKey(),
  };

  // -----------------------------
  // Clear all selections
  // -----------------------------
  void clearSelection() {
    setState(() {
      selectedIndices.clear();
    });
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      // Dismiss selection when tapping outside buttons
      onTap: clearSelection,
      behavior: HitTestBehavior.translucent,
      child: Scaffold(
        body: ListView(
          controller: _scrollController,
          children: [
            PracticeRow(
              key: rowKeys[0],
              rowIndex: 0,
              title: "Train Your Skills",
              icons: [
                "assets/practice_icons/Reading.svg",
                "assets/practice_icons/listening.svg",
                "assets/practice_icons/Writing.svg",
                "assets/practice_icons/Conversation.svg",
              ],
              selectedIndex: selectedIndices[0],
              onSelected: (i) => onButtonSelected(0, i),
            ),
            PracticeRow(
              key: rowKeys[1],
              rowIndex: 1,
              title: "Unlock Knowledge",
              icons: [
                "assets/practice_icons/Vocabulary learning.svg",
                "assets/practice_icons/Grammar learning.svg",
              ],
              selectedIndex: selectedIndices[1],
              onSelected: (i) => onButtonSelected(1, i),
            ),
            PracticeRow(
              key: rowKeys[2],
              rowIndex: 2,
              title: "Recall Your Knowledge",
              icons: [
                "assets/practice_icons/Vocabulary review.svg",
                "assets/practice_icons/Grammar review.svg",
                "assets/practice_icons/Vocabulary&Grammar review.svg",
              ],
              selectedIndex: selectedIndices[2],
              onSelected: (i) => onButtonSelected(2, i),
            ),
          ],
        ),
      ),
    );
  }

  // -----------------------------
  // Handle button selection
  // -----------------------------
  void onButtonSelected(int rowIndex, int buttonIndex) {
    setState(() {
      // Clear all other selections and select only the current button
      selectedIndices.clear();
      selectedIndices[rowIndex] = buttonIndex;
    });

    // Scroll the row to the center of the screen
    final keyContext = rowKeys[rowIndex]?.currentContext;
    if (keyContext != null) {
      Scrollable.ensureVisible(
        keyContext,
        duration: const Duration(milliseconds: 300),
        alignment: 0.5, // 0 = top, 1 = bottom, 0.5 = center
      );
    }
  }
}

// -----------------------------
// Widget for a row of practice buttons
// -----------------------------
class PracticeRow extends StatelessWidget {
  final int rowIndex;
  final String title;
  final List<String> icons;
  final int? selectedIndex;
  final Function(int) onSelected;

  const PracticeRow({
    super.key,
    required this.rowIndex,
    required this.title,
    required this.icons,
    required this.selectedIndex,
    required this.onSelected,
  });

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 24),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Row title
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 32.0),
            child: Text(
              title,
              style: const TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.bold,
              ),
            ),
          ),
          const SizedBox(height: 16),
          // Buttons in the row
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 64.0),
            child: Wrap(
              spacing: 16,
              runSpacing: 16,
              children: List.generate(icons.length, (i) {
                return PracticeButton(
                  iconPath: icons[i],
                  isSelected: selectedIndex == i,
                  isUnselected: selectedIndex != null && selectedIndex != i,
                  onTap: () => onSelected(i),
                );
              }),
            ),
          ),
        ],
      ),
    );
  }
}

// -----------------------------
// Widget for a single practice button
// -----------------------------
class PracticeButton extends StatelessWidget {
  final String iconPath;
  final bool isSelected;
  final bool isUnselected;
  final VoidCallback onTap;

  const PracticeButton({
    super.key,
    required this.iconPath,
    required this.isSelected,
    required this.isUnselected,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    // Change size and color based on selection state
    double size = isUnselected ? 132 : 148;
    Color bgColor = isSelected ? Colors.grey[700]! : Colors.blue[50]!;

    return GestureDetector(
      onTap: () {
        // Prevent outer GestureDetector from firing
        onTap();
      },
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 200),
        width: size,
        height: size,
        decoration: BoxDecoration(
          color: bgColor,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: Colors.grey, width: 0.5),
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
