/*
 * P 16
 * 求1到11之间的奇数乘积
 * */
void main(){
    int a=1,i;
    for (i=1;i<11;i+=2){
        a*=i;
    }
    printf("for循环求得1到11之间的奇数乘积为：%d\n",a);
    while(i<11){
        a*=i;
        i+=2;
    }
    printf("while循环求得1到11之间的奇数乘积为：%d\n",a);
}
