/*
 * =====================================================================================
 *
 *       Filename:  fig01_06.cpp
 *
 *    Description:  输入流对象 std::cin以及流提取操作符>>，获取用户通过键盘输入的两个整数，计算这两个值的和，再用std::cout输出结果。
 *
 *        Version:  1.0
 *        Created:  2010年03月21日 19时51分53秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *        Company:  
 *
 * =====================================================================================
 */

#include <iostream>
int main() {
    int integer1, integer2, sum; // 声明变量
    std::cout << "输入第一个整数:\n";
    std::cin >> integer1; // 用输入流对象cin(属于std这个名称空间)以及流提取操作符>>，以便从键盘取得值。
    std::cout << "输入第二个整数:\n";
    std::cin >> integer2;
    sum = integer1 + integer2;
    std::cout << "和为：" << sum << std:: endl;
    return 0;
}
