 The aim of this project based on Python is to process chaotic log data and obtain necessary results by means of regular expressions and store them in a safe way in JSON format.

### Types of processed information
1. **Emails**: classified as official ALU, unofficial ALU, Alumni, SI, and External emails.
2. **Credit Cards**: normal 16-digit card numbers.
3. **URLs**: normal URL.
4. **Phone numbers**: International formats

### Recommended security characteristics
- **Length constraint**: eliminates anything longer than 500 characters.
- **Tag deletion feature**: eliminates all harmful HTML and script tags.
- **Data anonymization feature**: anonymizes credit card and email.

### Steps to follow
1. Ensure that your input text is located in `input/raw-text.txt`.
2. Navigate to `src/`: `cd src`.
3. Execute the Python program `python main.py`.
4. You can check your output in `output/sample-output.json`.