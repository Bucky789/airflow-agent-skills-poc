# Airflow Agent Skills PoC

This is a minimal proof-of-concept demonstrating:

- Breeze environment detection (host vs container)
- Basic workflow orchestration:
  - run prek
  - retry on failure
  - run pytest
- Simple decision logic

## Run

```bash
python workflow.py