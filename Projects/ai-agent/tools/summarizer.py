def summarize(text):

    sentences = text.split(".")

    summary = " ".join(sentences[:2])

    return summary.strip()