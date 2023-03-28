from django.db import models

class Firma(models.Model):
    firma_adi = models.CharField(max_length=50)
    yetkili = models.CharField(max_length=100)
    telefon = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.firma_adi
    
class Kasa(models.Model):
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50,blank=True, null=True)
    seri_no = models.CharField(max_length=50,blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    firma = models.ForeignKey(Firma,on_delete=models.PROTECT,related_name="kasa")
    
    def __str__(self):
        return self.marka
class PSU(models.Model):
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50,blank=True, null=True)
    seri_no = models.CharField(max_length=50,blank=True, null=True)
    watt = models.CharField(max_length=10)
    time_stamp = models.DateTimeField(auto_now_add=True)
    garanti = models.BooleanField(default=False)
    garanti_bitis_tarihi = models.DateTimeField(blank=True,null=True)
    firma = models.ForeignKey(Firma,on_delete=models.PROTECT,related_name="psu")
    def __str__(self):
        return '{0}/{1}'.format(self.marka,self.watt)    
    

class MotherBoard(models.Model):
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    seri_no = models.CharField(max_length=50,blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    garanti = models.BooleanField(default=False)
    garanti_bitis_tarihi = models.DateTimeField(blank=True,null=True)
    firma = models.ForeignKey(Firma,on_delete=models.PROTECT,related_name="motherboard")
    
    def __str__(self):
        return '{0}/{1}'.format(self.marka,self.model) 
    
    
class CPU(models.Model):
    OPTIONS = (
        ('Intel', 'Intel'),
        ('AMD', 'AMD')
    )
    marka = models.CharField(max_length=50,choices=OPTIONS,default='Intel')
    model = models.CharField(max_length=50)
    seri_no = models.CharField(max_length=50,blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    garanti = models.BooleanField(default=False)
    garanti_bitis_tarihi = models.DateTimeField(blank=True,null=True)
    firma = models.ForeignKey(Firma,on_delete=models.PROTECT,related_name="cpu")
    
    def __str__(self):
        return '{0}/{1}'.format(self.marka,self.model) 
    
class Ram(models.Model):
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    capacity = models.CharField(max_length=50) 
    mhz = models.CharField(max_length=50)
    seri_no = models.CharField(max_length=50,blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    garanti = models.BooleanField(default=False)
    garanti_bitis_tarihi = models.DateTimeField(blank=True,null=True)
    firma = models.ForeignKey(Firma,on_delete=models.PROTECT,related_name="ram")
    
    def __str__(self):
        return '{0}/{1}'.format(self.marka,self.mhz) 


class GPU(models.Model):
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    capacity = models.CharField(max_length=50) 
    seri_no = models.CharField(max_length=50,blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    garanti = models.BooleanField(default=False)
    garanti_bitis_tarihi = models.DateTimeField(blank=True,null=True)
    firma = models.ForeignKey(Firma,on_delete=models.PROTECT,related_name="gpu")
    
    def __str__(self):
        return '{0}/{1}'.format(self.marka,self.model) 
    
class Monitor(models.Model):
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    curved = models.BooleanField(default=False)
    hz = models.CharField(max_length=50) 
    seri_no = models.CharField(max_length=50,blank=True, null=True)
    garanti = models.BooleanField(default=False)
    garanti_bitis_tarihi = models.DateTimeField(blank=True,null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    firma = models.ForeignKey(Firma,on_delete=models.PROTECT,related_name="monitor")
    
    def __str__(self):
        return '{0}/{1}'.format(self.marka,self.model) 
    
class Kulaklık(models.Model):
    OPTIONS = (
        ('Siyah', 'Siyah'),
        ('Boş', 'Boş')
    )
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50,default='Boş')
    strap_renk = models.CharField(max_length=50,choices=OPTIONS,blank=True, null=True)
    seri_no = models.CharField(max_length=50,blank=True, null=True)
    garanti = models.BooleanField(default=False)
    garanti_bitis_tarihi = models.DateTimeField(blank=True,null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    firma = models.ForeignKey(Firma,on_delete=models.PROTECT,related_name="kulaklık")
    
    def __str__(self):
        return '{0}/{1}'.format(self.marka,self.model) 
    
class Klavye(models.Model):
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    mekanik = models.BooleanField(default=False)
    seri_no = models.CharField(max_length=50,blank=True, null=True)
    garanti = models.BooleanField(default=False)
    garanti_bitis_tarihi = models.DateTimeField(blank=True,null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    firma = models.ForeignKey(Firma,on_delete=models.PROTECT,related_name="klavye")
    
    def __str__(self):
        return '{0}/{1}'.format(self.marka,self.model) 
    
class Mouse(models.Model):
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    seri_no = models.CharField(max_length=50,blank=True, null=True)
    garanti = models.BooleanField(default=False)
    garanti_bitis_tarihi = models.DateTimeField(blank=True,null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    firma = models.ForeignKey(Firma,on_delete=models.PROTECT,related_name="mouse")
    
    def __str__(self):
        return '{0}/{1}'.format(self.marka,self.model) 
    
class MousePad(models.Model):
    olcu = models.CharField(max_length=50)
    firma = models.ForeignKey(Firma,on_delete=models.PROTECT,related_name="mousepad")
    time_stamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '{0}'.format(self.olcu) 
    

class Koltuk(models.Model):
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50,blank=True, null=True)
    seri_no = models.CharField(max_length=50,blank=True, null=True)
    garanti = models.BooleanField(default=False)
    garanti_bitis_tarihi = models.DateTimeField(blank=True,null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    firma = models.ForeignKey(Firma,on_delete=models.PROTECT,related_name="koltuk")
    
    def __str__(self):
        return '{0}/{1}'.format(self.marka,self.model) 
    
class PC(models.Model):
    choise = (
        ('VIP','VIP'),
        ('Normal','Normal'),
    )
    name = models.CharField(max_length=50,blank=True, null=True,default='PC')
    role = models.CharField(max_length=50,choices=choise,default='Normal')
    kasa = models.ForeignKey(Kasa,on_delete=models.CASCADE,related_name="pc")
    psu = models.ForeignKey(PSU,on_delete=models.CASCADE,related_name="pc")
    motherboard = models.ForeignKey(MotherBoard,on_delete=models.CASCADE,related_name="pc")
    cpu = models.ForeignKey(CPU,on_delete=models.CASCADE,related_name="pc")
    ram = models.ManyToManyField(Ram,blank=True,null=True)
    gpu = models.ForeignKey(GPU,on_delete=models.CASCADE,related_name="pc",blank=True,null=True)
    monitor = models.ForeignKey(Monitor,on_delete=models.CASCADE,related_name="pc",blank=True,null=True)
    headset = models.ForeignKey(Kulaklık,on_delete=models.CASCADE,related_name="pc",blank=True,null=True)
    klavye = models.ForeignKey(Klavye,on_delete=models.CASCADE,related_name="pc",blank=True,null=True)
    mouse = models.ForeignKey(Mouse,on_delete=models.CASCADE,related_name="pc",blank=True,null=True)
    mouse_pad = models.ForeignKey(MousePad,on_delete=models.CASCADE,related_name="pc",blank=True,null=True)
    koltuk = models.ForeignKey(Koltuk,on_delete=models.CASCADE,related_name="pc",blank=True,null=True)
    
    