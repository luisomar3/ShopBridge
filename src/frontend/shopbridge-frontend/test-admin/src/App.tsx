import { fetchUtils, Admin, Resource, ListGuesser , EditGuesser } from "react-admin";
import simpleRestProvider from 'ra-data-simple-rest';
import jsonServerProvider from "ra-data-json-server";

import { UserList } from "./users";
import  {ItemList, ItemCreate} from "./items"
import { Dashboard } from './dashboard';
import authProvider  from './authProvider';


//Icons
import UserIcon from "@mui/icons-material/Group";
import InventoryIcon from '@mui/icons-material/Inventory';

const httpClient = (url, options = {}) => {
  if (!options.headers) {
      options.headers = new Headers({ Accept: 'application/json' });
  }
  // add your own headers here
  options.headers.set('Access-Control-Allow-Origin','*');
  options.headers.set('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
  options.headers.set('Access-Control-Allow-Headers', 'Content-Type');
  options.headers.set('Access-Control-Max-Age', '300');
  options.headers.set('Access-Control-Expose-Headers', 'Content-Range');
  options.headers.set('Authorization',`Bearer ${localStorage.getItem('token')}`)
  options.headers.set('Content-Type','application/json');

  // Access-Control-Expose-Headers: Content-Range
  console.log("ACA MIERDA")
  console.log(options.headers)
  console.log(options.headers)
  // options.headers.set('Authorization', 'foobar');
  return fetchUtils.fetchJson(url, options);
};
console.log(httpClient)
const dataProvider = simpleRestProvider('http://localhost:8000', httpClient,'X-Total-Count');

const App = () => (
   <Admin authProvider={authProvider} dataProvider={dataProvider} dashboard={Dashboard}>
     <Resource name="api/items" icon={InventoryIcon} list={ItemList} edit={EditGuesser} create={ItemCreate}/>
   </Admin>
  );
  
export default App;