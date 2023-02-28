import React, { useState, useEffect } from 'react';
import { getItems, createItem, updateItem, deleteItem } from './api';

function ItemList() {
  const [items, setItems] = useState([]);
  const [newItem, setNewItem] = useState('');
  const [editingItemId, setEditingItemId] = useState(null);
  const [editingItem, setEditingItem] = useState('');

  useEffect(() => {
    async function fetchItems() {
      const items = await getItems();
      setItems(items);
    }
    fetchItems();
  }, []);

  const handleNewItemChange = (event) => {
    setNewItem(event.target.value);
  };

  const handleEditItemChange = (event) => {
    setEditingItem(event.target.value);
  };

  const handleAddItem = async (event) => {
    event.preventDefault();
    const newItem = await createItem({ name: newItem });
    setItems([...items, newItem]);
    setNewItem('');
  };
  

  const handleEditItem = async (event, itemId) => {
    event.preventDefault();
    const itemToUpdate = items.find((item) => item.id === itemId);
    const updatedItemData = { ...itemToUpdate, name: editingItem };
    const updatedItem = await updateItem(itemId, updatedItemData);
    const updatedItems = items.map((item) => (item.id === itemId ? updatedItem : item));
    setItems(updatedItems);
    setEditingItemId(null);
    setEditingItem('');
  };

  const handleDeleteItem = async (itemId) => {
    await deleteItem(itemId);
    const updatedItems = items.filter((item) => item.id !== itemId);
    setItems(updatedItems);
  };

  return (
    <div>
      <h1>Items</h1>
      <ul>
        {items.map((item) =>
          editingItemId === item.id ? (
            <li key={item.id}>
              <form onSubmit={(event) => handleEditItem(event, item.id)}>
                <input type="text" value={editingItem} onChange={handleEditItemChange} />
                <button type="submit">Save</button>
                <button onClick={() => setEditingItemId(null)}>Cancel</button>
              </form>
            </li>
          ) : (
            <li key={item.id}>
              {item.name}{' '}
              <button onClick={() => setEditingItemId(item.id)}>Edit</button>{' '}
              <button onClick={() => handleDeleteItem(item.id)}>Delete</button>
            </li>
          )
        )}
      </ul>
      <form onSubmit={handleAddItem}>
        <input type="text" value={newItem} onChange={handleNewItemChange} />
        <button type="submit">Add</button>
      </form>
    </div>
  );
}

export default ItemList;
