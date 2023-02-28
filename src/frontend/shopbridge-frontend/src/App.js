import React, { useState, useEffect } from 'react';
import ItemList from './ItemList';
import { getItems } from './api';
import './App.css';

function App() {

  const [items, setItems] = useState([]);

  useEffect(() => {
    const fetchItems = async () => {
      const items = await getItems();
      console.log("hola")
      console.log(items)
      setItems(items);
    };
    fetchItems();
  }, []);
  
  return (
    <div className="App">
    <h1>ShopBridge</h1>
    {/* <AddItemForm /> */}
    <ItemList items={items} />

  </div>
  );
}

export default App;