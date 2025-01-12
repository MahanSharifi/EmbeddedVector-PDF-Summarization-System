# main.py
from config import CHUNK_SIZE, CHUNK_OVERLAP
from pdf_processor import PDFProcessor
from embedding_manager import EmbeddingManager
from summarizer import Summarizer
import os
from datetime import datetime

def process_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    processor = PDFProcessor(CHUNK_SIZE, CHUNK_OVERLAP)
    embedding_manager = EmbeddingManager()
    summarizer = Summarizer()
    
    print(f"Processing PDF: {pdf_path}")
    print("Extracting text from PDF...")
    text = processor.extract_text(pdf_path)
    print(f"Extracted {len(text)} characters")
    
    print("Splitting text into chunks...")
    chunks = processor.split_text(text)
    print(f"Created {len(chunks)} chunks")
    
    print("Creating embeddings and storing in database...")
    collection = embedding_manager.create_collection()
    embeddings = embedding_manager.add_documents(collection, chunks)
    print(f"Created {len(embeddings)} embeddings")
    
    print("Generating summary...")
    summary = summarizer.summarize(chunks)
    
    # Generate output filename using the input PDF name and timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_filename = f"summary_{pdf_name}_{timestamp}.txt"
    
    # Write summary to file
    with open(output_filename, 'w') as f:
        f.write(f"Summary of {pdf_path}\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("-" * 50 + "\n\n")
        f.write(summary)
        
    print(f"\nSummary has been saved to: {output_filename}")
    return summary

if __name__ == "__main__":
    pdf_path = "drylab.pdf"  # Change this to your PDF filename
    try:
        summary = process_pdf(pdf_path)
        print("\nSummary:")
        print(summary)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        import traceback
        print(traceback.format_exc())