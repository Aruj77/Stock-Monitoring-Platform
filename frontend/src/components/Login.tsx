import { useState } from 'react';
import { TextField, Button, Grid } from '@mui/material';
import axios from 'axios';

const Login: React.FC = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    axios.post('/api/login/', { username, password })
      .then(response => {
        console.log(response.data);
        // Redirect to dashboard upon successful login
        window.location.href = "/dashboard";
      })
      .catch(error => {
        console.error(error);
        // Handle login error
      });
  };

  return (
    <Grid container alignItems="center" style={{ height: '100vh' }}>
      <Grid item xs={4}>
        <form onSubmit={handleLogin}>
          <TextField
            label="Username"
            variant="outlined"
            fullWidth
            margin="normal"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <TextField
            type="password"
            label="Password"
            variant="outlined"
            fullWidth
            margin="normal"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <Button variant="contained" color="primary" fullWidth type="submit">
            Login
          </Button>
        </form>
      </Grid>
    </Grid>
  );
};

export default Login;
