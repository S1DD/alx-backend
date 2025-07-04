import { createClient} from 'redis';

const client = createClient();

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

client.on('connect', () => {
    console.log("Redis client connected to the server");
});

const setNewSchool = (schoolName, value) => {
    client.SET(schoolName, value, print);
};

const displaySchoolValue(schoolName) => {
    client.GET(schoolName, (_err, reply) => {
	console.log(reply);
    });
};

displaySchoolValue('ALX');
setNewSchool('ALXSanFrancisco', 100);
displaySchoolValue('ALXSanFrancisco');
