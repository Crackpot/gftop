/*
 * =====================================================================================
 *
 *       Filename:  fig01_14.cpp
 *
 *    Description:  用6个if结构比较用户输入的两个数字。只要满足任何一个if结构的条件，便会执行与if对应的输出语句。
 *
 *        Version:  1.0
 *        Created:  2010年03月21日 20时01分07秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *        Company:  
 *
 * =====================================================================================
 */

#include <iostream>

using std::cout; //using语句帮助我们避免重复std::前缀。一旦我们包含了这些using语句，那么可分别直接写cout，不用写std::cout；直接写cin，不用写std::cin；直接写endl，而不用写std::endl。
using std::cin;
using std::endl;

int main() {
    int num1, num2;
    cout << "输入两个整数，将显示出"
        << "它们所满足的情况:\n";
    cin >> num1 >> num2;
    if (num1 == num2)
        cout << num1 << "等于" << num2 << endl;

    if (num1 != num2)
        cout << num1 << "不等于" << num2 << endl;

    if (num1 < num2)
        cout << num1 << "小于" << num2 << endl;

    if (num1 > num2)
        cout << num1 << "大于" << num2 << endl;

    if (num1 <= num2)
        cout << num1 << "小于等于" << num2 << endl;

    if (num1 >= num2)
        cout << num1 << "大于等于" << num2 << endl;

    return 0;
}
