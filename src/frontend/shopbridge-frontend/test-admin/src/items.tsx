import { List, Datagrid, TextField, ReferenceField, EditButton, Create, SimpleForm, ReferenceInput , TextInput} from "react-admin";

const postFilters = [
    <TextInput source="q" label="Search" alwaysOn />,
    <TextInput source="title" label="Title" />
];

export const ItemList = () => (
  <List filters={postFilters}>
   <Datagrid>
    <TextField source="id" />
    <TextField source="name" />
    <EditButton />
    </Datagrid>
  </List>
);

export const ItemCreate = () => (
      <Create>
        <SimpleForm>
          <TextInput source="name" />
          <TextInput source="description" multiline rows={5} />
          <TextInput source="price" />
          <TextInput source="quantity"  />
        </SimpleForm>
      </Create>
    );