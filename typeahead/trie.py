from collections import deque


class TrieNode:
    def __init__(self, value='') -> None:
        self.children = {}
        self.end_word = False
        self.value = value


class Trie:
    def __init__(self) -> None:
        self.count_words = 0
        self.root = TrieNode()

    def insert(self, word):
        word = word.strip()
        self.count_words += 1
        crawl = self.root
        for c in word:
            if c not in crawl.children:
                crawl.children[c] = TrieNode(c)
            crawl = crawl.children[c]

        crawl.end_word = True

    def search(self, query):
        crawl = self.root
        for char in query:
            if char not in crawl.children:
                return False

            crawl = crawl.children[char]
        return crawl.end_word

    def collect_suffix(self, node, size, prefix):
        sequence = deque([(node, '')])
        results = []
        ignored_root = False
        while sequence:
            current_node, chars = sequence.popleft()
            if ignored_root:
                chars += current_node.value

            ignored_root = True
            if current_node.end_word:
                results.append(prefix + chars)

                if len(results) == size:
                    break

            for char in sorted(current_node.children.keys()):
                next_node = current_node.children[char]
                sequence.append((next_node, chars))

        return results

    def prefix_search(self, query, limit=10):
        crawl = self.root
        for c in query:
            if c not in crawl.children:
                return []
            crawl = crawl.children[c]

        return self.collect_suffix(crawl, limit, query)

    def __str__(self) -> str:
        return f"Count words: {self.count_words}"


def build_trie(contents):
    trie = Trie()
    for row in contents:
        trie.insert(row)

    return trie
