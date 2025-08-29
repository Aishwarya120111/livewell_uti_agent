# AI UTI Treatment Agent

A prototype AI agent for treating urinary tract infections (UTIs) through a CLI interface.

## Setup

1. Get OpenAI API Key

-  Go to [OpenAI Platform](https://platform.openai.com/api-keys)
-  Sign up or log in to your account
-  Create a new API key
-  Copy the key (it starts with `sk-`)

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set Up API Key:

-  Create a file named `.env` in the project root
-  Add your API key:
```
OPENAI_API_KEY=your-api-key-here
```

4. Run the rule-based version:
```bash
python main.py
```


## Usage

The agent will guide you through a series of questions about:
- UTI symptoms
- Medical history
- Allergies and medications
- Risk factors

Based on your responses, it will either:
- Recommend treatment if safe and appropriate
- Refer you to a doctor if needed

