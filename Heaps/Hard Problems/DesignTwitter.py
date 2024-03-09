'''

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. 
Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
 

Example 1:

Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]

Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.


Intuition
To design a simplified version of Twitter, we need to efficiently handle posting tweets, following/unfollowing users, and retrieving recent tweets in a user's news feed. 
We can achieve this by maintaining data structures to store tweets, user relationships, and a global counter to track tweet timestamps.

Approach

Initialization:
Initialize a global counter to track tweet timestamps. Initialize tweetMap to store user tweets and followMap to store user relationships.

Post Tweet:
Implement postTweet to allow users to compose new tweets. Each tweet is associated with a unique tweetId and is appended to the tweetMap with the userId as the key.

Get News Feed:
Implement getNewsFeed to retrieve the 10 most recent tweet IDs in the user's news feed.
Maintain a min heap to store the most recent tweets from users followed by the given userId.
Iterate over users followed by the given userId and push their most recent tweets onto the min heap.
Pop tweets from the min heap, append them to the result list, and push the next tweet from the same user onto the heap until 10 tweets are collected or the heap is empty.

Follow/Unfollow:
Implement follow and unfollow to allow users to follow or unfollow other users.
Maintain followMap to store user relationships. Users are represented as keys, and the set of users they follow is stored as values.

Complexity
Time complexity:
  Posting a tweet: O(1)
  Retrieving news feed: O(n log m), where n is the number of users followed by the given user and m is the total number of tweets from those users.
  Following/unfollowing: O(1)

Space complexity:
  Storage for tweetMap and followMap: O(u + t), where u is the number of users and t is the total number of tweets.
  
'''


class Twitter:

    def __init__(self):
        # Count is to set most recent tweets, similar to time
        self.count = 0
        self.tweetMap = defaultdict(list)  # Stores count and tweet of the user
        self.followMap = defaultdict(set)  # Stores followeeId of the follower

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Add count and tweetId to user list
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1  # Decreasing the count to maintain most recent tweets - for Max Heap

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []  
        res = [] # 10 most recent tweets

        # Adding user to its follower list, as required for the problem
        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1  # Need to get tweets from back of the list to get most recent tweets
                count, tweet = self.tweetMap[followeeId][index]
                # Appending count, tweet, index and followeeId to res
                # FolloweeId is to get more tweets from that followee
                # Index - 1 is to go to previous index as we are traversing from back
                heap.append([count, tweet, followeeId, index - 1])
        
        # We need most recent so need to use maxHeap
        heapq.heapify(heap)

        while heap and len(res) < 10:
            count, tweet, followeeId, index = heapq.heappop(heap)
            res.append(tweet)

            if index >= 0:
                # Get the tweet from previous index of the followee and push it into heap
                count, tweet = self.tweetMap[followeeId][index]
                heapq.heappush(heap, [count, tweet, followeeId, index - 1])
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        # Add followeeId to followerId set
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # If followeeId is in followerId, remove it
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
