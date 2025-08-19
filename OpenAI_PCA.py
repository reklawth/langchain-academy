from openai import OpenAI

client = OpenAI(
      
)

response = client.responses.create(
  model="gpt-4o-mini",
  input="Perform Principal Component Analysis on the four largest equities in the XLF",
  store=True,
)

print(response.output_text);