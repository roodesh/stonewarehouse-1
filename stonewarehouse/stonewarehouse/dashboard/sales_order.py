from __future__ import unicode_literals
from frappe import _

def get_data(data):
	data['non_standard_fieldnames'] = {
		'Delivery Note': 'against_sales_order',
		'Pick List': 'sales_order',
		"Journal Entry": "reference_name",
		"Payment Entry": "reference_name",
		"Payment Request": "reference_name",
		"Auto Repeat": "reference_document",
		"Maintenance Visit": "prevdoc_docname",
	}

	data['transactions'] = [
		{
			'label': _('Fulfillment'),
			"items": ["Sales Invoice", "Pick List", "Delivery Note", "Maintenance Visit"],
		},
		{"label": _("Purchasing"), "items": ["Material Request", "Purchase Order"]},
		{
			'label': _('Manufacturing'),
			'items': ['Work Order']
		},
		{"label": _("Reference"), "items": ["Quotation", "Auto Repeat"]},
		{"label": _("Payment"), "items": ["Payment Entry", "Payment Request", "Journal Entry"]},
	]

	return data
