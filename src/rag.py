import os

def ingest_pdf_to_memory(file_path: str):
    """
    Temporary placeholder for PDF ingestion.
    Replace later with real RAG pipeline.
    """
    if not os.path.exists(file_path):
        return "File not found."

    return f"PDF '{os.path.basename(file_path)}' ingested successfully!"
