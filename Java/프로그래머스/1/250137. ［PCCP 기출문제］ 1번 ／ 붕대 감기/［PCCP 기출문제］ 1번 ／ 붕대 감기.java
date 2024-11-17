class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        
        // index checking
        int idx = 0;
        // bandage success count
        int cnt = 0;
        // max stamina
        int MAX = health;
        // last attack time
        int last = attacks[(attacks.length)-1][0];
        for(int i = 0;i <= last;i++){
            // monster attack success
            if (attacks[idx][0] == i){
                health -= attacks[idx][1];
                idx++;
                cnt = 0;
                if(health <= 0) return -1;
            }
            //monser attack fails
            else{
                //recover health
                cnt++;
                health += bandage[1];
                if(cnt == bandage[0]){
                    health += bandage[2];
                    cnt = 0;
                }
                // health cannot get bigger than max
                if(health >= MAX){ health = MAX; }
            }
        }
        return health ;
    }
}