from django.shortcuts import render
from django.http import JsonResponse
from affinda import AffindaAPI, TokenCredential
from .models import Document

# Initialize Affinda API
api = AffindaAPI(credential=TokenCredential("your_affinda_api_key"))

def pull_document(request, document_id):
    try:
        document = api.get_document(document_id)
        doc_details = Document(
            document_id=document.id,
            file_name=document.file_name,
            file_url=document.url,
        )
        doc_details.save()
        return JsonResponse({'status': 'success', 'message': 'Document saved successfully'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'documents/document_list.html', {'documents': documents})
