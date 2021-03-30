from jsgf import parse_grammar_string

def main(args):
    # Parse input grammar file.
    with open(args.input_file_path, "r") as fp:
        text = fp.read()
        print("\ninput grammar: ")
        print(text)
        grammar = parse_grammar_string(text)

    # Print it.
    print("\noutput grammar: ")
    text = grammar.compile()
    print(text)
    with open(args.output_file_path, "w") as fp:
        fp.write(text)


if __name__ == '__main__':
    import argparse
    
    """Prepares arguments for the demo"""
    # Usage: python jsgf_tags.py test.jsgf out.jsgf 
    parser = argparse.ArgumentParser(description='expand JSGF grammar tags.') 
    parser.add_argument('input_file_path', type=str, help='Input JSGF grammar file path.')
    parser.add_argument('output_file_path', type=str, help='Output file path.')
    

    args = parser.parse_args()
    main(args)
