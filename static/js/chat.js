
function send(headSrc,str){
	var html="<div class='send'><div class='msg'><img src="+headSrc+" />"+
	"<p><i class='msg_input'></i>"+str+"</p></div></div>";
	upView(html);
}

function show(headSrc,str){
	var html="<div class='show'><div class='msg'><img src="+headSrc+" />"+
	"<p><i class='msg_input'></i>"+str+"</p></div></div>";
	upView(html);
}

function upView(html){
	$('.message').append(html);
	$('body').animate({scrollTop:$('.message').outerHeight()-window.innerHeight},200)
}
function sj(){
	return parseInt(Math.random()*10)
}
$(function(){
	$('.footer').on('keyup','input',function(){
		if($(this).val().length>0){
			$(this).next().css('background','#114F8E').prop('disabled',true);
		
		}else{
			$(this).next().css('background','#ddd').prop('disabled',false);
		}
	})
	$('.footer p').click(function(){
		show("static/images/touxiangm.png",$(this).prev().val());
		$.ajax({  
		     url: 'http://47.104.157.19:8080//chat',  // 请求地址
			 data: {"question": JSON.stringify($(this).prev().val())},  // 传输数据
			 success:function(res,status){  // 请求成功的回调函数
			 	test([res.replate('"',"")]);
			 	console.log(res)
			 },
			 error: function(error) {}  // 请求失败的回调函数
		});
	})
})


var arr=["Good night!"];
test(arr)
function test(arr){
	$(arr).each(function(i){
		setTimeout(function(){
			send('static/images/touxiang.png',arr[i])
		},sj()*500)
	})
}