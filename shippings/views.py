from django.shortcuts import render_to_response
from django.template.context import RequestContext
from shippings.forms import PrealertForm

def prealertar(request):

	if request.method == 'POST':
		form = PrealertForm(request.POST)
		if form.is_valid():
			form.cleaned_data['usuario'] = request.user.get_profile()
			print form.cleaned_data
			form.save()
	else:
		form = PrealertForm()
		
	
	return render_to_response('shippings/prealertar.html',{'form': form,}, context_instance=RequestContext(request)) 