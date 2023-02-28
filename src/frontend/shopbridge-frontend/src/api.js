const API_BASE_URL = 'http://localhost:8000/api';

export const register = async (username, password) => {
  const response = await fetch(`${API_BASE_URL}/auth/register`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password }),
  });
  const data = await response.json();
  return data;
};

export const login = async (username, password) => {
  const response = await fetch(`${API_BASE_URL}/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password }),
  });
  const data = await response.json();
  return data;
};

export const logout = async () => {
  const response = await fetch(`${API_BASE_URL}/auth/logout`, {
    method: 'DELETE',
    headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` },
  });
  return response.ok;
};

export const refreshAccessToken = async () => {
  const response = await fetch(`${API_BASE_URL}/auth/refresh`, {
    method: 'POST',
    headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` },
  });
  const data = await response.json();
  return data;
};

export const getItems = async () => {
  const response = await fetch(`${API_BASE_URL}/items/`, {
    headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` },
  });
  const data = await response.json();
  console.log(data)
  return data;
};

export const getItemById = async (itemId) => {
  const response = await fetch(`${API_BASE_URL}/items/${itemId}`, {
    headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` },
  });
  const data = await response.json();
  return data;
};

export const createItem = async (item) => {
  const response = await fetch(`${API_BASE_URL}/items`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${localStorage.getItem('access_token')}`,
    },
    body: JSON.stringify(item),
  });
  const data = await response.json();
  return data;
};

export const updateItem = async (itemId, item) => {
  const response = await fetch(`${API_BASE_URL}/items/${itemId}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${localStorage.getItem('access_token')}`,
    },
    body: JSON.stringify(item),
  });
  const data = await response.json();
  return data;
};

export const deleteItem = async (itemId) => {
    const response = await fetch(`${API_BASE_URL}/items/${itemId}`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('access_token')}`
      },
    });
    if (!response.ok) {
      throw new Error('Failed to delete item');
    }
    return response.json();
  };
  