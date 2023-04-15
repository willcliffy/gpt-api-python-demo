import time
import openai


def ask_gpt(
    prompt,
    engine="davinci",
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.7
):
    start = time.time()
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=max_tokens,
        n=n,
        stop=stop,
        temperature=temperature,
    )
    message = response.choices[0].text.strip()
    print(
        f"[SYS] Generated {len(response.choices)} completion in {round(time.time() - start, 2)}sec")
    return message


if __name__ == "__main__":
    import yaml

    with open(".env.yaml", "r") as env_file:
        env = yaml.safe_load(env_file)
        if "OPENAI_API_KEY" not in env:
            print("Must provide OPENAI_API_KEY")
            exit(1)
        openai.api_key = env["OPENAI_API_KEY"]

    while True:
        prompt = input("[YOU] ")
        if prompt.lower() == "exit":
            break
        response = ask_gpt(prompt)
        print("[GPT]" + response)
