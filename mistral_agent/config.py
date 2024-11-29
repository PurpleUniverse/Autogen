# Setting up Mistral API
config_list =  [
    {
        'model': 'open-mistral-7b',
        'api_key' : '', #INSERT YOUR API KEY!!
        'api_type': 'mistral'
    }
]

# Setting up API parameters for Mistral
llm_config = {
    "seed": 42,
    "config_list": config_list,
    "temperature": 0.5, # How creative the AI is in response
    "max_tokens": 10000,
    "safe_prompt": False,
}