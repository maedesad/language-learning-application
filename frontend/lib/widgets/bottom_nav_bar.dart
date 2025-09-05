import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:flutter_svg/flutter_svg.dart';
import '../theme/base_background_theme.dart';

// colors
import '../theme/colors/semantic_colors.dart';
// dimensions
import '../theme/dimensions.dart';

// Pages
import '../main_pages/home/home.dart';
import '../main_pages/learning_path/learning_path.dart';
import '../main_pages/library/library.dart';
import '../main_pages/practice/practice.dart';
import '../main_pages/planning/planning.dart';
import '../main_pages/setting/setting.dart';
import '../main_pages/profile/profile.dart';

class BottomNavBar extends StatefulWidget {
  const BottomNavBar({super.key});

  @override
  State<BottomNavBar> createState() => _BottomNavBarState();
}

class _BottomNavBarState extends State<BottomNavBar> {
  int _selectedIndex = 0;

  final List<Widget> _pages = const [
    HomePage(),
    LearningPathPage(),
    LibraryPage(),
    PracticingPage(),
    PlanningPage(),
    SettingPage(),
    ProfilePage(),
  ];

  /// Icon paths (unpressed, pressed)
  final List<List<String>> _icons = [
    ["assets/bottom_nav_bar_icons/door_unpressed.svg", "assets/bottom_nav_bar_icons/door_pressed.svg"],
    ["assets/bottom_nav_bar_icons/learning_path_unpressed.svg", "assets/bottom_nav_bar_icons/learning_path_pressed.svg"],
    ["assets/bottom_nav_bar_icons/library_unpressed.svg", "assets/bottom_nav_bar_icons/library_pressed.svg"],
    ["assets/bottom_nav_bar_icons/practicing_unpressed.svg", "assets/bottom_nav_bar_icons/practicing_pressed.svg"],
    ["assets/bottom_nav_bar_icons/planning_unpressed.svg", "assets/bottom_nav_bar_icons/planning_pressed.svg"],
    ["assets/bottom_nav_bar_icons/setting_unpressed.svg", "assets/bottom_nav_bar_icons/setting_pressed.svg"],
    ["assets/bottom_nav_bar_icons/profile_unpressed.svg", "assets/bottom_nav_bar_icons/profile_pressed.svg"],
  ];

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

   @override
    Widget build(BuildContext context) {
      return BaseBackground(
        child: Scaffold(
          backgroundColor: Colors.transparent, // بک‌گراند از BaseBackground بیفته
          body: _pages[_selectedIndex],
          bottomNavigationBar: _buildBottomBar(),
        ),
      );
    }

    Widget _buildBottomBar() {
      return Container(
        height: 70.h + 28.h, // main hight + bottom paading
        width: Dimensions.screenWidth,
        decoration: BoxDecoration(
          color: SemanticColors.surface,
          border: Border(
            top: BorderSide(
              color: SemanticColors.border,
              width: Dimensions.bottomNavBarBorder,
            ),
          ),
        ),
        child: Padding(
          padding: EdgeInsets.only(bottom: 28.h), // bottom padding
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: List.generate(_icons.length, (index) {
              final isSelected = _selectedIndex == index;
              final iconPath = isSelected ? _icons[index][1] : _icons[index][0];

              // resize
              Size size = const Size(55, 55);
              if (!isSelected) {
                size = index == 0 ? const Size(26, 36) : const Size(36, 36);
              }

              return GestureDetector(
                onTap: () => _onItemTapped(index),
                child: AnimatedContainer(
                  duration: const Duration(milliseconds: 300), // زمان انیمیشن
                  curve: Curves.easeOutBack, // نوع منحنی حرکت (حس بازی گونه و طبیعی)
                  height: size.height.h,
                  width: size.width.w,
                  child: Center(
                    child: SvgPicture.asset(
                      iconPath,
                      width: size.width.w,
                      height: size.height.h,
                    ),
                  ),
                ),
              );
            }),
          ),
        ),
      );      
  }
}



