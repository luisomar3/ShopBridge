import decodeJwt from 'jwt-decode';

const apiUrl = 'http://localhost:8000/api';

const dataProvider = {
  getList: async (resource, params) => {
    const { page, perPage } = params.pagination;
    const { field, order } = params.sort;
    const search = params.filter.q ? `&q=${params.filter.q}` : '';
    const url = `${apiUrl}/items`;
    const options = {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST',
        'Access-Control-Allow-Headers': 'Content-Type, Authorization'
      }};

    const response = await fetch(url, options);
    const totalItems = Number(response.headers.get('X-Total-Count'));
    const data = await response.json();

    return {
      data,
      total: totalItems,
    };
  },

  getOne: async (resource, params) => {
    const url = `${apiUrl}/items/${params.id}`;
    const options = {
      headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
    };

    const response = await fetch(url, options);
    const data = await response.json();

    return {
      data,
    };
  },

  create: async (resource, params) => {
    const url = `${apiUrl}/items`;
    const options = {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(params.data),
    };

    const response = await fetch(url, options);
    const data = await response.json();

    return {
      data,
    };
  },

  update: async (resource, params) => {
    const url = `${apiUrl}/items/${params.id}`;
    const options = {
      method: 'PUT',
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(params.data),
    };

    const response = await fetch(url, options);
    const data = await response.json();

    return {
      data,
    };
  },

  delete: async (resource, params) => {
    const url = `${apiUrl}/items/${params.id}`;
    const options = {
      method: 'DELETE',
      headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
    };

    await fetch(url, options);

    return {
      data: params.previousData,
    };
  },
};

export default dataProvider;
