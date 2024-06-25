# Restaurant Search App

Welcome to the Restaurant Search App! This project allows you to search for restaurants based on dishes they offer and provides recommendations based on your search queries.

## Installation

To get started with the project, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your_username/restaurant_search.git
   cd restaurant_search

2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

3. Install dependencies:
   pip install -r requirements.txt

4. Apply database migrations:
   python manage.py makemigrations
   python manage.py migrate
   python manage.py shell
   shell cmds:
   >>> from search.data_import import populate_data
   >>> populate_data()


5. Start the development server:
   python manage.py runserver

The app will be available at http://localhost:8000 in your web browser.

Usage:
Searching for Restaurants
Open your web browser and go to http://localhost:8000/search/search/.
Enter the name of a dish you want to search for in the search box.
Click on the "Search" button.
Viewing Results
You will see a list of restaurants that offer the dish you searched for.
Each restaurant will display its name and the items they offer.
Recommendations
Below the search results, you will find recommendations based on your search query.
Recommendations are sorted based on ratings and relevance to your search.