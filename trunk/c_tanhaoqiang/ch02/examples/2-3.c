/*
 * P 17
 * 判断2000到2500年中的每一年是否是闰年，将结果输出
 * */
void main(){
    int year;
    for(year=2000;year<=2500;year++){
        if (isLeapYear(year)){
            printf("%d年是闰年\n",year);
        }
        else
            printf("%d年不是闰年\n",year);
    }
}
int isLeapYear(int year){
    int flag=0;
    if ((year%4==0&&year%100!=0)||(year%100==0&&year%400==0())){
        flag=1;
    }
    return flag;
}
