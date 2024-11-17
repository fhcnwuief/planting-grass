import java.util.*;
import java.lang.*;
import java.io.*;
import java.util.Stack;

// The main method must be in a class named "Main".

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        Stack<Integer> stack = new Stack<>();//push, pop, peek, empty, seach 지원
        stack.push(0);
        for(int k = 0; k < moves.length;k++){
            int n = moves[k] - 1;
             for(int i = 0; i < board.length;i++){
                 if(board[i][n] != 0){
                     if(!stack.empty() && stack.peek() == board[i][n]){
                         answer++;
                         stack.pop();
                         board[i][n] = 0;
                         break;
                     }
                     else{
                         stack.push(board[i][n]);
                         board[i][n] = 0;
                         break;
                     }
                 }
            }
        }
        return answer * 2;
    }
}