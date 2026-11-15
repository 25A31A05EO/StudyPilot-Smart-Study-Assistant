document.getElementById('task-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const input = document.getElementById('task-input');
    const priority = document.getElementById('priority-select').value;
    if (!input.value.trim()) return;

    const ul = document.getElementById('task-list');
    const li = document.createElement('li');
    li.className = 'task-item';
    li.innerHTML = `<span>[${priority}] ${input.value}</span><button class="status-btn" onclick="toggleTask(this)">Mark Complete</button>`;
    ul.appendChild(li);

    input.value = '';
    updateStats();
});

function toggleTask(btn) {
    const li = btn.parentElement;
    li.classList.toggle('completed');
    if (li.classList.contains('completed')) {
        btn.textContent = 'Done';
    } else {
        btn.textContent = 'Mark Complete';
    }
    updateStats();
}

function updateStats() {
    const total = document.querySelectorAll('.task-item').length;
    const completed = document.querySelectorAll('.task-item.completed').length;
    const rate = total === 0 ? 0 : Math.round((completed / total) * 100);

    document.getElementById('total-count').textContent = total;
    document.getElementById('completed-count').textContent = completed;
    document.getElementById('productivity-score').textContent = rate + '%';
}
