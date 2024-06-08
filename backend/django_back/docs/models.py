from django.db.models import (
    Model,
    IntegerField,
    CharField,
    ForeignKey,
    DateTimeField,
    FileField,
    SET_NULL,
    PROTECT,
    CASCADE,
)


class DocumentsModel(Model):
    name = CharField(max_length=100, null=False)
    uploaded_at = DateTimeField(auto_now_add=True)
    doc_path = FileField(upload_to='docs/%Y/%m/%d/')
    category = ForeignKey(to='DocumentCategoriesModel', on_delete=SET_NULL, null=True)

    def save(self, *args, **kwargs):
        self.name = str(self.doc_path)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def __ge__(self, other):
        return True if self.name >= other.name else False

    def __le__(self, other):
        return True if self.name <= other.name else False

    def __lt__(self, other):
        return True if self.name < other.name else False

    def __ne__(self, other):
        return True if self.name != other.name else False


class DocumentCategoriesModel(Model):
    name = CharField(max_length=60, null=False)
    level = IntegerField()
    parent = ForeignKey(to='self', null=True, on_delete=PROTECT)

    def save(self, *args, **kwargs):
        if not self.parent:
            self.level = 0
        else:
            self.level = self.parent.level + 1
        super().save(*args, **kwargs)

    def __str__(self):
        cur = self
        res = [f'{self.name}']
        while cur.parent:
            res.append(f'{cur.parent.name}->')
            cur = cur.parent
        return ''.join(reversed(res))

    def __ge__(self, other):
        return True if self.name >= other.name else False

    def __le__(self, other):
        return True if self.name <= other.name else False

    def __lt__(self, other):
        return True if self.name < other.name else False

    def __ne__(self, other):
        return True if self.name != other.name else False


class DynamicFormModel(Model):
    field_name = CharField(max_length=40, null=False)
    field_type = CharField(max_length=40, null=False)
    field_label = CharField(max_length=60, null=False)
    field_validator = CharField(max_length=100, null=True)
    field_class = CharField(max_length=40, null=True)

    def __str__(self):
        return self.field_label


class DocsFormLinkModel(Model):
    doc = ForeignKey(to='DocumentsModel', on_delete=CASCADE, null=False)
    form = ForeignKey(to='DynamicFormModel', on_delete=CASCADE, null=False)
