class Solution {
    public int solution(String dartResult) {
        int answer = 0;
        //다트를 3번 던진다 했으니까
        int[] dart = new int[3];
        //인덱스 값 활용
        int idx = 0;
        String num = "";
        int calc = 0;
        
        for(int i = 0;i<dartResult.length();i++){
            char c = dartResult.charAt(i);
            
            //숫자 입력 처리
            if(c >= '0' && c <= '9'){
                // 우선 문자로 숫자 저장
                num += String.valueOf(c);
            }
                
            //영어 입력 처리
            else if (c=='S'||c=='D'||c=='T'){

                //저장된 문자를 숫자로 다시 바꾸기(계산해야 되니깐)
                calc = Integer.parseInt(num);
                if (c=='S'){
                    dart[idx] = (int)Math.pow(calc,1);
                }
                else if (c=='D'){
                    dart[idx] = (int)Math.pow(calc,2);
                }
                else{
                    dart[idx] = (int)Math.pow(calc,3);
                }
                idx++;
                num = "";
                calc = 0;
            }
                
            //옵션 입력 처리
            else {
                if (c =='*'){
                    dart[idx-1]*= 2;
                    if(idx-2>=0){
                        dart[idx-2]*=2;
                    }
                }
                else if (c == '#'){
                    dart[idx-1]*= (-1);
                }
            }
        }
        answer = dart[0] + dart[1] + dart[2];
        return answer;
    }
}