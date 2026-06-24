import os
from pipeline.intent_extractor import extract_intent
from pipeline.system_designer import design_system
from pipeline.schema_generator import generate_schemas
from pipeline.validator import validate_schemas
from pipeline.repair_engine import repair_schemas
from pipeline.runtime import execute_db_schema
from pipeline.code_generator import generate_backend_code

prompt = """
Build a CRM with login,
contacts,
dashboard,
role-based access,
premium plan with payments.
Admins can see analytics.
"""

# Stage 1
intent = extract_intent(prompt)

# Stage 2
design = design_system(intent)

# Stage 3
schemas = generate_schemas(design)

# Stage 4
errors = validate_schemas(
    design,
    schemas
)

print("\nINTENT")
print(intent.model_dump())

print("\nSYSTEM DESIGN")
print(design.model_dump())

print("\nUI SCHEMA")
print(schemas["ui"].model_dump())

print("\nAPI SCHEMA")
print(schemas["api"].model_dump())

print("\nDB SCHEMA")
print(schemas["db"].model_dump())

print("\nAUTH SCHEMA")
print(schemas["auth"].model_dump())

print("\nVALIDATION")


if errors:

    print(errors)

    schemas, repairs = repair_schemas(
        design,
        schemas,
        errors
    )

    print("\nREPAIRS")
    print(repairs)

    # Revalidate
    new_errors = validate_schemas(
        design,
        schemas
    )

    print("\nPOST REPAIR VALIDATION")

    if new_errors:
        print(new_errors)
    else:
        print("All issues resolved")

else:
    print("No validation errors")

print("\nEXECUTION")

result = execute_db_schema(
    schemas["db"]
)

print("Execution Result:")
print(result)

backend_code = generate_backend_code(
    schemas["api"]
)

os.makedirs(
    "outputs",
    exist_ok=True
)

with open(
    "outputs/generated_backend.py",
    "w",
    encoding="utf-8"
) as f:
    f.write(backend_code)

print("\nBACKEND GENERATED")