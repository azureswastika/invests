import Mongoose from 'mongoose';

Mongoose.Promise = global.Promise;

const connect = async () => {
    try {
        await Mongoose.connect(`mongodb://localhost:27017/main`, { useNewUrlParser: true, useUnifiedTopology: true });
        console.log('Connected to mongo');
    }
    catch (err) {
        console.log('Could not connect to MongoDB');
    }
}

export default connect;