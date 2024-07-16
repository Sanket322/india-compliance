from frappe.custom.doctype.custom_field.custom_field import (
    create_custom_fields as _create_custom_fields,
)

from india_compliance.income_tax_india.constants.custom_fields import CUSTOM_FIELDS


def after_install():
    print("in after install of setup of income tax india")
    create_custom_fields()


def create_custom_fields():
    _create_custom_fields(CUSTOM_FIELDS, ignore_validate=True)
