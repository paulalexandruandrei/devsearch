from django.http import HttpResponse, Http404
from django.conf import settings
import os


def acme_challenge(request, token):
    """
    Serve ACME HTTP-01 challenge files for Let's Encrypt certificate validation.
    
    This view serves files from /opt/portfolio-project/devsearch/staticfiles/.well-known/acme-challenge/
    as required by the ACME HTTP-01 challenge process for SSL certificate validation.
    """
    # Define the path to the ACME challenge directory
    acme_challenge_path = '/opt/portfolio-project/devsearch/staticfiles/.well-known/acme-challenge'
    
    # Construct the full file path
    file_path = os.path.join(acme_challenge_path, token)
    
    # Security check: ensure the requested file is within the allowed directory
    if not os.path.abspath(file_path).startswith(os.path.abspath(acme_challenge_path)):
        raise Http404("File not found")
    
    try:
        # Read and serve the challenge file
        with open(file_path, 'r') as f:
            content = f.read()
        return HttpResponse(content, content_type='text/plain')
    except (FileNotFoundError, PermissionError):
        raise Http404("File not found")