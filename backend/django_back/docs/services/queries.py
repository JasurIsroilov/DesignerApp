from itertools import groupby

from django.template.loader import render_to_string

from docs.models import DocumentCategoriesModel, DocumentsModel


def get_docs() -> dict:
    res = {}
    grouped_docs = groupby(DocumentsModel.objects.all().order_by('category_id'),
                           key=lambda x: x.category_id)
    for key, items in grouped_docs:
        res[key] = sorted([item for item in items])
    return res


def get_tree_structure() -> str:

    template_elem = []
    template_path = 'docs/treemaker_extra/{}'

    def print_tree(elem):
        template_elem.append(render_to_string(
            template_name=template_path.format('treemaker_top.html'),
            context={'elem': elem}
        ))
        root = by_parent_tree.get(elem.id)
        if root:
            for child in root:
                print_tree(child)
        else:
            if documents.get(elem.id):
                template_elem.append(render_to_string(
                    template_name=template_path.format('treemaker_doc.html'),
                    context={'elem': elem,
                             'documents': documents.get(elem.id)}
                ))
            else:
                template_elem.append(render_to_string(
                    template_name=template_path.format('treemaker_empty.html'),
                ))

        template_elem.append(render_to_string(
            template_name=template_path.format('treemaker_bottom.html'),
        ))

    res = list(DocumentCategoriesModel.objects.all().order_by('parent_id'))
    data = groupby(res, key=lambda x: x.parent_id)
    by_parent_tree = {}
    trees_root = []

    for key, items in data:
        by_parent_tree[key] = sorted([item for item in items])

    for query_obj in res:
        if query_obj.level == 0:
            trees_root.append(query_obj)

    documents = get_docs()

    for lvl_elem in sorted(trees_root):
        print_tree(lvl_elem)

    return ''.join(template_elem)
