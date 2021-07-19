import argparse

parser = argparse.ArgumentParser()
parser.add_argument('url', help="Specify the URL")
args = parser.parse_args()

web_url = args.url
