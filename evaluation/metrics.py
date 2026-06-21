import json
import time

from pipeline.intent_extractor import extract_intent
from pipeline.system_designer import design_system
from pipeline.schema_generator import generate_schemas
from pipeline.validator import validate_schemas


def run_evaluation():

    with open("evaluation/dataset.json", "r") as f:
        dataset = json.load(f)

    total = len(dataset)
    success = 0
    failures = 0
    repairs_needed = 0

    latencies = []

    for item in dataset:

        prompt = item["prompt"]

        start = time.time()

        try:
            intent = extract_intent(prompt)

            design = design_system(intent)

            schemas = generate_schemas(design)

            errors = validate_schemas(
                design,
                schemas
            )

            if errors:
                repairs_needed += 1

            success += 1

        except Exception:
            failures += 1

        end = time.time()

        latencies.append(end - start)

    avg_latency = sum(latencies) / len(latencies)

    report = {
        "total_prompts": total,
        "successful_generations": success,
        "failed_generations": failures,
        "repairs_needed": repairs_needed,
        "success_rate": round(
            (success / total) * 100,
            2
        ),
        "avg_latency_seconds": round(
            avg_latency,
            4
        )
    }

    return report


if __name__ == "__main__":

    result = run_evaluation()

    with open(
        "evaluation/results.json",
        "w"
    ) as f:

        json.dump(
            result,
            f,
            indent=4
        )

    print(result)

    print(
        "\nResults saved to evaluation/results.json"
    )