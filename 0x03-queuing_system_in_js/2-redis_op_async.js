import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue() {
    try {
        console.log('School');
        const schoolReply = await getAsync('school');
        console.log(`Reply: ${schoolReply}`);

        console.log('Course');
        const courseReply = await getAsync('course');
        console.log(`Reply: ${courseReply}`);
    } catch (error) {
        console.error('Error:', error);
    } finally {
        client.quit();
    }
}

client.on('connect', () => {
    console.log('Redis client connected to the server');
    displaySchoolValue();
});
