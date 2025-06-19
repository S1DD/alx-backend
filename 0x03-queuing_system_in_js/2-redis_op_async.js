import { createClient} from 'redis';

const client = createClient();

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

client.on('connect', () => {
    console.log("Redis client connected to the server");
});

const setNewSchool = (schoolName, value) => {
   await client.SET(schoolName, value, print);
};

const displaySchoolValue = async (schoolName) => {
    console.log(await promisify(client.GET).bind(client)(schoolName));
};


async function main() {
    await displaySchoolValue('ALX');
    setNewSchool('ALXSanFrancisco', 100);
    await displaySchoolValue('ALXSanFrancisco');
};

client.on('connect', async () => {
  console.log('Redis client connected to the server');
  await main();
});
