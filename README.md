# PDF Processing and Summarization System

# Concept used in Stealth Startup

# Summarized text: summary_drylab_20250112_162647.txt
This project implements a PDF processing system that extracts text, creates vector embeddings, and generates summaries using modern NLP techniques.

## Tech Stack

- **Python 3.x**: Core programming language
- **PyPDF (pypdf)**: PDF text extraction
- **Sentence Transformers**: Vector embeddings generation
  - Using the 'all-MiniLM-L6-v2' model for efficient, high-quality embeddings
- **Transformers (Hugging Face)**: Text summarization
  - Using BART (facebook/bart-large-cnn) for generating summaries
- **ChromaDB**: Vector database for storing and managing embeddings
- **PyTorch**: Backend for transformer models

## Features

- PDF text extraction and processing
- Text chunking for handling large documents
- Vector embeddings generation and storage
- Automated text summarization
- Local processing without requiring external API calls
- Output summary generation with timestamps

## Project Structure

```
├── main.py              # Main execution script
├── pdf_processor.py     # PDF handling and text extraction
├── embedding_manager.py # Vector embeddings management
├── summarizer.py        # Text summarization
└── config.py           # Configuration settings
```

## Installation

1. Clone the repository:
```bash
git clone [your-repo-url]
cd [repo-name]
```

2. Install required packages:
```bash
pip install transformers torch sentence-transformers pypdf chromadb
```

## Usage

1. Place your PDF file in the project directory

2. Run the main script:
```bash
python main.py
```

3. The system will:
   - Extract text from the PDF
   - Split text into manageable chunks
   - Generate and store embeddings
   - Create a summary
   - Save the summary to a timestamped text file

## Output

The system generates two types of output:
1. A timestamped summary file: `summary_[filename]_[timestamp].txt`
2. Console logs showing processing progress

## Technical Details

### Text Processing
- Uses PyPDF for robust PDF text extraction
- Implements chunk-based processing for handling large documents
- Configurable chunk size and overlap

### Embeddings
- Utilizes Sentence Transformers for generating text embeddings
- Stores embeddings in ChromaDB for potential future use
- Efficient vector representation of text content

### Summarization
- Employs BART model for text summarization
- Handles long texts through intelligent chunking
- Produces coherent, contextual summaries

## Future Improvements

- Add support for multiple document formats
- Implement similarity search using stored embeddings
- Add customizable summarization parameters
- Implement batch processing for multiple documents

## Contributing

Feel free to open issues or submit pull requests for improvements.

## License

[Your chosen license]
