import { AUTH_LOGIN, AUTH_LOGOUT, AUTH_ERROR, AUTH_CHECK, AUTH_GET_PERMISSIONS } from 'react-admin';
import decodeJwt from 'jwt-decode';

const apiUrl = 'http://localhost:8000/api';

const authProvider = (type: string, params: any) => {
  if (type === AUTH_LOGIN) {
    const { username, password } = params;
    const request = new Request(`${apiUrl}/auth/login`, {
      method: 'POST',
      body: JSON.stringify({ email: username, password }),
      headers: new Headers({ 'Content-Type': 'application/json' }),
    });

    return fetch(request)
      .then((response) => {
        if (response.status < 200 || response.status >= 300) {
          throw new Error(response.statusText);
        }
        return response.json();
      })
      .then((data) => {
        localStorage.setItem('token', data.access_token);
        return Promise.resolve();
      });
  }

  if (type === AUTH_LOGOUT) {
    localStorage.removeItem('token');
    return Promise.resolve();
  }

  if (type === AUTH_ERROR) {
    const status = params.status;
    if (status === 401 || status === 403) {
      localStorage.removeItem('token');
      return Promise.reject();
    }
    return Promise.resolve();
  }

  if (type === AUTH_CHECK) {
    const token = localStorage.getItem('token');
    if (!token) {
      return Promise.reject();
    }
    const { exp } = decodeJwt(token);
    if (Date.now() / 1000 > exp) {
      localStorage.removeItem('token');
      return Promise.reject();
    }
    return Promise.resolve();
  }

  return Promise.resolve();
};

export default authProvider;
