def generate_backend_code(api_schema):

    code = []

    code.append("from fastapi import FastAPI")
    code.append("")
    code.append("app = FastAPI()")
    code.append("")

    for endpoint in api_schema.endpoints:

        method = endpoint.method.lower()

        route = endpoint.path

        function_name = (
            f"{method}_"
            + route.replace("/", "_")
                    .replace("{", "")
                    .replace("}", "")
                    .strip("_")
        )

        code.append(
            f"@app.{method}('{route}')"
        )

        code.append(
            f"def {function_name}():"
        )

        code.append(
            "    return {'message': 'generated'}"
        )

        code.append("")

    return "\n".join(code)