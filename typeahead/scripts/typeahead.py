import sys
import logging
import time
from typeahead.cli import parse
from typeahead.data_loader import get_contents
from typeahead.trie import build_trie


def main():
    logging.basicConfig(level=logging.INFO)
    try:
        args = parse()
        contents = get_contents(args.data_path)
        start_time = int(round(time.time() * 1000))
        trie = build_trie(contents)
        end_time = int(round(time.time() * 1000))
        print(start_time, end_time)
        print(f"Elapsed time for laod data"
              f"and build trie: {(end_time-start_time)}ms")
        while True:
            sentence = input("Please enter word to search or CTRL+C for exit\n")
            start_time = time.time_ns()
            found_items = trie.prefix_search(sentence)
            print(f"Found items: {found_items}")
            end_time = time.time_ns()
            print(f"Elapsed time for search: {end_time - start_time}ns")

    except Exception as ex:
        logging.error(ex)
        sys.exit(1)
