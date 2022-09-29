import java.util.Arrays;

class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        int N = intervals.length;
        Arrays.sort(intervals, (int1, int2) -> int1[1] - int2[1]);
        int count = 1, prevEnd = intervals[0][1];
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] >= prevEnd) {
                prevEnd = intervals[i][1];
                count += 1;
            }
        }
        return N - count;
    }
    public static void main(String[] args) {
        
    }
}