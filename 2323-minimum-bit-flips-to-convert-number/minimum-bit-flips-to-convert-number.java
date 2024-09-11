class Solution {
    public int minBitFlips(int start, int goal) {
        int steps = 0;
        while (start > 0 || goal > 0) {
            if (start % 2 != goal % 2) {
                steps += 1;
            }
            start = start / 2;
            goal = goal / 2;
        }
        return steps;
    }
}
