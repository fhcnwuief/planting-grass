class Solution{
    public long[] solution(int a, int b){
        long[] number = new long[b];
        number[0] = a;
        for(int i = 1 ;i < b;i++){
            number[i] = number[i-1] + a;
        }
        return number;
    }
}