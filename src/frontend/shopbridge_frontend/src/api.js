import axios from 'axios';

const BASE_URL = 'http://localhost:8000/api/';

const api = axios.create({
  baseURL: BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Function to set the access token in the headers of the API requests
const setAccessToken = (token) => {
  if (token) {
    api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  } else {
    delete api.defaults.headers.common['Authorization'];
  }
};

export const registerUser = (data) => api.post('auth/register/', data);

export const loginUser = (data) => api.post('auth/login', data)
  .then(response => {
    // Store the tokens in the app's state or in a cookie

    console.log("ERRORBHERE",data,response)
    localStorage.setItem('access_token', response.data['access_token']);
    localStorage.setItem('refresh_token', response.data['refresh_token']);
    setAccessToken(response.data['access_token']);
    return response;
  });

export const logoutUser = () => {
  // Remove the tokens from the app's state or from the cookie
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
  setAccessToken(null);
  return api.delete('auth/logout/');
};

export const refreshAccessToken = (refreshToken) => api.post('auth/refresh/', { refresh: refreshToken })
  .then(response => {
    const { access } = response.data;
    localStorage.setItem('access_token', access);
    setAccessToken(access);
    return response;
  });

  export const getItems = () => {
    const token = localStorage.getItem('access_token');
    console.log("TOKEN",token)
    return api.get('items/', {
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
    });
  };
  
  export const getItemById = (id) => {
    const token = localStorage.getItem('access_token');
    return api.get(`items/${id}/`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
  };
  
  export const createItem = (data) => {
    const token = localStorage.getItem('access_token');
    return api.post('items/', data, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
  };
  
  export const updateItem = (id, data) => {
    const token = localStorage.getItem('access_token');
    return api.put(`items/${id}/`, data, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
  };
  
  export const deleteItem = (id) => {
    const token = localStorage.getItem('access_token');
    return api.delete(`items/${id}/`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
  };
  
  export const testApiCondition = () => {
    return api.get('items/ping/');
  };
  

// Call this function in your app's initialization code to set the access token from the stored token
const initializeApi = () => {
  const accessToken = localStorage.getItem('access_token');
  setAccessToken(accessToken);
};

export default initializeApi;
