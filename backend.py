// backend/app.js
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');
require('dotenv').config();

const app = express();
app.use(cors());
app.use(express.json());

// MongoDB connection
mongoose.connect(process.env.MONGO_URI)
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.log(err));

// Models
const User = mongoose.model('User', new mongoose.Schema({
  name: String,
  email: { type: String, unique: true },
  password: String,
  role: { type: String, enum: ['admin', 'staff', 'customer'], default: 'customer' }
}));

const Table = mongoose.model('Table', new mongoose.Schema({
  date: String,
  time: String,
  guests: Number,
  customerEmail: String
}));

const MenuItem = mongoose.model('MenuItem', new mongoose.Schema({
  name: String,
  description: String,
  price: Number,
  image: String,
  category: String
}));

// Auth APIs
app.post('/api/auth/register', async (req, res) => {
  const user = new User(req.body);
  user.password = await bcrypt.hash(user.password, 12);
  await user.save();
  res.json({ message: 'User registered', user });
});

app.post('/api/auth/login', async (req, res) => {
  const user = await User.findOne({ email: req.body.email });
  if (!user || !(await bcrypt.compare(req.body.password, user.password))) {
    return res.status(401).json({ message: 'Invalid credentials' });
  }
  const token = jwt.sign({ id: user._id, role: user.role }, process.env.JWT_SECRET);
  res.json({ token });
});

// Table Booking
app.post('/api/bookings', async (req, res) => {
  const exists = await Table.findOne({ date: req.body.date, time: req.body.time });
  if (exists) return res.status(400).json({ message: 'Slot already booked' });
  const booking = new Table(req.body);
  await booking.save();
  res.json(booking);
});

// Menu Management
app.post('/api/menu', async (req, res) => {
  const item = new MenuItem(req.body);
  await item.save();
  res.json(item);
});

app.get('/api/menu', async (req, res) => {
  const items = await MenuItem.find();
  res.json(items);
});

// Server listen
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running at http://localhost:${PORT}`));
