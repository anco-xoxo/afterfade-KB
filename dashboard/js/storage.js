const Storage = {
  CARDS_KEY: 'afterfade_cs_cards',
  TEMPLATES_KEY: 'afterfade_cs_templates',

  getCards() {
    const data = localStorage.getItem(this.CARDS_KEY);
    return data ? JSON.parse(data) : {};
  },

  saveCards(cards) {
    localStorage.setItem(this.CARDS_KEY, JSON.stringify(cards));
  },

  getCard(date) {
    const cards = this.getCards();
    return cards[date] || null;
  },

  saveCard(date, card) {
    const cards = this.getCards();
    cards[date] = card;
    this.saveCards(cards);
  },

  createCard(date, templates) {
    return {
      date,
      startDate: '',
      dueDate: '',
      opening: templates.opening.map((t, i) => ({
        id: i + 1,
        text: t.text,
        done: false
      })),
      closing: templates.closing.map((t, i) => ({
        id: i + 1,
        text: t.text,
        done: false
      })),
      custom: []
    };
  },

  getTemplates() {
    const data = localStorage.getItem(this.TEMPLATES_KEY);
    return data ? JSON.parse(data) : null;
  },

  saveTemplates(templates) {
    localStorage.setItem(this.TEMPLATES_KEY, JSON.stringify(templates));
  },

  getNextId(items) {
    if (items.length === 0) return 1;
    return Math.max(...items.map(i => i.id)) + 1;
  }
};
