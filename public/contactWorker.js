import { expose } from 'comlink';

const workerFunctions = {
  duplicateContacts: (contacts) => {
    const duplicatedContacts = [];
    while (duplicatedContacts.length < 10000) {
      duplicatedContacts.push(...contacts.map((contact) => ({ ...contact, id: contact.id })));
    }
    return { type: 'duplicate', data: duplicatedContacts };
  },

  sortContacts: (contacts) => {
    return { type: 'sort', data: contacts.sort((a, b) => a.name.localeCompare(b.name)) };
  }
};

expose(workerFunctions);
