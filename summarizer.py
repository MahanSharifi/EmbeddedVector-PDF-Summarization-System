# summarizer.py
from transformers import pipeline
import torch

class Summarizer:
    def __init__(self, api_key=None):
        self.summarizer = pipeline(
            "summarization",
            model="facebook/bart-large-cnn",
            device=-1  # Use CPU
        )
        self.max_length = 1024
        self.min_length = 40

    def summarize(self, texts):
        """Generate summary using BART model with chunk handling"""
        # Combine all texts
        combined_text = " ".join(texts)
        
        # Split into smaller chunks if needed
        max_chunk_length = 1000  # BART's limit is around 1024 tokens
        chunks = []
        current_chunk = ""
        
        for sentence in combined_text.split(". "):
            if len(current_chunk) + len(sentence) < max_chunk_length:
                current_chunk += sentence + ". "
            else:
                chunks.append(current_chunk)
                current_chunk = sentence + ". "
        if current_chunk:
            chunks.append(current_chunk)

        # Summarize each chunk
        summaries = []
        for chunk in chunks:
            try:
                summary = self.summarizer(
                    chunk,
                    max_length=self.max_length // 2,
                    min_length=self.min_length,
                    do_sample=False,
                    truncation=True
                )[0]['summary_text']
                summaries.append(summary)
            except Exception as e:
                print(f"Warning: Error summarizing chunk: {e}")
                continue

        # Combine summaries
        final_summary = " ".join(summaries)
        
        return final_summary