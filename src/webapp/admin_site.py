from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _

class CustomAdminSite(AdminSite):
    site_header = _('COREEVENTOS: Administración Django')
    site_title = _('Admin Django')
    index_title = _('Panel de Gestión')

    def get_app_list(self, request):
        original_app_list = super().get_app_list(request)

        custom_apps_order = [
            'app_servicio',
            'app_cliente',
            'app_empleado',
            'app_coordinador',
            'app_reservaservicio',
        ]

        gestion_models = []
        auth_app_data = None
        other_non_custom_apps = []
        
        for app in original_app_list:
            if app['app_label'] in custom_apps_order:
                for model in app['models']:
                    model_copy = model.copy()
                    model_copy['original_app_label'] = app['app_label']
                    gestion_models.append(model_copy)
            elif app['app_label'] == 'auth':
                auth_app_data = app
            else:
                other_non_custom_apps.append(app)
        
        gestion_models.sort(key=lambda x: custom_apps_order.index(x['original_app_label']))

        gestion_app_entry = {
            'name': 'Gestión',
            'app_label': 'gestion_custom',
            'models': gestion_models,
        }

        ordered_app_list = [gestion_app_entry]

        ordered_app_list.extend(other_non_custom_apps)

        if auth_app_data:
            ordered_app_list.append(auth_app_data)

        return ordered_app_list

custom_admin_site = CustomAdminSite(name='my_custom_admin')