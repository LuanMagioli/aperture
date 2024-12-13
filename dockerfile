FROM python:1.12

ENV GOOGLE_GEMINI_API_KEY=AIzaSyCYgrOjCeABiEoqvWbTEEcXPZyTBkE1DUg
ENV GOOGLE_SEARCH_ENGINE_KEY=AIzaSyCYgrOjCeABiEoqvWbTEEcXPZyTBkE1DUg

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80