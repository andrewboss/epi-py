from typing import List


def compute_h_index_v1(citations: List[int]) -> int:
    """
    Time complexity: O(n^2) - not acceptable!
    Space complexity: O(n)
    :param citations: list of citations of each paper
    :return: computed h-index
    """
    h = 0
    for c1 in citations:
        paper_count = 0
        for c2 in citations:
            if c2 - c1 >= 0:
                paper_count += 1
            else:
                continue
            if paper_count >= c1:
                h = paper_count if paper_count > h else h
                break

    return h


h = compute_h_index_v1(
    citations=[1, 4, 1, 4, 2, 1, 3, 5, 6]
)

print(h)
