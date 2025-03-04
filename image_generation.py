from openai import OpenAI
import user_config

client = OpenAI(api_key=user_config.openai_key)

response = client.images.generate(
    model = "dall-e-2",
    prompt="doraemon and nobita",
    n=1,
    size="1024x1024",
    quality="standard",
)

print(response.data[0].url)