# Generated by Django 3.2.24 on 2024-06-12 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0020_alter_file_preset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='extension',
            field=models.CharField(blank=True, choices=[('mp4', 'MP4 Video'), ('webm', 'WEBM Video'), ('vtt', 'VTT Subtitle'), ('mp3', 'MP3 Audio'), ('pdf', 'PDF Document'), ('jpg', 'JPG Image'), ('jpeg', 'JPEG Image'), ('png', 'PNG Image'), ('gif', 'GIF Image'), ('json', 'JSON'), ('svg', 'SVG Image'), ('perseus', 'Perseus Exercise'), ('graphie', 'Graphie Exercise'), ('zip', 'HTML5 Zip'), ('h5p', 'H5P'), ('zim', 'ZIM'), ('epub', 'ePub Document'), ('bloompub', 'bloom Document')], max_length=40),
        ),
        migrations.AlterField(
            model_name='file',
            name='preset',
            field=models.CharField(blank=True, choices=[('high_res_video', 'High Resolution'), ('low_res_video', 'Low Resolution'), ('video_thumbnail', 'Thumbnail'), ('video_subtitle', 'Subtitle'), ('video_dependency', 'Video (dependency)'), ('audio', 'Audio'), ('audio_thumbnail', 'Thumbnail'), ('audio_dependency', 'audio (dependency)'), ('document', 'Document'), ('epub', 'ePub Document'), ('document_thumbnail', 'Thumbnail'), ('exercise', 'Exercise'), ('exercise_thumbnail', 'Thumbnail'), ('exercise_image', 'Exercise Image'), ('exercise_graphie', 'Exercise Graphie'), ('channel_thumbnail', 'Channel Thumbnail'), ('topic_thumbnail', 'Thumbnail'), ('html5_zip', 'HTML5 Zip'), ('html5_dependency', 'HTML5 Dependency (Zip format)'), ('html5_thumbnail', 'HTML5 Thumbnail'), ('h5p', 'H5P Zip'), ('h5p_thumbnail', 'H5P Thumbnail'), ('zim', 'Zim'), ('zim_thumbnail', 'Zim Thumbnail'), ('qti', 'QTI Zip'), ('qti_thumbnail', 'QTI Thumbnail'), ('slideshow_image', 'Slideshow Image'), ('slideshow_thumbnail', 'Slideshow Thumbnail'), ('slideshow_manifest', 'Slideshow Manifest'), ('imscp_zip', 'IMSCP Zip'), ('bloompub', 'Bloom Document')], max_length=150),
        ),
        migrations.AlterField(
            model_name='localfile',
            name='extension',
            field=models.CharField(blank=True, choices=[('mp4', 'MP4 Video'), ('webm', 'WEBM Video'), ('vtt', 'VTT Subtitle'), ('mp3', 'MP3 Audio'), ('pdf', 'PDF Document'), ('jpg', 'JPG Image'), ('jpeg', 'JPEG Image'), ('png', 'PNG Image'), ('gif', 'GIF Image'), ('json', 'JSON'), ('svg', 'SVG Image'), ('perseus', 'Perseus Exercise'), ('graphie', 'Graphie Exercise'), ('zip', 'HTML5 Zip'), ('h5p', 'H5P'), ('zim', 'ZIM'), ('epub', 'ePub Document'), ('bloompub', 'bloom Document')], max_length=40),
        ),
    ]
