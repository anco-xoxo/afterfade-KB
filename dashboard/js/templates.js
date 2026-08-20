const Templates = {
  async load() {
    const saved = Storage.getTemplates();
    if (saved) return saved;

    try {
      const resp = await fetch('data/templates.json');
      const templates = await resp.json();
      Storage.saveTemplates(templates);
      return templates;
    } catch (e) {
      console.warn('Could not load templates.json, using defaults');
      return this.defaults();
    }
  },

  defaults() {
    return {
      opening: [
        { text: "Check Vocero inbox for new messages" },
        { text: "Review new Shopify orders" },
        { text: "Check Trello board for pending tasks" },
        { text: "Review returns & refund requests" },
        { text: "Check WhatsApp for new conversations" },
        { text: "Review Sendcloud for shipping updates" }
      ],
      closing: [
        { text: "Follow up on unresolved customer tickets" },
        { text: "Update Trello board status" },
        { text: "Note any escalations for tomorrow" },
        { text: "Log daily questions to questions.json" },
        { text: "Check pending shipments via Sendcloud" },
        { text: "Confirm all urgent replies sent" }
      ]
    };
  }
};
