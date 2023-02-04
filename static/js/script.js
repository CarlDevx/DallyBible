const sl23 = "Salmos 23, Versiculo 1: 'O Senhor é meu pastor e nada me faltará'"


function span_show(){
	const text = document.getElementById("msg").innerHTML;
	if (text == sl23){
		contexto = document.getElementById("contexto");
		contexto.innerHTML = "Loren Ipsulum";
		
	};
};
