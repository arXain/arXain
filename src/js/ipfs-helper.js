import * as axios from 'axios';


var ax = axios.create({
      baseURL: 'http://localhost:5000'
      //timeout: 1000
      //headers: {'X-Custom-Header': 'foobar'}
});

function initIpfs() {
    return ax.get('/init/arxain');
}

function upload(formData) {
    return ax.post('/upload/file', formData);
}

function initAuthor(account) {
    return ax.get('/init/author?author_id='+account);
}

function submitManuscript(account, contract, paper) {
    return ax.get('/submit/manuscript?author_id='+account+'&paper_id='+contract+'&paper_directory='+paper);
}

function submitRevision(account, contract, paper) {
    return ax.get('/submit/revision?author_id='+account+'&paper_id='+contract+'&paper_directory='+paper);
}

export { initIpfs, upload, initAuthor, submitManuscript, submitRevision }
