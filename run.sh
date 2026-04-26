#!/bin/bash
# Run script for Django landing page with venv

cd "$(dirname "$0")"
source venv/bin/activate

echo "Starting Django development server..."
echo "Access: http://localhost:8000/"
echo ""
python manage.py runserver 0.0.0.0:8000
