from openai import OpenAI

client = OpenAI(
    api_key="sk-xt-010efc9fc777be9cfdf23279b80e09f428d2d88a4fbaafd5",
    base_url="https://api.xkiro.com/v1",
)

print(client.chat.completions.create(
    model="qwen/qwen3.8-max:free",
    messages=[{"role": "user", "content": "Hello"}],
).choices[0].message.content)
