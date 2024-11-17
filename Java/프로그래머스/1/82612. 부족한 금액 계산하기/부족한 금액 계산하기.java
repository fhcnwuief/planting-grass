class Solution {
    public long solution(int price, int money, int count) {
        long calc = 0;
        for(int i = 1; i <= count ; i++) { calc += price * i ; }
        return calc <= money ? 0 : calc - money ;
    }
}