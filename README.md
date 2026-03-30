*This project has been created as part of the 42 curriculum by mlorenzo.*

# 42 Python Piscine

## Description

This repository contains my work for the **42 Python Piscine**, organized by progressive modules (`Module_00` to `Module_10`) and exercises (`ex0`, `ex1`, etc.).

The goal of this project is to build a strong Python foundation through short, focused exercises that move from:

- basic syntax and control flow,
- to functions, error handling, and data processing,
- to object-oriented design patterns and package organization,
- and finally to more complete mini-systems and architecture-oriented challenges.

Each exercise is designed to train one or more practical skills used in real software development: decomposition, defensive coding, readability, abstraction, and maintainability.

## Module Journey (Purpose of Each Module)

`Module_00` - **Python basics and procedural thinking**
- First contact with syntax, variables, conditions, loops, and simple function decomposition.
- Focus: writing clean, predictable scripts from basic requirements.

`Module_01` - **Data structures and OOP introduction**
- Manipulating collections and building first class-based designs.
- Focus: moving from script logic to reusable objects and data modeling.

`Module_02` - **Exceptions and robust error handling**
- Understanding built-in exceptions, custom exceptions, `try/except/finally`, and controlled `raise`.
- Focus: writing resilient code that fails safely and communicates errors clearly.

`Module_03` - **Intermediate architecture with applied mini-systems**
- Command handling, analytics, tracking, inventory, and streaming-style problems.
- Focus: combining multiple concepts into coherent, modular solutions.

`Module_04` - **File/stream style processing and operational scenarios**
- Archive, security, and crisis-response themed exercises with stronger control flow and state transitions.
- Focus: practical scenario modeling and clearer system boundaries.

`Module_05` - **Pipelines and data flow patterns**
- Stream processing and pipeline-oriented architecture.
- Focus: sequential transformations, composition, and maintainable processing chains.

`Module_06` - **Imports, packages, and module structure**
- Package layout, circular import awareness, and project organization (`alchemy/`, subpackages).
- Focus: understanding Python import mechanics and scalable code structure.

`Module_07` - **Advanced OOP and design patterns**
- Interfaces/protocol-like classes, factories, strategies, ranking systems, and a game domain.
- Focus: polymorphism, extensibility, and low-coupling object collaboration.

`Module_08` - **Environment and tooling integration**
- Packaging and dependency files (`pyproject.toml`, `requirements.txt`) plus runtime-loading style tasks.
- Focus: reproducible execution and Python project hygiene.

`Module_09` - **Applied projects and system composition**
- More complete scenarios (for example space-station themed challenges) to integrate prior concepts.
- Focus: structuring medium-sized code with clearer responsibilities.

`Module_10` - **Capstone-level consolidation**
- Final exercises to validate autonomy and software engineering maturity.
- Focus: combining correctness, readability, architecture, and execution discipline.

## Instructions

### Prerequisites

- Python 3.10+ (3.11 recommended)
- A terminal (PowerShell, bash, or zsh)

### Repository Setup

```bash
# clone
git clone <your-repo-url>
cd Module_python

# optional virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
```

### Execute an Exercise

Most exercises are standalone Python scripts.

```bash
# example
python Module_00/ex0/ft_hello_garden.py
python Module_02/ex3/ft_finally_block.py
python Module_07/ex4/main.py
```

### Run with Input (when needed)

```bash
python <path_to_script.py> "arg1" "arg2"
```

### Code Quality Checks (recommended)

```bash
python -m py_compile Module_00/ex0/ft_hello_garden.py
```

You can repeat this command for any target file to quickly validate syntax.

## Algorithm Choices and Implementation Strategy

Even though this Piscine is split into many small exercises, a consistent strategy is used across modules:

1. **Start with a minimal valid solution**
	- Implement the simplest path that satisfies the exercise specification.
2. **Refactor for readability**
	- Rename variables/functions for intent, isolate reusable logic into helpers, and keep functions focused.
3. **Add defensive guards**
	- Validate assumptions, handle expected edge cases, and make error paths explicit (especially from `Module_02`).
4. **Choose the simplest suitable algorithm**
	- Iterative loops for straightforward counting/transforms.
	- Recursion only when the exercise explicitly targets recursive reasoning.
	- Dictionary/set-based lookup patterns when membership or counting is frequent.
5. **Prefer composition over monoliths**
	- For higher modules, split behavior into classes and collaborating components (factory/strategy style patterns in `Module_07`).
6. **Keep side effects controlled**
	- Separate pure computation from input/output where possible to simplify testing and debugging.

This approach keeps solutions understandable while still progressively introducing software design depth.

## Visual Representation Features

This project is terminal-first, so visual representation is focused on **readable console output** and **clear structural navigation**:

- Human-readable printed states and summaries in analytics/tracker/dashboard exercises.
- Consistent naming conventions (`ft_*`) and folder structure (`Module_xx/exy`) for rapid orientation.
- Scenario-based outputs (inventory, dashboards, archives, game states) that make behavior easier to validate mentally.

How this improves user experience:

- Faster debugging: outputs communicate state transitions and results clearly.
- Faster review: peers/staff can inspect progression module by module.
- Better learning feedback loop: visible results make algorithm adjustments immediate.

## Resources

### Core Python References

- Python Official Documentation: https://docs.python.org/3/
- Python Tutorial: https://docs.python.org/3/tutorial/
- Built-in Exceptions: https://docs.python.org/3/library/exceptions.html
- `pathlib`: https://docs.python.org/3/library/pathlib.html
- `typing`: https://docs.python.org/3/library/typing.html
- PEP 8 (Style Guide): https://peps.python.org/pep-0008/

### Learning and Practice References

- Real Python tutorials: https://realpython.com/
- Programiz Python reference: https://www.programiz.com/python-programming
- Refactoring Guru (design patterns): https://refactoring.guru/design-patterns/python

### AI Usage Disclosure

AI tools were used as an **assistant**, not as an automatic solution generator.

- Used for:
  - clarifying exercise statements,
  - reviewing naming/readability,
  - drafting and polishing documentation
- Not used for:
  - replacing personal understanding of core concepts,
  - bypassing algorithm design decisions,
  - submitting unreviewed code.

## Repository Structure

```text
.
|- Module_00/
|- Module_01/
|- Module_02/
|- Module_03/
|- Module_04/
|- Module_05/
|- Module_06/
|- Module_07/
|- Module_08/
|- Module_09/
`- Module_10/
```

## Notes

- This repository is intended for educational purposes in the 42 curriculum.
- Exercise names and themes may vary across Piscine versions, but the learning progression remains consistent.
