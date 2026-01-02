# DeepEval Research - OWASP LLM Security Testing

Research project demonstrating AI security testing with DeepEval framework, focusing on OWASP LLM Top 10 vulnerabilities.

## Quick Start

```bash
# Clone repository
git clone https://github.com/codewithesc/deepeval.git
cd deepeval

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure API key
cp .env.example .env
# Edit .env and add: OPENAI_API_KEY=your-key-here

# Install package
pip install -e .
```

## Run Examples

```bash
# OWASP Security Tests (7 vulnerability categories)
python src/deepeval_poc/examples/owasp_security_tests.py

# Medical Records Conversation Security (12-turn test)
python src/deepeval_poc/examples/conversational_live.py

# Generate 100 Synthetic Test Cases
python src/deepeval_poc/examples/synthetic_generation.py

# Prompt Optimization
python src/deepeval_poc/examples/prompt_optimizer.py
```

## Features

### OWASP LLM Security Testing
Tests for 7/10 OWASP LLM Top 10:2025 categories:
- **LLM01**: Prompt Injection (8 test cases)
- **LLM02**: Sensitive Information Disclosure (9 test cases)
- **LLM04**: Data and Model Poisoning (2 test cases)
- **LLM05**: Improper Output Handling (6 test cases)
- **LLM06**: Excessive Agency (2 test cases)
- **LLM07**: System Prompt Leakage (10 test cases)
- **LLM09**: Misinformation (2 test cases)

### Medical Records Conversation
- 12-turn conversation testing HIPAA compliance
- Identity verification across conversation flow
- Credential protection (passwords, SSN)
- Medical information privacy

### Synthetic Test Generation
- Generate 100+ test cases automatically
- Medical records and healthcare scenarios
- Evolution strategies (reasoning, multi-context, etc.)

### Prompt Optimization
- GEPA algorithm for prompt improvement
- Support agent scenario
- AnswerRelevancyMetric evaluation

## Project Structure

```
deepeval/
├── src/deepeval_poc/
│   ├── __init__.py              # Auto-loads .env
│   └── examples/
│       ├── owasp_security_tests.py      # OWASP testing
│       ├── conversational_live.py       # Medical conversation
│       ├── synthetic_generation.py      # Test case generation
│       └── prompt_optimizer.py          # Prompt optimization
├── requirements.txt             # 4 dependencies
├── setup.py                     # Package setup
└── .env.example                 # Environment template
```

## Requirements

- Python 3.12+
- OpenAI API key
- Dependencies: deepeval, openai, python-dotenv, requests

## References

- [DeepEval Documentation](https://docs.confident-ai.com/)
- [OWASP LLM Top 10:2025](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
