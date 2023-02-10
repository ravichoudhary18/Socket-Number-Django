from django.utils.log import DEFAULT_LOGGING
from datetime import timedelta
from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = eval(os.environ.get("DEBUG"))

if DEBUG:
    ALLOWED_HOSTS = ["*"]
    CSRF_TRUSTED_ORIGINS = ["http://*.localhost/"]
    CORS_ORIGIN_ALLOW_ALL = True
    SECRET_KEY = os.environ.get("SECRET_KEY")
    import socket  # only if you haven't already imported this
    
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + [
        "127.0.0.1",
        "10.0.2.2",
    ]
else:
    ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(",")
    CORS_ORIGIN_WHITELIST = os.environ.get("CORS_ORIGIN_WHITELIST")
    CSRF_TRUSTED_ORIGINS = [os.environ.get("CSRF_TRUSTED_ORIGINS")]
    SECRET_KEY = os.environ.get("SECRET_KEY")


INSTALLED_APPS = [
    'daphne',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MY_APPS = [

]

THIRD_PARTY_APPS = [
    "rest_framework",
    "corsheaders",
    "debug_toolbar",
]

INSTALLED_APPS += MY_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

THIRD_PARTY_MIDDLEWARES = [
    # CROSS
    "corsheaders.middleware.CorsMiddleware",
    # Django DEBUG TOOLBAR
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

MIDDLEWARE += THIRD_PARTY_MIDDLEWARES

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

ASGI_APPLICATION = "backend.routing.application"
# WSGI_APPLICATION = "backend.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/mnt/staticfiles/"

STATIC_ROOT = "/mnt/staticfiles/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# LOGGING

LOGS_DIR = "/mnt/logs"
if not Path(LOGS_DIR).exists():
    Path(LOGS_DIR).mkdir()

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
        },
        "django.server": DEFAULT_LOGGING["formatters"]["django.server"],
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
        "file": {
            "level": "INFO",
            "formatter": "default",
            "class": "logging.FileHandler",
            "filename": f"{LOGS_DIR}/info.log",
        },
    },
    "loggers": {
        "": {
            "handlers": ["file", "console"],
            "level": "INFO",
            "propagate": True,
        },
    },
}
