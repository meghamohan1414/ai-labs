def normalize_texts(texts: list[str]) -> list[str]:
    # list comprehension to normalize text by converting to lowercase and stripping whitespace
    return [text.strip().lower() for text in texts if text and text.strip()]


def word_counts(texts: list[str]) -> dict[str, int]:
    # dictionary comprehension to count the occurrences of each word in the list of texts
    counts: dict[str, int] = {}
    for text in normalize_texts(texts):
        for word in text.split():
            counts[word] = counts.get(word, 0) + 1
    return counts


if __name__ == "__main__":
    texts = ["Hello World", "hello", "AI Labs", "", "   ", "AI"]
    print("Normalized Texts:", normalize_texts(texts))
    print("Word Counts:", word_counts(texts))
