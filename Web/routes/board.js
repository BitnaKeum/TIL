var express = require('express');
var router = express.Router();
var mysql = require('mysql');
var pool = mysql.createPool({
    connectionLimit: 5,
    host: 'localhost',
    user: 'root',
    password: 'password1!',
    database: 'tutorial'
});


const multer = require('multer');
const upload = multer({dest: './uploads/'});


router.get('/', function(req, res, next) {
    res.redirect('/board/list/1');
});

/* GET home page. */
router.get('/list/:page', function(req, res, next) {
  pool.getConnection(function(err, connection) {
      var sqlForSelectList = 'SELECT idx, creator_id, title, hit FROM board';
      connection.query(sqlForSelectList, function(err, rows) {
          if(err) console.error('err: ' + err);
          console.log("rows : " + JSON.stringify(rows));
          
          res.render('list', {title: '게시판 전체 글 조회', rows: rows});
          connection.release();
      });
  });
});


// 글쓰기 화면 표시 GET
router.get('/write',function(req, res, next) {
   res.render('write', {title: "게시판 글 쓰기"});
});

// 글쓰기 로직 처리 POST
router.post('/write', upload.single('image'), function(req, res, next) {
    var creator_id = req.body.creator_id;
    var title = req.body.title;
    var content = req.body.content;
    var passwd = req.body.passwd;
    if (req.file)
        var image = req.file.filename;
    var datas = [creator_id, title, content, passwd, image];
    
    pool.getConnection(function(err, connection) {
        var sqlForInsertBoard = "INSERT INTO board(creator_id, title, content, passwd, image) values(?,?,?,?,?)";
        connection.query(sqlForInsertBoard, datas, function(err, rows) {
            if(err) console.error("err : " + err);
            console.log("rows : " + JSON.stringify(rows));
            
            res.redirect('/board');
            connection.release();
        });
    });
});


// 글 조회 로직 처리 GET
router.get('/read/:idx', function(req, res, next) {
    var idx = req.params.idx;
    
    pool.getConnection(function(err, connection) {
        var sql = "SELECT idx, creator_id, title, content, hit, image FROM board WHERE idx=?";
        
        connection.query(sql, [idx], function(err, rows) {
            if(err) console.error("err : " + err);
            console.log("1개 글 조회 결과 확인 : ", rows);
            
            res.render('read', {title: "글 조회", rows: rows[0]});
            connection.release();
        });
    });
});

// 글 수정 화면 표시 GET
router.get('/update', function(req, res, next) {
    var idx = req.query.idx;
    
    pool.getConnection(function(err, connection) {
        if(err) console.error("err : " + err);
        
        var sql = "SELECT idx, creator_id, title, content, hit FROM board WHERE idx=?";
        
        connection.query(sql, [idx], function(err, rows) {
            if(err) console.error("err : " + err);
            console.log("update에서 1개 글 조회 결과 확인 : ", rows);
            
            res.render('update', {title: "글 수정", row: rows[0]});
            connection.release();
        });
    });
});

// 글 수정 로직 처리 POST
router.post('/update', upload.single('image'), function(req, res, next) {
    var idx = req.body.idx;
    var creator_id = req.body.creator_id;
    var title = req.body.title;
    var content = req.body.content;
    var passwd = req.body.passwd;
    if (req.file)
        var image = req.file.filename;
    var datas = [creator_id, title, content, idx, passwd, image];
    
    pool.getConnection(function(err, connection) {
        var sql = "UPDATE board SET creator_id=?, title=?, content=?, image=? WHERE idx=? AND passwd=?";
        connection.query(sql, [creator_id, title, content, image, idx, passwd], function(err, result) {
            console.log(result);
            if(err) console.error("글 수정 중 에러 발생 err : " + err);
            
            if(result.affectedRows == 0) {
                res.send("<script>alert('패스워드가 일치하지 않거나, 잘못된 요청으로 인해 변경되지 않았습니다.');history.back();</script>");
            }
            else {
                res.redirect('/board/read/'+idx);
            }
            connection.release();
        });
    });
});

router.get('/write', function(req,res,next){
    res.render('write', {title: "게시판 글 쓰기"});
});

// 글쓰기 로직 처리 POST
router.post('/write', function(req, res, next) {
    var creator_id = req.body.creator_id;
    var title = req.body.title;
    var content = req.body.content;
    var passwd = req.body.passwd;
    var datas = [creator_id, title, content, passwd];
    
    pool.getConnection(function(err, connection) {
        var sqlForInsertBoard = "INSERT INTO board(creator_id, title, content, passwd) values(?,?,?,?)";
        connection.query(sqlForInsertBoard, datas, function(err, rows) {
            if(err) console.error("err : " + err);
            console.log("rows : " + JSON.stringify(rows));
            
            res.redirect('/board');
            connection.release();
        });
    });
});

// 글 조회 로직 처리 GET
router.get('/read/:idx', function(req, res, next) {
    var idx = req.params.idx;
    
    pool.getConnection(function(err, connection) {
        var sql = "SELECT idx, creator_id, title, content, hit FROM board WHERE idx=?";
        
        connection.query(sql, [idx], function(err, rows) {
            if(err) console.error("err : " + err);
            console.log("1개 글 조회 결과 확인 : ", row);
            
            res.render('read', {title: "글 조회", row: row[0]});
            connection.release();
        });
    });
});

// 글 수정 화면 표시 GET
router.get('/update', function(req, res, next) {
    var idx = req.query.idx;
    
    pool.getConnection(function(err, connection) {
        if(err) console.error("err : " + err);
        
        var sql = "SELECT idx, creator_id, title, content, hit FROM board WHERE idx=?";
        
        connection.query(sql, [idx], function(err, rows) {
            if(err) console.error("err : " + err);
            console.log("update에서 1개 글 조회 결과 확인 : ", rows);
            
            res.render('update', {title: "글 수정", row: rows[0]});
            connection.release();
        });
    });
});

// 글 수정 로직 처리 POST
router.post('/update', function(req, res, next) {
    var idx = req.body.idx;
    var creator_id = req.body.creator_id;
    var title = req.body.title;
    var content = req.body.content;
    var passwd = req.body.passwd;
    var datas = [creator_id, title, content, idx, passwd];
    
    pool.getConnection(function(err, connection) {
        var sql = "UPDATE board SET creator_id=?, title=?, content=? WHERE idx=? AND passwd=?";
        connection.query(sql, [creator_id, title, content, idx, passwd], function(err, result) {
            console.log(result);
            if(err) console.error("글 수정 중 에러 발생 err : " + err);
            
            if(result.affectedRows == 0) {
                res.send("<script>alert('패스워드가 일치하지 않거나, 잘못된 요청으로 인해 변경되지 않았습니다.');history.back();</script>");
            }
            else {
                res.redirect('/board/read/'+idx);
            }
            connection.release();
        });
    });
});


// 글 삭제

router.get('/delete/:idx', function(req, res, next){
    var idx = req.params.idx;
    pool.getConnection(function(err, connection) {
        var sql = 'DELETE FROM board WHERE idx = ?';
        connection.query(sql, [idx], function(err, result) {
            console.log("글 " + idx + " 삭제");
            if(err) console.error("글 삭제 중 에러 발생 err : " + err);
            res.redirect('/board/list/1');
            connection.release();
        });
    });
});




module.exports = router;
