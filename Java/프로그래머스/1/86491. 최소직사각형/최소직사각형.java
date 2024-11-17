class Solution {
    public int solution(int[][] sizes) {
        
        for(int i = 0; i < sizes.length; i++){
            int tmp = 0;
            //가로 세로 중에 긴거 한쪽으로 몰기(?)
            //가로 > 세로 -> 위치 바꾸기
            if(sizes[i][0] > sizes[i][1]){
                tmp = sizes[i][0];
                sizes[i][0] = sizes[i][1];
                sizes[i][1] = tmp;
            }
        }
        
        int wmax = 0;
        int hmax = 0;
        for(int i = 0; i < sizes.length; i++){
            wmax = Math.max(sizes[i][0],wmax);
            hmax = Math.max(sizes[i][1],hmax);
        }
            
        return wmax * hmax;
    }
}