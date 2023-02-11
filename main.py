# This is a very simple Python script I am writing to put as first version of my docker image of this app.
# If time permits, I will type the code given in the problem.
#def show_lines(n):
#  print("You have entered: ", n)
  
#if __name__ == "__main__":
#  def show_lines(4)
import os
import sys
import argparse
from lorem_text import lorem

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="FIle with lines generator")

        parser.add_argument('--lines_number', '-n', required=True, type=int, help="Number of lines to be generated")
        args = parser.parse_args()

        paragraph_length = args.lines_number
        paragraph = lorem.paragraphs(paragraph_length)

        with open(os.path.join('.', 'file_with_lines.txt'), 'w') as f:
          f.write(paragraph)
        print(paragraph)

    except Exception as exc:
        print(f"There was an expected behavior from user or application side. Error : '{exc}'")
        sys.exit(1)

    sys.exit(0)