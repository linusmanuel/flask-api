const url = 'http://127.0.0.1:5000/';

import fetch from 'node-fetch';

async function getData(url) {
	try {
		const connection = await fetch(url);

		if (!connection.ok) {
			throw new Error('A requisição falhou');
		}

		const convertedConnection = await connection.json();

		console.log(convertedConnection);
		return convertedConnection;
	} catch (error) {
		console.error('Ocorreu um erro:', error);
	}
}

getData(url);
