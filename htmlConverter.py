if __name__ == "__main__":
    import sys
    import markdown

    command = sys.argv[1]
    inputfile = sys.argv[2]
    outputfile = sys.argv[3]

    if command == "markdown":
        with open(inputfile, "r",encoding="utf-8_sig") as inputfile:
            with open(outputfile, "w") as outputfile:
                outputfile.write(markdown.markdown(inputfile.read()))
    else:
        print("error")
