<!-- NewFile.jsp -->   


<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>회원 정보</title>
</head>

<body>

<%
String id = request.getParameter("id");
String pwd = request.getParameter("pwd");
String repwd = request.getParameter("repwd");
String name = request.getParameter("name");
String month = request.getParameter("month");
String day = request.getParameter("day");
String human = request.getParameter("human");


if(!pwd.equals(repwd)){
	out.println("pwd와 재확인 pw가 일치하지 않습니다"+"<br>");
}else{
	out.println("아이디 : "+id+"<br>");
	out.println("비밀번호 : "+pwd+"<br>");
	out.println("재확인 비밀번호 : "+repwd+"<br>");
	out.println("이름 : "+name+"<br>");
	out.println("생년월일 : "+month+" "+day+"<br>");
	out.println("성별 : "+human+"<br>");
}
%>

</body>
</html>