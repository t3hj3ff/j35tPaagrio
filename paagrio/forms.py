from django import forms


class SubmitIssueForm(forms.Form):
    issue_title = forms.CharField(max_length=255)
    issue_description = forms.Textarea()
