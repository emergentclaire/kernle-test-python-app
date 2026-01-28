# Kernle Test: Python Application

Testing Kernle as a library in a Python application - how a dev would integrate it into their own codebase.

## Setup

```bash
pip install kernle
```

## Usage

```python
from kernle import Kernle

k = Kernle("my-app-agent")

# Load memory at start
memory = k.load()

# Save experiences
k.episode("User completed task", "Success", lessons=["User prefers X"])

# Save checkpoint before shutdown
k.checkpoint("App shutdown state")
```
