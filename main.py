from src.chains import Chain
import os
import logging
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def read_txt_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            contents = file.read()
        word_count = len(contents.split())
        logging.info(f"Loaded file: {file_path} with word count: {word_count}")
        return contents
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return "File not found."
    except Exception as e:
        logging.error(f"An error occurred while reading {file_path}: {e}")
        return f"An error occurred: {e}"


def main():
    chain = Chain()
    transcript = read_txt_file(r"data/transcript_raw.txt")
    # print(chain.diarization(transcript))
    print(chain.notes(transcript))

if __name__ == "__main__":
    main()