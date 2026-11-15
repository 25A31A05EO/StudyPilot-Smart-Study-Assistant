# StudyPilot – Smart Study & Task Planner

A Python-based Smart Study and Task Planner designed to help students organize their study activities, manage tasks, track progress, and analyze productivity.

## 📌 About the Project

StudyPilot is a student productivity application developed using Python and Flask. It provides a simple way to create and manage study tasks, monitor task completion, and view productivity analytics.

The project also includes a browser-based prototype built using HTML, CSS, and JavaScript to demonstrate the user interface and planned functionality.

## 🎯 Objectives

- Organize academic tasks in one place.
- Set priorities for study activities.
- Track completed and pending tasks.
- Monitor study productivity.
- Provide analytics to understand task progress.
- Encourage consistent study habits.

## ✨ Key Features

- **Task Management:** Add and view study tasks.
- **Task Tracking:** Monitor task completion.
- **Priority Management:** Organize tasks based on importance.
- **Productivity Analytics:** View study and task statistics.
- **REST API:** Access task and analytics functionality through Flask endpoints.
- **Browser Prototype:** Explore the proposed interface through a web browser.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming |
| Flask | Backend and REST API |
| HTML | Webpage structure |
| CSS | User interface styling |
| JavaScript | Browser interactions |
| JSON | Data storage |
| Git & GitHub | Version control and collaboration |

## 📂 Project Structure

```text
StudyPilot-Smart-Study-Assistant/
│
├── src/
│   ├── app.py
│   ├── task_manager.py
│   └── analytics.py
│
├── prototype/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── docs/
│   ├── Project_Report.docx
│   └── System_Architecture_Flowchart.png
│
├── presentation/
│   └── StudyPilot_Presentation.pptx
│
├── assets/
│   └── ui_preview.png
│
├── requirements.txt
└── README.md
```

## 🚀 Installation and Execution

### 1. Clone the repository

```bash
git clone https://github.com/25A31A05EV/StudyPilot-Smart-Study-Assistant.git
```

### 2. Open the project folder

```bash
cd StudyPilot-Smart-Study-Assistant
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask application

```bash
python src/app.py
```

### 5. Open in your browser

```text
http://localhost:5000
```

## 🌐 Browser Prototype

The project includes a standalone browser prototype.

To open it:
1. Navigate to the `prototype` folder.
2. Open `index.html` in your web browser.
3. Explore the prototype interface.

**Note:** The browser prototype is a standalone demonstration and does not automatically synchronize with the Flask backend.

## 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Application status |
| GET | `/tasks` | Retrieve tasks |
| POST | `/tasks/add` | Add a new task |
| GET | `/analytics` | View productivity analytics |

## 👥 Project Team

This project is developed collaboratively by:

1. **Sowmya Velugubantla**
2. **Shiny Hadassah**
3. **Mounika Surya**
4. **Sai Kiran**

All team members collaborate through a shared GitHub repository.

## 🔮 Future Enhancements

- User authentication and personalized dashboards.
- Study reminders and notifications.
- Calendar integration.
- Advanced productivity reports.
- Database integration.
- AI-powered study recommendations.

## 📄 Project Deliverables

- Python source code
- Browser-based prototype
- Project documentation
- System architecture flowchart
- Project presentation
- UI preview

## 📌 GitHub Repository

https://github.com/25A31A05EV/StudyPilot-Smart-Study-Assistant

---

**StudyPilot – Plan Smart. Study Better. Achieve More.**
