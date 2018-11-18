const express = require('express')
const app = express()
const port = 3000

const inboxMessagesRoutes = require('./routers/inboxMessagesRoutes');
const groupMessagesRoutes = require('./routers/groupMessagesRoutes');
const usersRoutes = require('./routers/usersRoutes');
const groupsRoutes = require('./routers/groupsRoutes');

app.get('/', (req, res) => res.send('Hello World!'))
app.use('/inbox', inboxMessagesRoutes);
app.use('/users', usersRoutes);
app.use('/groups', groupsRoutes);
app.use('/groups', groupMessagesRoutes);

app.listen(port, () => console.log(`Server gate listening on port ${port}!`))
