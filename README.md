# LLM-Inspired Agent-Based Traffic Simulation

This project implements a minimal **agent-based traffic simulation** inspired by
concepts from **Large Language Models (LLMs)**, such as perception, memory,
reasoning, and decision-making.

Each agent represents a vehicle that observes its local environment, stores
recent experiences in memory, reasons about potential risks, and decides how to
adjust its speed accordingly. The simulation demonstrates how **macro-level
traffic phenomena** (e.g., congestion and queue formation) can emerge from
simple micro-level agent behaviors.

---

## Key Concepts

- **Perception**: Agents observe the distance to the vehicle ahead.
- **Memory**: Agents store recent danger or safety experiences.
- **Reasoning**: Decisions are influenced by personality and memory.
- **Action**: Agents accelerate, decelerate, or maintain speed.
- **Emergence**: Traffic patterns arise without explicit global traffic rules.

---

## Installation

Create a virtual environment and install the required dependencies:
**Windows**
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
**Linux / macOS**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Running the Simulation
```bash
python run_simulation.py
```
## Running Experiments (Notebook)
```bash
jupyter notebook demo/demo.ipynb
```