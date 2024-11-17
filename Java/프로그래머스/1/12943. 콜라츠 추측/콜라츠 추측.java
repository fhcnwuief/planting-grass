class Solution {
    public int solution(long n){
        //int n으로 하면 오버플로우 발생 >>test3 통과 안됨 >> long n으로 변경
        int answer = 0;
        while(n!=1){
            if(n%2==0){ n /= 2; }
            else{ n = n * 3 + 1; }
            answer++;

            if(answer >=500){ return -1; }
        }
        
        return answer ;
    }
}