# Lodgio Group Project

## Overview
Lodgio is a Django-based accommodation and booking platform designed to map the entities of our ERD strictly into isolated modular apps, fulfilling the requirements for the Django Project Creation assignment.

## Group Member Contributions & Project Structure
To ensure a cohesive project, the ERD was divided such that each group member handled specific entities, encapsulating them into individual Django Apps within this master repository:

*   **`core`**: Contains the foundational `User` model (handling secure authentication, passwords, and sessions), as well as the main Index Dashboard and Login View. *
*   **`listings`**: Handles the physical tracking of properties via the `Listing` model, and their availability via the `CalendarBlock` model.
*   **`bookings`**: Contains the `Booking` model mapping Guest interactions to Specific Listings. *(Built by Group Leader)*
*   **`wishlist`**: Manages users saving and tracking their favorite properties. *(Built by Teammate)*
*   **`search`**: Handles and logs query filtering across active lodgings. *(Built by Teammate)*
*   **`approvals`**: Administrator tracking for validating and verifying host listings. *(Built by Teammate)*

---

## How to Run This Project

### 1. Environment Setup
Create and activate an empty Python virtual environment, then quickly install all necessary dependencies using the provided file:
```bash
pip install -r requirements.txt
```

### 2. Database Connection
This project relies on MySQL 8.0 instead of SQLite. Open MySQL Workbench and run:
```sql
CREATE DATABASE lodgio_db;
```
*(Ensure your local MySQL `root` user password matches the one in `lodgio/settings.py`. If it does not, update the file locally before proceeding).*

### 3. Generate the Tables
Once the core database is created, let Django read all the modular Apps and construct the formal ERD structure inside MySQL Workbench:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Boot the Server
```bash
python manage.py runserver 8080
```
Navigate to `http://127.0.0.1:8080/login/` to enter the application!
