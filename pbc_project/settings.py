import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ... inside TEMPLATES ...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR],  # This allows Django to find index.html in the root
        'APP_DIRS': True,    # This allows Django to find marketing/signin.html inside your app
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]