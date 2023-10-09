import React from 'react';
import { Grid, Paper, Typography, IconButton, Box } from '@mui/material';
import styled from '@emotion/styled';
import { Link } from 'react-router-dom';
import { PhoneCallback, Person, PhotoCamera } from '@mui/icons-material';
import Header from './Header';



const IconWrapper = styled(Paper)(({ theme }) => ({
  width: 80,
  height: 80,
  borderRadius: 15,
  backgroundColor: theme.palette.primary.main,
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
  color: 'white'
}));

const AppIcon = ({ icon: Icon, label, to }) => (
  <Grid item xs={4}>
    <Link to={to} style={{ textDecoration: 'none' }}>
      <IconButton>
        <IconWrapper>
          <Icon fontSize="large" />
        </IconWrapper>
      </IconButton>
      <Typography variant="subtitle2" align="center" fontWeight="semibold">
        {label}
      </Typography>
    </Link>
  </Grid>
);

const Home = () => {
    return (
      <div className="Home">
        <Typography variant="h3" fontWeight="bold" gutterBottom>
          Home
        </Typography>
        <Box mt={2} ml={90} textAlign="left">
  <Header />
</Box>

        <Grid container spacing={3}>
          <AppIcon icon={PhotoCamera} label="Camera" to="/camera" />
          <AppIcon icon={PhoneCallback} label="PhoneInCall" to="/phoneincall" />
          <AppIcon icon={Person} label="Contacts" to="/contacts" />
        </Grid>
      </div>
    );
  };
  

export default Home;
