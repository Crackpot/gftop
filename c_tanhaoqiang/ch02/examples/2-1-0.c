/*
 * 求1到5的乘积
 * P 15
 * */
void main(){
    int a=1,i;
    for(i=1;i<=5;i++){
        a*=i;
    }
    printf("for循环求得5的阶乘为：%d\n",a);
    while(i<6){
        a*=i;
        i++;
    }
    printf("while循环求得5的阶乘为：%d\n",a);
}
