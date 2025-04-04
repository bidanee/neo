## 알아두기
### a tag에서 onclick을 사용하고 싶을 때

```
function gohome() {
	location.href=`user.html?id=${id}`;
}

<a href="javascript:void(0);" onclick="gohome();">Home</a>
```
