<<<<<<< HEAD
# Generated by Django 4.1.3 on 2024-08-02 18:14
=======
# Generated by Django 4.1.3 on 2024-08-02 16:18
>>>>>>> 2714c173b9b943c70a5cc942bd498e1f9a698bd0

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_postblog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postblog',
            name='comments',
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='post',
<<<<<<< HEAD
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='content.postblog'),
=======
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='content.postblog'),
>>>>>>> 2714c173b9b943c70a5cc942bd498e1f9a698bd0
            preserve_default=False,
        ),
    ]
