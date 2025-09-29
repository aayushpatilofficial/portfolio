# Portfolio Web Application

## Overview

This is a Flask-based personal portfolio website for Aayush Patil that showcases projects, handles contact form submissions, and provides a responsive web interface. The application features a simple architecture with JSON-based data storage for portfolio items and contact messages, integrated email functionality for contact form notifications, and a modern responsive design using Tailwind CSS.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Template Engine**: Jinja2 templates with Flask for server-side rendering
- **CSS Framework**: Tailwind CSS via CDN for rapid styling and responsive design
- **JavaScript**: Vanilla JavaScript for basic interactivity (scroll animations, keyboard shortcuts)
- **Design Pattern**: Mobile-first responsive design with component-based template structure

### Backend Architecture
- **Web Framework**: Flask (Python) with single-file application structure
- **Deployment**: Gunicorn WSGI server configuration for production deployment
- **Routing**: Simple Flask routes handling GET/POST requests for pages and API endpoints
- **Error Handling**: Flash messages for user feedback and basic error handling

### Data Storage
- **Primary Storage**: JSON files for simplicity and ease of deployment
- **Portfolio Data**: `data/portfolio.json` stores project information with id, title, description, and tags
- **Contact Data**: `data/contacts.json` stores contact form submissions with timestamps
- **File Structure**: Organized data directory with automatic file initialization

### Email Integration
- **Email Service**: Flask-Mail with Gmail SMTP for contact form notifications
- **Configuration**: Environment variable-based email credentials for security
- **Features**: Automatic email sending when contact forms are submitted

### Security & Configuration
- **Secret Management**: Environment variables for sensitive data (Flask secret key, email credentials)
- **Session Security**: Flask secret key requirement for secure sessions and flash messages
- **Production Ready**: Gunicorn configuration with worker scaling and logging setup

## External Dependencies

### Core Framework Dependencies
- **Flask 3.1.2**: Web application framework
- **Flask-Mail 0.10.0**: Email sending functionality
- **Gunicorn 23.0.0**: Production WSGI server

### Utility Dependencies
- **python-dotenv 1.1.1**: Environment variable management

### Frontend Dependencies
- **Tailwind CSS**: Loaded via CDN for styling and responsive design
- **Vanilla JavaScript**: No external JS frameworks, minimal client-side dependencies

### Email Service Integration
- **Gmail SMTP**: Configured for sending contact form notifications
- **App Password Authentication**: Supports Gmail's app-specific passwords for security

### Deployment Platform Support
- **Replit Compatible**: Designed to work seamlessly on Replit platform
- **Render Compatible**: Configuration supports Render deployment platform
- **Environment Configuration**: Flexible environment variable setup for different deployment targets