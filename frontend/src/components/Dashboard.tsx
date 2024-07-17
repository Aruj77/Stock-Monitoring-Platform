import { useState, useEffect } from 'react';
import { Typography, Grid } from '@mui/material';
import axios from 'axios';

const Dashboard: React.FC = () => {
  const [watchlist, setWatchlist] = useState<string[]>([]);

  useEffect(() => {
    // Fetch user's watchlist upon component mount
    axios.get('/api/watchlist/')
      .then(response => {
        setWatchlist(response.data.watchlist);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  return (
    <Grid container     alignItems="center" style={{ height: '100vh' }}>
      <Grid item xs={8}>
        <Typography variant="h4" gutterBottom>
          My Watchlist
        </Typography>
        <ul>
          {watchlist.map(symbol => (
            <li key={symbol}>{symbol}</li>
          ))}
        </ul>
      </Grid>
    </Grid>
  );
};

export default Dashboard;
