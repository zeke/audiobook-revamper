import replicate
import re

def remove_duplicate_spaces_and_tabs(text) -> str:
    # Replace tabs with nothing
    text_no_tabs = text.replace('\t', '')
    
    # Replace multiple spaces with a single space
    text_clean = re.sub(' +', ' ', text_no_tabs)

    return text_clean

def shorten(input_text):
    """Shortens text to 300 words or less, while preserving the overall meaning and the most important points"""

    prompt= f"""Shorten the following text to 300 words or less, while preserving the overall meaning and the most important points:\n\n{input_text}"""
    prompt = remove_duplicate_spaces_and_tabs(prompt)

    model = "mistralai/mixtral-8x7b-instruct-v0.1"
    # model = "meta/llama-2-70b-chat"

    output = replicate.run(
        model,
        input={
            "prompt": prompt
        }
    )

    # print("type of output: ", type(output))
    # print("output: ", output)

    output = "".join(output)

    return remove_extra_whitespace(output)

def remove_extra_whitespace(text):
    return re.sub(r'\s+', ' ', text).strip()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename, "r") as input_file:
            print(shorten(input_file.read()))
    else:
        print("File name missing, must have file name passed as argument")