# Pam Holdings Estates - Client Registration

A mobile-first client registration system that captures client information via Google OAuth and stores it in Google Sheets.

## Features

- QR code ready for different campaigns
- Mobile-first responsive design
- Google OAuth authentication
- Automatic data saving to Google Sheets
- Phone number collection

## Setup

1. Copy \.env.example\ to \.env\
2. Fill in your Google Cloud credentials
3. Run \pip install -r requirements.txt\
4. Run \python manage.py migrate\
5. Run \python manage.py runserver\

## Deployment

Configured for Vercel deployment with automatic static file handling.
