class Solution {
    public int[] solution(int n, int m) {
        int[] answer = {1,1};
        int[] origin = {n,m};
//      int max = n;
//      if (max < m) {max = m;}
        int max = Math.max(n,m);
        
        
        //최대공약수
        for(int i = 1; i <= max;i++ ){
            if(n%i == 0 && m%i == 0){
                answer[0] = i;
            }
        }
        
        //최소공배수
        answer[1] = (origin[0] * origin[1]) / answer[0];
        return answer;
    }
}