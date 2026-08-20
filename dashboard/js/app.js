const App = {
  currentDate: null,
  templates: null,

  async init() {
    this.templates = await Templates.load();

    document.getElementById('btn-today').addEventListener('click', () => {
      this.loadDate(this.today());
    });

    document.getElementById('date-picker').addEventListener('change', (e) => {
      this.loadDate(e.target.value);
    });

    document.getElementById('start-date').addEventListener('change', (e) => {
      this.updateMeta('startDate', e.target.value);
    });

    document.getElementById('due-date').addEventListener('change', (e) => {
      this.updateMeta('dueDate', e.target.value);
    });

    document.getElementById('opening-add').addEventListener('click', () => this.addCustomTask('opening'));
    document.getElementById('closing-add').addEventListener('click', () => this.addCustomTask('closing'));
    document.getElementById('custom-add').addEventListener('click', () => this.addCustomTask('custom'));

    ['opening-input', 'closing-input', 'custom-input'].forEach(id => {
      document.getElementById(id).addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          const section = id.replace('-input', '');
          this.addCustomTask(section);
        }
      });
    });

    this.loadDate(this.today());
  },

  today() {
    return new Date().toISOString().split('T')[0];
  },

  loadDate(date) {
    this.currentDate = date;

    let card = Storage.getCard(date);
    if (!card) {
      card = Storage.createCard(date, this.templates);
      Storage.saveCard(date, card);
    }

    document.getElementById('date-picker').value = date;
    document.getElementById('card-date').textContent = this.formatDate(date);
    document.getElementById('start-date').value = card.startDate || '';
    document.getElementById('due-date').value = card.dueDate || '';

    this.renderChecklist('opening', card.opening);
    this.renderChecklist('closing', card.closing);
    this.renderChecklist('custom', card.custom);

    this.updateStats();
    this.renderRecentDays();
  },

  formatDate(dateStr) {
    const d = new Date(dateStr + 'T00:00:00');
    return d.toLocaleDateString('en-US', {
      weekday: 'long',
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  },

  renderChecklist(section, items) {
    const ul = document.getElementById(`${section}-checklist`);
    ul.innerHTML = '';

    items.forEach(item => {
      const li = document.createElement('li');
      if (item.done) li.classList.add('done');

      const checkbox = document.createElement('input');
      checkbox.type = 'checkbox';
      checkbox.checked = item.done;
      checkbox.addEventListener('change', () => this.toggleItem(section, item.id));

      const text = document.createElement('span');
      text.className = 'task-text';
      text.textContent = item.text;

      li.appendChild(checkbox);
      li.appendChild(text);

      if (item.dueDate) {
        const due = document.createElement('span');
        due.className = 'task-due';
        due.textContent = `Due: ${item.dueDate}`;
        li.appendChild(due);
      }

      if (section === 'custom' || !this.isTemplateItem(section, item.text)) {
        const del = document.createElement('button');
        del.className = 'task-delete';
        del.textContent = '×';
        del.addEventListener('click', () => this.deleteItem(section, item.id));
        li.appendChild(del);
      }

      ul.appendChild(li);
    });

    this.updateProgress(section, items);
  },

  isTemplateItem(section, text) {
    const templateItems = this.templates[section] || [];
    return templateItems.some(t => t.text === text);
  },

  toggleItem(section, id) {
    const card = Storage.getCard(this.currentDate);
    const items = card[section];
    const item = items.find(i => i.id === id);
    if (item) {
      item.done = !item.done;
      Storage.saveCard(this.currentDate, card);
      this.renderChecklist(section, items);
      this.updateStats();
    }
  },

  deleteItem(section, id) {
    const card = Storage.getCard(this.currentDate);
    card[section] = card[section].filter(i => i.id !== id);
    Storage.saveCard(this.currentDate, card);
    this.renderChecklist(section, card[section]);
    this.updateStats();
  },

  addCustomTask(section) {
    const input = document.getElementById(`${section}-input`);
    const dueInput = document.getElementById('custom-due');
    const text = input.value.trim();
    if (!text) return;

    const card = Storage.getCard(this.currentDate);
    const newItem = {
      id: Storage.getNextId(card[section]),
      text,
      done: false
    };

    if (section === 'custom' && dueInput && dueInput.value) {
      newItem.dueDate = dueInput.value;
    }

    card[section].push(newItem);
    Storage.saveCard(this.currentDate, card);

    input.value = '';
    if (dueInput) dueInput.value = '';

    this.renderChecklist(section, card[section]);
    this.updateStats();
  },

  updateMeta(field, value) {
    const card = Storage.getCard(this.currentDate);
    card[field] = value;
    Storage.saveCard(this.currentDate, card);
  },

  updateProgress(section, items) {
    const total = items.length;
    const done = items.filter(i => i.done).length;
    document.getElementById(`${section}-progress`).textContent = `${done}/${total}`;
  },

  updateStats() {
    const card = Storage.getCard(this.currentDate);
    ['opening', 'closing', 'custom'].forEach(section => {
      const items = card[section];
      const total = items.length;
      const done = items.filter(i => i.done).length;
      const pct = total === 0 ? 0 : Math.round((done / total) * 100);
      const el = document.getElementById(`stat-${section}`);
      el.textContent = `${pct}%`;
      el.style.color = pct === 100 ? 'var(--success)' : pct >= 50 ? 'var(--warning)' : 'var(--text)';
    });
  },

  renderRecentDays() {
    const list = document.getElementById('recent-days-list');
    list.innerHTML = '';

    const today = this.today();
    const dates = [];

    for (let i = 0; i < 7; i++) {
      const d = new Date();
      d.setDate(d.getDate() - i);
      dates.push(d.toISOString().split('T')[0]);
    }

    dates.forEach(date => {
      const li = document.createElement('li');
      li.textContent = date === today ? `Today (${date})` : date;
      if (date === this.currentDate) li.classList.add('active');
      li.addEventListener('click', () => this.loadDate(date));
      list.appendChild(li);
    });
  }
};

document.addEventListener('DOMContentLoaded', () => App.init());
