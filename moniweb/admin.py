from django.contrib import admin

from .models import Departamento
from .models import Ciudad
from .models import Sede
from .models import TipoTransporte
from .models import Transportista
from .models import Cliente
from .models import Producto
from .models import Pedido
from .models import Envio
from .models import Paquete
from .models import Factura
from .models import Pago
from .models import PedPro
from .models import PaquPro

# Register your models here.


admin.site.register(Departamento)
admin.site.register(Ciudad)
admin.site.register(Sede)
admin.site.register(TipoTransporte)
admin.site.register(Transportista)
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Envio)
admin.site.register(Paquete)
admin.site.register(Factura)
admin.site.register(Pago)
admin.site.register(PedPro)
admin.site.register(PaquPro)