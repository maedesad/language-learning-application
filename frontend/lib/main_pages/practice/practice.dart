import 'package:flutter/material.dart';
import 'handle_button_selection.dart';
import 'row_of_practice_buttons.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';

import 'practice_button_data.dart';
import 'practice_entry_popup.dart';

// practices entry pages
import '../../practices/conversation/conversation_entry_page.dart';
import '../../practices/grammar_learning/grammar_learning_entry_page.dart';
import '../../practices/grammar_review/grammar_review_entry_page.dart';
import '../../practices/listening/listening_entry_page.dart';
import '../../practices/reading/reading_entry_page.dart';
import '../../practices/vocab&grammar_review/vocab&grammar_review_entry_page.dart';
import '../../practices/vocab_learning/vocab_learning_entry_page.dart';
import '../../practices/vocab_review/vocab_review_entry_page.dart';
import '../../practices/writing/writing_entry_page.dart';


// text
import '../../theme/text.dart';

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
      behavior: HitTestBehavior.translucent,
      onTapDown: (_) {
        // با اولین لمس، پاپ‌آپ رو ببند و انتخاب رو پاک کن
        PracticePopup.hidePopup();
        clearSelection();
      },
      child: Scaffold(
        backgroundColor: Colors.transparent,
        body: NotificationListener<ScrollNotification>(
          onNotification: (notification) {
            // اگر کاربر خودش (drag) اسکرول کرد → پاپ‌آپ را ببند و انتخاب پاک شود
            if (notification is UserScrollNotification) {
              // این notification وقتی تولید می‌شود که user با لمس اسکرول کند
              if (PracticePopup.isVisible) {
                PracticePopup.hidePopup();
                clearSelection();
              }
            } else if (notification is ScrollStartNotification && notification.dragDetails != null) {
              // بعضی مواقع ScrollStartNotification با dragDetails هم به عنوان scroll-by-user می‌آید
              if (PracticePopup.isVisible) {
                PracticePopup.hidePopup();
                clearSelection();
              }
            }
            // برنمی‌گردانیم true چون می‌خواهیم notification به بقیه هم برسد
            return false;
          },
          child: ListView(
            controller: scrollController,
            children: [
              Padding(
                padding: EdgeInsets.only(
                  top: 32.h,
                  bottom: 98.h,
                ),
                child: Column(
                  children: [
                    /// 🔹 ردیف اول
                    PracticeRow(
                      key: rowKeys[0],
                      rowIndex: 0,
                      title: "Train Your Skills",
                      buttonsData: [
                        PracticeButtonData(
                          iconPath: "assets/practice_icons/Reading.svg",
                          title: TextVariables.readingMotivatingTitle,
                          page: ReadingEntryPage(),
                        ),
                        PracticeButtonData(
                          iconPath: "assets/practice_icons/Listening.svg",
                          title: TextVariables.listeningMotivatingTitle,
                          page: ListeningEntryPage(),
                        ),
                        PracticeButtonData(
                          iconPath: "assets/practice_icons/Writing.svg",
                          title: TextVariables.writingMotivatingTitle,
                          page: WritingEntryPage(),
                        ),
                        PracticeButtonData(
                          iconPath: "assets/practice_icons/Conversation.svg",
                          title: TextVariables.conversationMotivatingTitle,
                          page: ConversationEntryPage(),
                        ),
                      ],
                      selectedIndex: selectedIndices[0],
                      hasAnySelected: selectedIndices.isNotEmpty,
                      onSelected: (i, key, title, page) => onButtonSelected(0, i, key, title, page),
                      onUnselect: clearSelection,
                    ),

                    /// 🔹 ردیف دوم
                    PracticeRow(
                      key: rowKeys[1],
                      rowIndex: 1,
                      title: "Unlock Knowledge",
                      buttonsData: [
                        PracticeButtonData(
                          iconPath: "assets/practice_icons/Vocabulary learning.svg",
                          title: TextVariables.vocabLearningMotivatingTitle,
                          page: VocabLearningEntryPage(),
                        ),
                        PracticeButtonData(
                          iconPath: "assets/practice_icons/Grammar learning.svg",
                          title: TextVariables.grammarLearningMotivatingTitle,
                          page: GrammarLearningEntryPage(),
                        ),
                      ],
                      selectedIndex: selectedIndices[1],
                      hasAnySelected: selectedIndices.isNotEmpty,
                      onSelected: (i, key, title, page) => onButtonSelected(1, i, key, title, page),
                      onUnselect: clearSelection,
                    ),

                    /// 🔹 ردیف سوم
                    PracticeRow(
                      key: rowKeys[2],
                      rowIndex: 2,
                      title: "Recall Your Knowledge",
                      buttonsData: [
                        PracticeButtonData(
                          iconPath: "assets/practice_icons/Vocabulary review.svg",
                          title: TextVariables.vocabReviewMotivatingTitle,
                          page: VocabReviewEntryPage(),
                        ),
                        PracticeButtonData(
                          iconPath: "assets/practice_icons/Grammar review.svg",
                          title: TextVariables.grammarReviewMotivatingTitle,
                          page: GrammarReviewEntryPage(),
                        ),
                        PracticeButtonData(
                          iconPath: "assets/practice_icons/Vocabulary&Grammar review.svg",
                          title: TextVariables.vocabGrammarReviewMotivatingTitle,
                          page: VocabGrammarReviewEntryPage(),
                        ),
                      ],
                      selectedIndex: selectedIndices[2],
                      hasAnySelected: selectedIndices.isNotEmpty,
                      onSelected: (i, key, title, page) => onButtonSelected(2, i, key, title, page),
                      onUnselect: clearSelection,
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),  
      ),
    );
  }
}

