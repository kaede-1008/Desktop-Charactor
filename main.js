// Electron���̏����ݒ�
const electron = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
let mainWindow;

// �A�v�����������quit
app.on('window-all-closed', function() {
  app.quit();
});

// �A�v���N����̏���
app.on('ready', function() {
  var subpy = require('child_process').spawn('python',['./charactor.py']);
  var rq = require('request-promise');
  var mainAddr = 'http://localhost:5000';

  var openWindow = function() {
    mainWindow = new BrowserWindow({
      'width': 400, 
      'height': 300,
      'transparent': true
      //'frame': false
    });
    mainWindow.loadURL(mainAddr);

    // �I������
    mainWindow.on('closed', function() {
      mainWindow = null;
      subpy.kill('SIGINT');
    });
  };

  var startUp = function() {
    rq(mainAddr)
      .then(function(htmlString) {
        console.log('server started');
        openWindow();
      })
      .catch(function(err) {
        startUp();
      });
  };

  startUp();
});