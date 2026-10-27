class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # [n(0), n(1), ..., **n(k)**, n(k+1), ..., n(_len-1)]
        # n(k) number of visits is required
        # min(n(0), n(k)) + min(n(1), n(k)) + ... + min(n(k-1), n(k))
        #    + n(k)
        #    + min((n(k)-1), n(k+1)) + min((n(k)-1), n(k+2)) + ...

        n_k = tickets[k]
        val = [(min(n_k, v) if (i < k) else (min(n_k-1, v) if i > k else n_k)) for i, v in enumerate(tickets)]
        return sum(val)