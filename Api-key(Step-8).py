load_dotenv()   # load the .env file

api_key = os.getenv("GEMINI_API_KEY")   # use the exact variable name from your .env file
genai.configure(api_key=api_key)

gen_model = genai.GenerativeModel("gemini-3.6-flash")
