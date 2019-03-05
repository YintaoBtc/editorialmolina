from django.db import models


class Writer(models.Model):

    name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)
    image = models.ImageField(verbose_name = "Imagen", upload_to="writer")
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.name


class Book(models.Model):

    title = models.CharField(max_length = 150, verbose_name = "Titulo")
    subtitle = models.CharField(max_length=150, verbose_name = "Subtítulo")
    description = models.TextField(verbose_name = "Contenido")
    autor = models.ForeignKey(Writer, on_delete=models.CASCADE, related_name="get_books")
    ISBN = models.CharField(max_length = 150, null=True, blank=True)
    img_front = models.ImageField(verbose_name = "Imagen Delantera", upload_to="books")
    img_back = models.ImageField(verbose_name = "Imagen Trasera", upload_to="media/books")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha Creación")
    modified = models.DateTimeField(auto_now=True, verbose_name = "Fecha Edición")

   # class Meta:
    #    verborse_name = "libro"
     #   verborse_name_plural = "libros"
      #  ordering = ["-created"]
    
    
    def __str__(self):
        return self.title

    
