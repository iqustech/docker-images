from typing import Optional, Union

from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from api.generation import (
    ImageGenerationOptions,
    ImageGenerationResult,
    ImageGenerationError,
    ImageGenerationProgress,
)
from modules import runners

from ..api_router import api
from ..models.base import BaseResponseModel


class GenerateImageRequest(BaseModel):
    prompt: str
    negative_prompt: str = ""
    batch_size: int = 1
    batch_count: int = 1
    scheduler_id: str = "euler_a"
    steps: int = 28
    scale: int = 7.5
    image_height: int = 512
    image_width: int = 512
    seed: Optional[int] = None
    strength: Optional[float] = None
    img: Optional[str] = None


class GenerateImageResponseModel(BaseResponseModel):
    data: ImageGenerationResult


@api.post("/images/generate", response_model=GenerateImageResponseModel)
def generate_image(req: ImageGenerationOptions):
    result = runners.generate(req)
    return GenerateImageResponseModel(
        status="success",
        data=result,
    )


@api.post("/images/generator", response_model=Union[str, ImageGenerationResult, ImageGenerationError, ImageGenerationProgress])
def generator_image(req: ImageGenerationOptions):
    def generator():
        try:
            for data in runners.generator(req):
                yield data.ndjson()
        except Exception as e:
            yield ImageGenerationError(error=type(e).__name__, message=str(e)).ndjson()
            raise e

    return StreamingResponse(generator())
