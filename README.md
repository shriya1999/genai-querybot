# QueryBot: Language to SQL

**QueryBot** is an application that converts natural language questions into SQL queries and retrieves answers from a SQLite database. Powered by Google Gemini, this app allows users to interact with a database using natural language, making it easier to query and analyze data.

## Features

- Converts English questions into SQL queries using Google Gemini's generative model.
- Executes SQL queries on a SQLite database.
- Displays query results in a user-friendly format.

## Getting Started

### Prerequisites

- Python 3.x
- Streamlit
- Google Gemini API key
- SQLite3

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/shriya1999/querybot.git
   cd querybot
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the root directory of the project and add your Google Gemini API key:

   ```
   GOOGLE_API_KEY=your_google_api_key
   ```

5. **Prepare the SQLite database:**

   Ensure you have a SQLite database file named `banking.db` in the project directory with the appropriate schema and data.

### Usage

1. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

2. **Open your web browser and navigate to `http://localhost:8501` to interact with the app.**

### How It Works

- **Natural Language to SQL Conversion:** The app uses Google Gemini's generative model to convert user-provided natural language questions into SQL queries.
- **Database Query Execution:** The generated SQL queries are executed on a SQLite database (`banking.db`).
- **Display Results:** Query results are fetched and displayed in a table format within the Streamlit app.

### Example

1. **Question:** "How many customers have savings accounts?"
2. **Generated SQL Query:** `SELECT COUNT(*) FROM Account WHERE AccountType="Savings"`
3. **Results:** Displays the count of customers with savings accounts.

### Contributing

Feel free to submit issues or pull requests if you have any improvements or fixes. Please follow the project's coding style and guidelines.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Acknowledgments

- [Google Gemini](https://cloud.google.com/generative-ai) for the generative AI model.
- [Streamlit](https://streamlit.io/) for the easy-to-use framework.

---

Replace placeholders like `yourusername` and `your_google_api_key` with actual values. This `README.md` should help users understand, set up, and contribute to your project effectively.
