import os
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential


def format_bounding_region(bounding_regions):
    if not bounding_regions:
        return "N/A"
    return ", ".join("Page #{}: {}".format(region.page_number, format_polygon(region.polygon)) for region in bounding_regions)


def format_polygon(polygon):
    if not polygon:
        return "N/A"
    return ", ".join(["[{}, {}]".format(p.x, p.y) for p in polygon])


def document_to_ocr(url):
    endpoint = os.environ.get("AZURE_DOCUMENT_LAYOUT_ENDPOINT")
    key = os.environ.get("AZURE_DOCUMENT_LAYOUT_KEY")

    try:
        file_text = ""
        document_analysis_client = DocumentAnalysisClient(
            endpoint=endpoint, credential=AzureKeyCredential(key))
        poller = document_analysis_client.begin_analyze_document_from_url(
            "prebuilt-layout", url)

        result = poller.result()

        if not result.paragraphs:
            print("No paragraphs were extracted from the document.")
        else:
            print("----Paragraphs found in document----")
            for paragraph in result.paragraphs:
                file_text += paragraph.content
                file_text += "\n"

        return file_text.strip()
    except Exception as e:
        print(e)
        return f"ERROR: {e}"
