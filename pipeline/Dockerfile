FROM python:3.13.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/
# for bringing uv from another image to this image, so that we can use uv to install dependencies in the virtual environment.

WORKDIR /code

# Add virtual environment to PATH so we can use installed packages
ENV PATH="/code/.venv/bin:$PATH"


COPY pyproject.toml .python-version uv.lock ./

RUN uv sync --locked --no-install-project
# for running dependencies in the virtual environment.

RUN pip install pandas pyarrow

COPY pipeline.py .

ENTRYPOINT ["python", "pipeline.py"] 
#definfing the entrypoint for the docker image, so that when we run the docker image, it will run the pipeline.py file.