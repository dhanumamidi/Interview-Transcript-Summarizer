import argparse
import openai
import re

default_stop = "<<END>>"
max_chunk_size = 10000


def read_file(path):
    with open(path, "r") as f:
        return f.read()


def write_file(path, text):
    with open(path, "w") as f:
        f.write(text)


# Split transcript into chunks of around 6000 characters without splitting a dialogue
def create_chunks(transcript):
    dialogues = re.findall(r'([A-Za-z]+: ".*?")(?:\s|$)', transcript)
    chunks = []
    chunk = ""
    for dialogue in dialogues:
        chunk += dialogue
        if len(chunk) > max_chunk_size:
            chunks.append(chunk)
            chunk = ""
    return chunks


def gpt_summarize(prompt, engine="text-davinci-003", temperature=0.5, max_tokens=600, top_p=1, frequency_penalty=0, presence_penalty=0, stop=["<<END>>"], best_of=1):
    try:
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            best_of=best_of,
            stop=stop,
        )
        return response.choices[0].text
    except Exception as e:
        print(f"Error: {str(e)}")
        raise e


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Summarize an interview transcript using GPT-3")
    parser.add_argument("input_file", type=str, help="Path to input text file")
    parser.add_argument("output_file", type=str, help="Path to output text file")
    parser.add_argument(
        "--prompt", type=str, default="Summarize an interview transcript using GPT-3 by preserving all the statistical and important information", help="Prompt to use for summarization"
    )
    parser.add_argument("--length", type=int, default=600, help="Maximum length of summary")
    args = parser.parse_args()

    input_transcript = read_file(args.input_file)
    output_summary = ""
    chunks = create_chunks(input_transcript)
    try:
        for chunk in chunks:
            prompt = args.prompt + "\n" + chunk + "\n" + default_stop
            output_summary += gpt_summarize(prompt, max_tokens=1000).strip()  # Summarizing each chunk separately to get a initial moderate summary of the transcript

        write_file("detailed_" + args.output_file, output_summary)

        # Summarizing all the chuck summaries together to get a more concise summary
        prompt = "write very detailed summary of the below text by preserving all the statistical and important information: \n" + output_summary + "\n" + default_stop
        output_summary = gpt_summarize(prompt, max_tokens=args.length, best_of=3, temperature=0.4)
        output_summary = output_summary.strip()
        output_summary = output_summary.replace("\n", " ")
        write_file(args.output_file, output_summary)
    except Exception as e:
        print(f"Error: {str(e)}")
        raise e
