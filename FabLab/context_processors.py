from machines.models import Machine

def get_machine_for_menu(request):
	return {'machines_nav': Machine.objects.all(),
			'category_nav': Machine.objects.values_list('category', flat=True).distinct().exclude(category__isnull=True)
			}
