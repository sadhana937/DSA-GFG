class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        meetings = list(zip(end, start))
        meetings.sort()
        output = 0
        prev_end = 0
        for end, start in meetings:
            if start > prev_end:
                output += 1
                prev_end = end
        return output
