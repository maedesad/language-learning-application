import 'package:flutter/material.dart';
import 'handle_button_selection.dart';
import 'row_of_practice_buttons.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';

class PracticingPage extends StatefulWidget {
  const PracticingPage({super.key});

  @override
  State<PracticingPage> createState() => _PracticingPageState();
}

class _PracticingPageState extends State<PracticingPage>
    with HandleButtonSelection {
  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: clearSelection,
      behavior: HitTestBehavior.translucent,
      child: Scaffold(
        backgroundColor: Colors.transparent,
        body: ListView(
          controller: scrollController,
          children: [
            Padding(
              padding: EdgeInsets.only(
                top: 32.h,   
                bottom: 98.h, 
              ),
              child: Column(
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
                    hasAnySelected: selectedIndices.isNotEmpty,
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
                    hasAnySelected: selectedIndices.isNotEmpty,
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
                    hasAnySelected: selectedIndices.isNotEmpty,
                    onSelected: (i) => onButtonSelected(2, i),
                  ),
                ],
              ),
            ),
          ],
        ),

      ),
    );
  }
}

