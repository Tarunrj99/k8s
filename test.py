import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--input_file", required=True, help="Input file")
    parser.add_argument("-o", "--output_file", required=True, help="Output file")
    args = parser.parse_args()

    with open(args.input_file, "r") as input_file:
        content = input_file.read()

    with open(args.output_file, "w") as output_file:
        output_file.write(content)

if __name__ == "__main__":
    main()
