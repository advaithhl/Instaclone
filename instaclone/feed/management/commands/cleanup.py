import logging
from pathlib import Path as pathlib_Path
from shutil import rmtree as shutil_rmtree

from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


def delete_stray_media_dirs(media_dir, logger, dry_run, style):
    # Display warning that this is a test run.
    if dry_run:
        logger.info(
            style.WARNING('NOTE: This is a a dry run! Nothing will be actually'
                          ' deleted.'))
    # Set counters to 0.
    del_no, keep_no, skip_no = 0, 0, 0

    # Set the `media_path` to the directory to iterate through.
    media_path = pathlib_Path(media_dir)
    logger.debug(f"Attempting walk through '{media_path}'...")

    # Iterate through `media_path`.
    for dirname in media_path.iterdir():
        # Check if the file system object is a directory.
        if dirname.is_dir():
            # Check if user with the directory name does not exist.
            if not User.objects.filter(username=dirname.name).exists():
                # Delete the directory, if no such user exists and not dry run.
                if not dry_run:
                    shutil_rmtree(dirname.absolute())
                logger.debug(
                    f"Deleted '{dirname}', as no user named '{dirname.name}'.")
                del_no += 1
            else:
                # Do not delete directory, if user exists.
                logger.debug(
                    f"Keeping '{dirname}', as user '{dirname.name}' exists.")
                keep_no += 1
        else:
            # Check if file name is `.DS_Store` (useless file in macOS).
            if dirname.name == '.DS_Store':
                # Delete the file, if not dry run.
                if not dry_run:
                    dirname.unlink()
                logger.debug(f"Removed '{dirname}'.")
                del_no += 1
            else:
                # Do not delete unknown file.
                logger.debug(f"Skipping '{dirname}' as not a directory.")
                skip_no += 1
    else:
        # Get total count.
        total_count = del_no + keep_no + skip_no
        # Log if nothing to cleanup.
        if total_count == 0:
            logger.info(f"Nothing to cleanup in '{media_path}'.")

    # Log details.
    logger.debug('\nSUMMARY')
    logger.debug('=======')
    logger.info(f'Items deleted: {del_no}')
    logger.info(f'Items skipped: {skip_no}')
    logger.info(f'Items kept   : {keep_no}')
    logger.info(f'Total        : {del_no + keep_no + skip_no}')


class Command(BaseCommand):
    help = 'Remove `media/user/` directory of non-existent users.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--media_dir',
            help='Specify a custom directory to cleanup '
                 '(default: settings.MEDIA_ROOT).',
        )
        parser.add_argument(
            '--dry_run',
            action='store_true',
            help='Show what would be deleted without deleting anything.'
                 '(default: False)'
        )

    def handle(self, *args, **kwargs):
        # Define a custom logger.
        logger = logging.getLogger(__name__)

        # Define a stream handler to write to `self.stdout` and attach it.
        stream_handler = logging.StreamHandler(stream=self.stdout)
        logger.addHandler(stream_handler)

        # If verbosity is 0, the messages will be passed to the root logger
        # which has a default log level of `WARNING`. Hence the `DEBUG` and
        # `INFO` messages here will be ignored.
        # If verbosity is 1, only `INFO` messages are displayed.
        # If verbosity is greater than or equal to 2, both `DEBUG` and `INFO`
        # messages are displayed.
        verbosity = kwargs.get('verbosity')
        if verbosity == 1:
            logger.setLevel(logging.INFO)
        elif verbosity >= 2:
            logger.setLevel(logging.DEBUG)

        delete_stray_media_dirs(
            media_dir=kwargs['media_dir'] if kwargs.get(
                'media_dir') else settings.MEDIA_ROOT,
            logger=logger,
            dry_run=kwargs['dry_run'],
            style=self.style,
        )
