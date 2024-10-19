import openai

openai.api_key = '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'

# List all models available for your API key
models = openai.Model.list()

# Print model IDs to see which ones you have access to
for model in models['data']:
    print(model['id'])
