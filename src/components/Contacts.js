import React, { useState, useEffect } from 'react';
import styles from './Contacts.module.css';
import { v4 as uuidv4 } from 'uuid';


const workerCode = `
importScripts('https://cdnjs.cloudflare.com/ajax/libs/uuid/8.3.2/uuid.min.js');
    self.onmessage = function(event) {
        const { type, contacts } = event.data;

        switch (type) {
            case 'duplicateContacts':
                self.postMessage(duplicateContacts(contacts));
                break;
            case 'sortContacts':
                self.postMessage(sortContacts(contacts));
                break;
            default:
                break;
        }
    }

    function duplicateContacts(contacts) {
      const duplicatedContacts = [];
      while (duplicatedContacts.length < 10000) {
          duplicatedContacts.push(...contacts.map((contact) => ({ ...contact, id: uuid.v4() })));
      }
      return { type: 'duplicate', data: duplicatedContacts };
  }

    function sortContacts(contacts) {
        return { type: 'sort', data: [...contacts].sort((a, b) => a.name.localeCompare(b.name)) };
    }
    `;

const workerBlob = new Blob([workerCode], { type: 'application/javascript' });
const workerUrl = URL.createObjectURL(workerBlob);
const worker = new Worker(workerUrl);


  

function Contacts() {
  const [contacts, setContacts] = useState([]);
  const [newContactName, setNewContactName] = useState('');

  const addContact = () => {
    if (newContactName.trim() === '') {
      alert('Please enter a contact name.');
      return;
    }

    const newContact = {
      id: uuidv4(),
      name: newContactName,
    };

    setContacts((prevContacts) => [...prevContacts, newContact]);
    setNewContactName('');
  };

  const deleteContact = (id) => {
    setContacts((prevContacts) => prevContacts.filter((contact) => contact.id !== id));
  };


  const duplicateContacts = async () => {
    if (contacts.length === 0) {
      alert('No contacts to duplicate.');
      return;
    }
    worker.postMessage({ type: 'duplicateContacts', contacts: contacts });
  };  

    const sortContacts = () => {
      worker.postMessage({ type: 'sortContacts', contacts: contacts });
  };

  // Handle responses from the worker
  worker.onmessage = function(event) {
    const { type, data } = event.data;
    switch (type) {
        case 'duplicate':
            setContacts(data);
            break;
        case 'sort':
            setContacts(data);
            break;
        default:
            break;
    }
}


  return (
    <div className={styles.contacts}>
      <h1 className={styles.title}>Contacts</h1>
      <div className={styles.addContactContainer}>
        <input
          className={styles.contactNameInput}
          type="text"
          placeholder="Enter contact name"
          value={newContactName}
          onChange={(e) => setNewContactName(e.target.value)}
        />
        <button className={styles.addContactButton} onClick={addContact}>
          Add Contact
        </button>
        <button data-testid="duplicateContactsButton" className={styles.duplicateButton} onClick={duplicateContacts}>
          Duplicate Contacts
        </button>
      </div>
      <button className={styles.sortButton} onClick={sortContacts}>
        Sort Contacts
      </button>
      <ul className={styles.contactList}>
        {contacts.map((contact) => (
          <li key={contact.id} className={styles.contactItem} data-testid="contactItem">
            {contact.name}{' '}
            <button className={styles.deleteButton} onClick={() => deleteContact(contact.id)}>
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Contacts;
