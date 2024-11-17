class Solution{
    public long solution(int a, int b){
        long number = 0;
        if (a==b) return a;
        else if (a<b){
            for(int i = a;i <= b;i++){
                number += i;
            }
        }
        else{
            for(int i = b;i <= a;i++){
                number += i;
            }
        }
        return number;
    }
}