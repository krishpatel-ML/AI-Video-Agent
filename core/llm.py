import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.rate_limiters import InMemoryRateLimiter

load_dotenv()

# One limiter shared by every call in the app: ~1 request every 2 seconds
_rate_limiter = InMemoryRateLimiter(
    requests_per_second=0.5,
    check_every_n_seconds=0.1,
    max_bucket_size=1,
)


def get_llm(temperature: float = 0.3):
    return ChatGroq(
        model=os.getenv("GROQ_MODEL", "openai/gpt-oss-120b"),
        temperature=temperature,
        max_retries=5,
        timeout=90,
        rate_limiter=_rate_limiter,
    )
