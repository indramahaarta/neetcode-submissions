class Twitter:

    def __init__(self):
        self.FollowMap = defaultdict(set)
        self.TwitMap = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.TwitMap[userId].append((self.count, tweetId))
        self.count -= 1

        # print("postTweet", self.TwitMap[userId])

    def getNewsFeed(self, userId: int) -> List[int]:
        followers = list(self.FollowMap[userId])
        followers.append(userId)

        maxHeap = [] #contains twit record 
        for i in followers:
            index = len(self.TwitMap[i]) - 1
            if index >= 0:
                count, tweetId = self.TwitMap[i][index]
                maxHeap.append((count, tweetId, i, index-1))
        
        heapq.heapify(maxHeap)

        res = []
        while maxHeap and len(res) < 10:
            count, tweetId, userId, index = heapq.heappop(maxHeap)
            res.append(tweetId)
            if index >= 0:
                nextCount, nextTweetId = self.TwitMap[userId][index]
                heapq.heappush(maxHeap, (nextCount, nextTweetId, userId, index-1))


        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.FollowMap[followerId].add(followeeId)
        # print("follow", self.FollowMap[followerId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.FollowMap[followerId].discard(followeeId)
        # print("unfollow", self.FollowMap[followerId])
        
