#before running this script you need to manually download the models: docling-tools models download
#or enable downloads
#check how to enable download for easyocr https://www.jaided.ai/easyocr/documentation/
#mkdir -p /tmp/EasyOcr
#wget https://github.com/JaidedAI/EasyOCR/releases/download/pre-v1.1.6/craft_mlt_25k.zip 
#unzip it to the model dir

import os
os.environ["EASYOCR_DISABLE_DOWNLOADS"] = "0"

import docling
from pathlib import Path
from docling.document_converter import DocumentConverter
from docling.datamodel.settings import settings


settings.cache_dir = '/tmp'
settings.artifacts_path = '/tmp/'
models_dir = Path('/tmp/models')
try:
  docling.utils.model_downloader.download_models(output_dir=models_dir, progress=True)
  print("model download finished successfuly")
except Exception as e:
  print("model download failed")
  print(e)



source = "https://arxiv.org/pdf/2408.09869"  # document per local path or URL
converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_markdown())  # output: "## Docling Technical Report[...]"
