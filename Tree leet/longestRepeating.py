class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        n = len(s)
        # Tree node structure: [lc, rc, p_len, s_len, max_len]
        tree = [None] * (4 * n)

        def merge(left, right, l_len, r_len):
            lc, l_rc, l_p, l_s, l_max = left
            r_lc, rc, r_p, r_s, r_max = right

            # Base merge max
            new_max = max(l_max, r_max)

            # Check if boundary characters match
            if l_rc == r_lc:
                new_max = max(new_max, l_s + r_p)

            # Calculate new prefix length
            p_len = l_p + r_p if (l_p == l_len and l_rc == r_lc) else l_p

            # Calculate new suffix length
            s_len = r_s + l_s if (r_s == r_len and l_rc == r_lc) else r_s

            return [lc, rc, p_len, s_len, new_max]

        def build(node, start, end):
            if start == end:
                char = s[start]
                tree[node] = [char, char, 1, 1, 1]
                return
            
            mid = (start + end) // 2
            build(node * 2, start, mid)
            build(node * 2 + 1, mid + 1, end)
            
            tree[node] = merge(
                tree[node * 2], tree[node * 2 + 1],
                mid - start + 1, end - mid
            )

        def update(node, start, end, idx, char):
            if start == end:
                tree[node] = [char, char, 1, 1, 1]
                return

            mid = (start + end) // 2
            if idx <= mid:
                update(node * 2, start, mid, idx, char)
            else:
                update(node * 2 + 1, mid + 1, end, idx, char)

            tree[node] = merge(
                tree[node * 2], tree[node * 2 + 1],
                mid - start + 1, end - mid
            )

        # Build initial tree
        build(1, 0, n - 1)

        result = []
        for char, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, char)
            # The root node (node 1) holds the answer for the entire string
            result.append(tree[1][4])

        return result
