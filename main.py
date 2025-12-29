# main.py

import os
from PyPDF2 import PdfFileMerger, PdfFileReader
import argparse

def merge_pdfs(pdf_files, output_file):
    """
    Merge a list of PDF files into a single PDF file.

    Args:
        pdf_files (list): List of paths to PDF files to merge.
        output_file (str): Path to the output PDF file.

    Raises:
        Exception: If an error occurs during the merging process.
    """
    try:
        # Create a PdfFileMerger object
        merger = PdfFileMerger()

        # Append each PDF file to the merger
        for pdf_file in pdf_files:
            # Check if the PDF file exists
            if not os.path.exists(pdf_file):
                raise FileNotFoundError(f"PDF file '{pdf_file}' not found.")

            # Check if the PDF file is valid
            try:
                PdfFileReader(pdf_file)
            except Exception as e:
                raise Exception(f"Invalid PDF file '{pdf_file}': {str(e)}")

            # Append the PDF file to the merger
            merger.append(pdf_file)

        # Write the merged PDF to the output file
        with open(output_file, 'wb') as f:
            merger.write(f)

    except Exception as e:
        raise Exception(f"Error merging PDF files: {str(e)}")

def parse_args():
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description='Merge PDF files.')
    parser.add_argument('pdf_files', nargs='+', help='PDF files to merge.')
    parser.add_argument('-o', '--output', default='output.pdf', help='Output PDF file.')
    return parser.parse_args()

def main():
    """
    Main entry point.
    """
    args = parse_args()
    try:
        merge_pdfs(args.pdf_files, args.output)
        print(f"PDF files merged successfully. Output file: {args.output}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    main()