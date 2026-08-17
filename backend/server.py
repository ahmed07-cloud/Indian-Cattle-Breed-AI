# ============================================================
# INDIAN CATTLE BREED AI
# FASTAPI BACKEND
# ============================================================

from io import BytesIO

from fastapi import (
    FastAPI,
    UploadFile,
    File,
    HTTPException
)

from fastapi.middleware.cors import (
    CORSMiddleware
)

from PIL import Image

from app.model import (
    predict_breed,
    class_names
)

from app.breed_data import (
    get_breed_info,
    get_canonical_breed_name
)


# ============================================================
# FASTAPI APPLICATION
# ============================================================

app = FastAPI(

    title="Indian Cattle Breed AI",

    description=(
        "AI-powered Indian cattle and "
        "buffalo breed identification API"
    ),

    version="4.0.0"
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(

    CORSMiddleware,

    allow_origins=[
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://indian-cattle-breed-ai.vercel.app"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)


# ============================================================
# ROOT
# ============================================================

@app.get("/")
def root():

    return {

        "message":
            "Indian Cattle Breed AI Backend is running!",

        "status":
            "success",

        "version":
            "4.0.0",

        "model":
            "V4 EfficientNet-B0",

        "classes":
            len(class_names)
    }


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
def health_check():

    return {

        "status":
            "healthy",

        "model":
            "V4 EfficientNet-B0",

        "classes":
            len(class_names)
    }


# ============================================================
# BREED LIST
# ============================================================

@app.get("/breeds")
def get_breeds():

    return {

        "success":
            True,

        "total":
            len(class_names),

        "breeds":
            class_names
    }


# ============================================================
# BREED INFORMATION
# ============================================================

@app.get("/breeds/{breed_name}")
def get_breed_info_api(
    breed_name: str
):

    try:

        # ----------------------------------------------------
        # CANONICAL NAME
        # ----------------------------------------------------

        canonical_name = (
            get_canonical_breed_name(
                breed_name
            )
        )


        # ----------------------------------------------------
        # GET INFORMATION
        # ----------------------------------------------------

        breed_info = (
            get_breed_info(
                canonical_name
            )
        )


        # ----------------------------------------------------
        # NOT FOUND
        # ----------------------------------------------------

        if breed_info is None:

            raise HTTPException(

                status_code=404,

                detail=(
                    f"Information for breed "
                    f"'{breed_name}' "
                    f"is not available."
                )
            )


        # ----------------------------------------------------
        # RESPONSE
        # ----------------------------------------------------

        return {

            "success":
                True,

            "breed":
                canonical_name,

            "information":
                breed_info
        }


    except HTTPException:

        raise


    except Exception as e:

        print(
            "Breed information error:",
            str(e)
        )

        raise HTTPException(

            status_code=500,

            detail=(
                "Failed to load breed "
                f"information: {str(e)}"
            )
        )


# ============================================================
# PREDICT BREED
# ============================================================

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):

    # ========================================================
    # CHECK CONTENT TYPE
    # ========================================================

    if not file.content_type:

        raise HTTPException(

            status_code=400,

            detail=(
                "File type could not "
                "be determined."
            )
        )


    if not file.content_type.startswith(
        "image/"
    ):

        raise HTTPException(

            status_code=400,

            detail=(
                "Please upload a "
                "valid image file."
            )
        )


    try:

        # ====================================================
        # READ IMAGE
        # ====================================================

        image_bytes = (
            await file.read()
        )


        if not image_bytes:

            raise HTTPException(

                status_code=400,

                detail=(
                    "Uploaded image "
                    "is empty."
                )
            )


        # ====================================================
        # OPEN IMAGE
        # ====================================================

        try:

            image = Image.open(

                BytesIO(
                    image_bytes
                )

            ).convert("RGB")


        except Exception:

            raise HTTPException(

                status_code=400,

                detail=(
                    "The uploaded file "
                    "is not a valid image."
                )
            )


        # ====================================================
        # AI PREDICTION
        # ====================================================

        result = predict_breed(
            image
        )


        print(
            "Prediction result:",
            result
        )


        # ====================================================
        # GET PREDICTED BREED
        # ====================================================

        predicted_breed = (
            result.get("breed")
        )


        if not predicted_breed:

            raise HTTPException(

                status_code=500,

                detail=(
                    "Model did not "
                    "return a breed."
                )
            )


        # ====================================================
        # CANONICAL BREED NAME
        # ====================================================

        canonical_breed = (
            get_canonical_breed_name(
                predicted_breed
            )
            or predicted_breed
        )


        # ====================================================
        # GET BREED INFORMATION
        # ====================================================

        breed_info = (
            get_breed_info(
                canonical_breed
            )
        )


        # ====================================================
        # RESPONSE
        # ====================================================

        response = {

            "success":
                True,

            "filename":
                file.filename,

            "breed":
                canonical_breed,

            "confidence":
                result.get(
                    "confidence",
                    0
                ),

            "top_3":
                result.get(
                    "top_3",
                    []
                ),

            "breed_info":
                breed_info or {}
        }


        print(
            "Final API response:",
            response
        )


        return response


    # ========================================================
    # FASTAPI ERROR
    # ========================================================

    except HTTPException:

        raise


    # ========================================================
    # UNEXPECTED ERROR
    # ========================================================

    except Exception as e:

        print(
            "Prediction error:",
            str(e)
        )

        raise HTTPException(

            status_code=500,

            detail=(
                f"Prediction failed: {str(e)}"
            )
        )
