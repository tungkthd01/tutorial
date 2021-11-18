from django.db import models
from user.models import clients
from user.models import users
class Events(models.Model):
    event_id = models.IntegerField(null=False,primary_key=True)
    client_id = models.ForeignKey(clients,on_delete=models.CASCADE,related_name='events')
    type =models.SmallIntegerField(null=False, choices=[(1, 'Live stream event'),(2,'Offline event')])
    title = models.CharField(max_length=255,null=False)
    body = models.TextField(null=False)
    is_private = models.BooleanField(null=False)
    private_key = models.CharField(max_length=255)
    is_archived = models.BooleanField(null=False)
    created_at = models.DateTimeField(null=False,auto_now_add=True)
    updated_at = models.DateTimeField(null=False,auto_now=True)
    class Meta:
        db_table = 'events'

class Image_paths(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(users,on_delete=models.CASCADE)
    event_id = models.ForeignKey(Events,on_delete=models.CASCADE)
    # box_notification_trans_content_id = models.ForeignKey(box_notification_trans_content)
    file_name = models.CharField(max_length=255, null=False)
    dir_path = models.CharField(max_length=255, null=False)
    image_url = models.CharField(max_length=255, null=False)
    display_order = models.SmallIntegerField(null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)

    class Meta:
        db_table = "image_path"
# class event_authorized_users(models.Model):
#     event_id = models.IntegerField(primary_key=True,null=False)
#     user_id = models.ForeignKey(null=False)
#     created_at = models.DateTimeField(null=False)
#     updated_at = models.DateTimeField(null=False)
#
#
class Performances(models.Model):
    performance_id = models.IntegerField(primary_key=True, null=False)
    event_id = models.ForeignKey(Events,null=False,on_delete=models.CASCADE,related_name="events")
    # streaming_method = models.SmallIntegerField(choices={1:'App',2: 'OBS'})
    # name = models.CharField(max_length=255,null=False)
    start_datetime = models.DateTimeField(null=False)
    end_datetime = models.DateTimeField(null=False)
    # capacity = models.IntegerField()
    ticket_available_flag = models.BooleanField(null=False)
    # created_at = models.DateTimeField(null=False)
    # updated_at = models.DateTimeField(null=False)
    class Meta:
        db_table = 'performance'

class Tickets(models.Model):
    ticket_id = models.IntegerField(primary_key=True)
    performance_id =models.ForeignKey(Performances,on_delete=models.CASCADE,related_name='performance')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, null=True,decimal_places=0)
    # points_required = models.DecimalField(max_digits=15,null=True)
    # expiration_datetime = models.DateTimeField()
    drawing_flag = models.BooleanField()
    drawing_application_deadline = models.DateTimeField(null=True)
    drawing_status = models.BooleanField()
    # stamp_available_flag = models.BooleanField()
    # max_number_of_tickets = models.IntegerField()
    # number_of_issued_tickets = models.IntegerField()
    # is_seat_id_assigned = models.BooleanField()
    # created_at = models.DateTimeField(null=False)
    # updated_at = models.DateTimeField(null=False)
    class Meta:
        db_table = 'ticket'

class Drawwings(models.Model):
    ticket_id = models.IntegerField(primary_key=True)
    # user_id  =  models.ForeignKey(users,on_delete=models.CASCADE())
    is_elected = models.BooleanField()
    is_purchased = models.BooleanField()
    created_at = models.DateTimeField(null=False,auto_now=True)
    updated_at = models.DateTimeField(null=False,auto_now_add=True)
#
# class points_package_purchase_histories(models.Model):
#     id = models.IntegerField(null=False,primary_key=True)
#     user_point_id = models.ForeignKey(null=False,on_delete=models.CASCADE())
#     points_package_id = models.ForeignKey(null=False,on_delete=models.CASCADE())
#     payment_amount = models.DecimalField(max_digits=15)
#     purchased_at = models.DateTimeField(null=False)
#     apple_trans_id = models.CharField(max_length=255)
#     google_trans_id = models.CharField(max_length=255)
#     apple_receipt = models.TextField()
#     google_receipt = models.TextField()
#     created_at = models.DateTimeField(null=False)
#     updated_at = models.DateTimeField(null=False)
#
# class point_spending_histories(models.Model):
#     id = models.IntegerField(primary_key=True, null=False)
#     user_point_id = models.ForeignKey(null=False,on_delete=models.CASCADE())
#     user_gift_id = models.ForeignKey(null=False,on_delete=models.CASCADE())
#     spent_at =models.DateTimeField(null=False)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#
# class gifts(models.Model):
#     gift_id = models.IntegerField(null=False,primary_key=True)
#     client_id = models.ForeignKey(client,null=False,on_delete=models.CASCADE())
#     name = models.CharField(max_length=255,null=False)
#     point_spent = models.DecimalField(max_digits=15,null=False)
#     image_url = models.CharField(max_length=255,null=False)
#     display_order = models.SmallIntegerField(null=False)
#     created_at = models.DateTimeField(null=False)
#     updated_at = models.DateTimeField(null=False)
#
# class gift_purchase_histories(models.Model):
#     id = models.IntegerField(null=False, primary_key=True)
#     user_gift_id = models.ForeignKey(null=False,on_delete=models.CASCADE())
#     user_point_id = models.ForeignKey(null=False,on_delete=models.CASCADE())
#     points_spent = models.DecimalField(max_digits=15)
#     purchase_at = models.DateTimeField(null=False)
#     created_at = models.DateTimeField(null=False)
#     updated_at = models.DateTimeField(null=False)
#
# class gift_tipping_histories(models.Model):
#     id = models.IntegerField(null=False, primary_key=True)
#     user_gift_id = models.ForeignKey(, on_delete=models.CASCADE())
#     user_point_id = models.ForeignKey(null=False, on_delete=models.CASCADE())
#     points_equivalent = models.DecimalField(max_digits=15)
#     tipped_at = models.DateTimeField(null=False)
#     created_at = models.DateTimeField(null=False)
#     updated_at = models.DateTimeField(null=False)
#
# class stamp_codes(models.Model):
#     stamp_code_id = models.IntegerField(null=False, primary_key=True)
#     client_id = models.ForeignKey(client, null=False, on_delete=models.CASCADE())
#     name = models.CharField(max_length=255)
#     code = models.CharField(max_length=6)
#     stamps_granted = models.DecimalField(max_digits=15)
#     number_of_applicable_users = models.IntegerField()
#     number_of_applied_users = models.IntegerField(null=False)
#     expires_in = models.DateTimeField(null=False)
#     created_at = models.DateTimeField(null=False)
#     updated_at = models.DateTimeField(null=False)
#

#





















