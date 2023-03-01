import { useEffect, useState } from 'react';
import { getItems } from '../api';
import { Container, Box, Typography, Pagination } from '@mui/material';


import * as React from 'react';
import { styled } from '@mui/material/styles';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemAvatar from '@mui/material/ListItemAvatar';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import Avatar from '@mui/material/Avatar';
import IconButton from '@mui/material/IconButton';
import FormGroup from '@mui/material/FormGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Grid from '@mui/material/Grid';
import FolderIcon from '@mui/icons-material/Folder';
import DeleteIcon from '@mui/icons-material/Delete';

const ITEMS_PER_PAGE = 6;

const ItemListContainer = styled(Container)({
  paddingTop: '50px',
  paddingBottom: '50px',
});

const ItemList = ({ token }) => {
  const [items, setItems] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await getItems(token);
        setItems(response.data);
      } catch (error) {
        console.log(error);
      }
    };

    fetchData();
  }, [token]);

  const indexOfLastItem = currentPage * ITEMS_PER_PAGE;
  const indexOfFirstItem = indexOfLastItem - ITEMS_PER_PAGE;
  const currentItems = items.slice(indexOfFirstItem, indexOfLastItem);

  const pageNumbers = [];
  for (let i = 1; i <= Math.ceil(items.length / ITEMS_PER_PAGE); i++) {
    pageNumbers.push(i);
  }

  const handlePageChange = (event, value) => {
    setCurrentPage(value);
  };

  return (
    <ItemListContainer maxWidth="md">
      <Box sx={{ marginBottom: '20px' }}>
        <Typography variant="h2">List of Items</Typography>
        <ul>
          {currentItems.map((item) => (
            <li key={item.id}>
              <Typography variant="h4">{item.name}</Typography>
              <Typography variant="body1">{item.description}</Typography>
            </li>
          ))}
        </ul>
      </Box>
      <Pagination
        count={pageNumbers.length}
        page={currentPage}
        onChange={handlePageChange}
        color="primary"
        sx={{ justifyContent: 'center' }}
      />
    </ItemListContainer>
  );
};

export default ItemList;
