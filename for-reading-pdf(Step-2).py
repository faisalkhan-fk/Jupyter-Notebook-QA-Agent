import pymupdf                                           # for reading PDFs
from sentence_transformers import SentenceTransformer   # to convert text into numeric vectors
import faiss                                             # for fast similarity search
import numpy as np
import google.generativeai as genai                     # for generating answers
from dotenv import load_dotenv                          # to load the API key from .env
import os
