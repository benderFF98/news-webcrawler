import argparse
from crawler_functions import tabnews


def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Crawl articles and save to API")

    # Add arguments to specify which function to run
    parser.add_argument('--tabnews', action='store_true', help='Crawl articles')

    # Parse the command-line arguments
    args = parser.parse_args()

    if args.tabnews:
        tabnews()  # Call the crawl_articles function from crawler_functions
    # elif args.save:
    #     another_crawler()
    else:
        print("Please specify a function to run. Use --tabnews or --save.")


if __name__ == "__main__":
    main()
