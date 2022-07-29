import os

os.environ.setdefault("AWS_ACCESS_KEY_ID", "<your aws access key id>")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "<your aws secret access key>")
os.environ.setdefault("DATABASE_URL", "<your database url>")
os.environ.setdefault("EMAIL_HOST_PASS", "<your gmail app password>")
os.environ.setdefault("EMAIL_HOST_USER", "<your gmail email>")
os.environ.setdefault("SECRET_KEY", "<your secret key>")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "<your stripe public key>")
os.environ.setdefault("STRIPE_SECRET_KEY", "<your stripe secret key>")
os.environ.setdefault("STRIPE_WH_SECRET", "<your stripe webhook signing secret>")  # noqa
os.environ.setdefault("USE_AWS", "<True>")
os.environ.setdefault("DEVELOPMENT", "<True>")
