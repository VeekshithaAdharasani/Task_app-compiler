from fastapi import FastAPI
from pydantic import BaseModel

from pipeline.intent_extractor import extract_intent
from pipeline.system_designer import design_system
from pipeline.schema_generator import generate_schemas
from pipeline.validator import validate_schemas
from pipeline.runtime import execute_db_schema
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PromptRequest(BaseModel):
    prompt: str


@app.post("/generate")
def generate_app(req: PromptRequest):

    intent = extract_intent(req.prompt)

    design = design_system(intent)

    schemas = generate_schemas(design)

    errors = validate_schemas(
        design,
        schemas
    )

    execution = execute_db_schema(
        schemas["db"]
    )

    return {
        "intent": intent.model_dump(),
        "design": design.model_dump(),
        "ui": schemas["ui"].model_dump(),
        "api": schemas["api"].model_dump(),
        "db": schemas["db"].model_dump(),
        "auth": schemas["auth"].model_dump(),
        "validation": errors,
        "execution": execution
    }