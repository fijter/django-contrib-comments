===========================
Django Custom Comments
===========================

Django used to include a comments framework; since Django 1.6 it's been
separated to a separate project. This is that project.

This framework can be used to attach comments to any model, so you can use it
for comments on blog entries, photos, book chapters, or anything else.

For details, `consult the documentation`__.

__ http://django-contrib-comments.readthedocs.org/



Changes between this version and the official version
-----------------------------------------------------

I have changed the primary model to use a PostiveIntegerField rather than a
TextField to store the foreign key for the "attached" model. Thus the
GenericForeignKey can only be attached to models with PositiveIntegerFields
as their primary key (which is all standard models).

This change prevents a variety of complex bugs with Postgres, because Postgres
does not automatically cast strings to integers.

The final result is the ability to use this model with a GenericRelation on the
"attached" model, allowing better references between models and the ability
to use the database to offload counting and other processing.
