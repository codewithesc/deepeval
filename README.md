# DeepEval POC - Prompt Evaluation and Optimization

A professional implementation demonstrating prompt evaluation and optimization using DeepEval and OpenAI GPT models.

## 📁 Project Structure

```
deepeval/
├── src/
│   └── deepeval_poc/
│       ├── core/                 # Core modules
│       │   ├── config.py        # Configuration management
│       │   └── openai_model.py  # OpenAI model wrapper
│       ├── examples/            # Example implementations
│       │   ├── conversational_live.py      # Live conversational evaluation
│       │   ├── conversational_test.py      # Static conversational tests
│       │   ├── simple_test.py              # Simple evaluation example
│       │   ├── prompt_optimizer.py         # Prompt optimization
│       │   └── synthetic_generation.py     # Synthetic test generation
│       ├── tests/               # Test files
│       └── utils/               # Utility functions
├── integrations/
│   └── flowise/                 # Flowise integration modules
├── docs/                        # Documentation
├── venv/                        # Virtual environment
├── .env                         # Environment variables (not in git)
├── .env.example                 # Environment template
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## 🚀 Quick Start

### 1. Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your API key
# Set OPENAI_API_KEY=your-key-here
```

### 3. Run Examples

```bash
# Simple evaluation
python -m src.deepeval_poc.examples.simple_test

# Live conversational evaluation
python -m src.deepeval_poc.examples.conversational_live

# Generate 100+ synthetic test cases
python -m src.deepeval_poc.examples.synthetic_generation

# Prompt optimization
python -m src.deepeval_poc.examples.prompt_optimizer
```

## 📖 Examples

### 1. Live Conversational Evaluation

Demonstrates how to:
- Use `chatbot_role` as system prompt
- Generate actual model responses with context
- Evaluate conversational completeness

```python
from deepeval_poc.examples.conversational_live import main
main()
```

### 2. Synthetic Test Generation

Generate 100+ test cases automatically:
- From scratch (based on scenario)
- From context (based on your docs)
- Different evolution strategies

```python
from deepeval_poc.examples.synthetic_generation import main
main()
```

### 3. Simple Evaluation

Basic prompt evaluation without optimization:

```python
from deepeval_poc.examples.simple_test import main
main()
```

### 4. Prompt Optimization

Iteratively optimize prompts using GEPA algorithm:

```python
from deepeval_poc.examples.prompt_optimizer import main
main()
```

## 🔑 Key Features

### Conversational Testing
- **System Prompt via `chatbot_role`**: Define your assistant's personality and instructions
- **Live Response Generation**: Generate actual model responses with conversation context
- **Multiple Metrics**: Conversation completeness, relevancy, etc.

### Synthetic Test Generation
- **Scale**: Generate 100+ test cases automatically
- **From Scratch**: No context needed, just define scenario
- **From Context**: Use your knowledge base/documentation
- **Evolution Types**: Reasoning, Multi-context, Hypothetical, Comparative, etc.

### Best Practices
- Clean separation of concerns
- Type hints throughout
- Comprehensive error handling
- Production-ready code structure

## 📚 Documentation

See `/docs` for detailed documentation:
- [Flowise Integration Guide](docs/FLOWISE_INTEGRATION.md)
- [Flowise Native Integration](docs/FLOWISE_NATIVE_INTEGRATION.md)
- [Testing Guide](docs/TESTING.md)

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | OpenAI API key (required) | None |
| `MODEL_NAME` | OpenAI model to use | gpt-4o-mini |
| `MODEL_TEMPERATURE` | Sampling temperature (0-2) | 0.7 |
| `MODEL_MAX_TOKENS` | Maximum tokens in response | 1024 |
| `METRIC_THRESHOLD` | Minimum acceptable metric score | 0.7 |
| `MAX_ITERATIONS` | Maximum optimization iterations | 10 |
| `VERBOSE` | Enable verbose logging | true |

## 🧪 Testing

```bash
# Run all tests
pytest src/deepeval_poc/tests/

# Run specific test
pytest src/deepeval_poc/tests/test_api_server.py
```

## 📦 Core Modules

### `deepeval_poc.core.config`
Configuration management with validation:
```python
from deepeval_poc.core.config import load_config

model_config, optimization_config = load_config()
```

### `deepeval_poc.core.openai_model`
OpenAI model wrapper implementing DeepEvalBaseLLM:
```python
from deepeval_poc.core.openai_model import GPTModel

model = GPTModel(model_name="gpt-4o-mini")
response = model.generate("Your prompt here")
```

## 🤝 Contributing

This is a proof of concept for evaluation purposes.

## 📄 License

This is a proof of concept for evaluation purposes.

## 🔗 References

- [DeepEval Documentation](https://docs.confident-ai.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [DeepEval GitHub Repository](https://github.com/confident-ai/deepeval)
