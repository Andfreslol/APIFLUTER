import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://cruduser:vJHFuJzFHpsoDsc4Z1IbSN0ULNaAX3IH@dpg-d9hfqtupbkes73a0276g-a.oregon-postgres.render.com/crudapi_qaac"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False